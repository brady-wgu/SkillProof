# -*- coding: utf-8 -*-
"""Update the Superhuman developer page WITHOUT rebuilding it.

build_links.py --superhuman --publish uses replace-all, which deletes every
table and recreates it. That was correct exactly once, to convert 93 bullets
into 4 tables. It is wrong from then on: new tables get new ids, and every
conditional format, column width and row colour set in the UI is destroyed
with them.

So this is the steady-state path. It changes CELL VALUES in the tables that
already exist, matched by LRPS ID, and rewrites the roll-up line in place. It
never creates, deletes or restructures a table, so hand-applied formatting
survives.

    python sync_superhuman.py            dry run -- prints what would change
    python sync_superhuman.py --commit   apply it

Colour on the Status column is NOT set here, because no API route writes a
conditional format. Set it once in the UI against the exact strings this
writes -- "Up", "Untested", "Down" -- and it will keep applying to every future
sync, because the table is never replaced.
"""
import importlib.util
import io
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
WRITER = r'C:\dev\repos\superhuman-docs-writer'
WRITER_PY = os.path.join(WRITER, '.venv', 'Scripts', 'python.exe')
sys.path.insert(0, WRITER)

_spec = importlib.util.spec_from_file_location('bl', os.path.join(REPO, 'build_links.py'))
bl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bl)

from superhuman_write import _request, get_token  # noqa: E402

# maintenance mode is batch-capped at 25 rows, so updates are sent in chunks.
BATCH = 25


def tables_on_page(doc, page, token):
    """Every table whose parent is this page.

    Paginated, and that is not optional: this doc holds 259 tables and the
    endpoint caps a page at 100 regardless of the limit asked for. Reading only
    the first page found none of ours and the sync reported "nothing to update"
    -- a silent no-op, which is the worst way for a sync to fail.

    Tables are matched by PARENT and by COLUMNS, never by name. Brady renames
    them in the UI ("Dev Server Public Links"), and a sync that keyed off the
    name would quietly stop working the moment he did.
    """
    items, cursor = [], None
    while True:
        params = {'limit': 100}
        if cursor:
            params['pageToken'] = cursor
        payload = _request('GET', '/docs/%s/tables' % doc, token, params=params)
        items.extend(payload.get('items', []))
        cursor = payload.get('nextPageToken')
        if not cursor:
            break
    # Base tables only. A chart VIEW is returned here too and carries the same
    # column names, but writing a row through a view writes through to its base
    # table -- so including them means updating every cell twice, inflating the
    # batch count against the 25-row cap for no effect.
    return [t for t in items
            if (t.get('parent') or {}).get('id') == page
            and t.get('tableType') != 'view']


def read_rows(doc, table_id, token):
    rows, cursor = [], None
    while True:
        params = {'limit': 200, 'valueFormat': 'simple'}
        if cursor:
            params['pageToken'] = cursor
        p = _request('GET', '/docs/%s/tables/%s/rows' % (doc, table_id), token, params=params)
        rows.extend(p.get('items', []))
        cursor = p.get('nextPageToken')
        if not cursor:
            break
    return rows


def columns(doc, table_id, token):
    p = _request('GET', '/docs/%s/tables/%s/columns' % (doc, table_id), token,
                 params={'limit': 100})
    items = p.get('items', [])
    return (dict((c['name'], c['id']) for c in items),
            dict((c['name'], c.get('format') or {}) for c in items))


def check_select_options(table_name, fmt, wanted):
    """Refuse to write a value the Status column cannot style.

    The Status column is a select list, and the colour comes from conditional
    formatting matched on the exact option string. A value that is not an
    option is not rejected by the API -- it is accepted and shown UNSTYLED,
    which is the worst outcome: the sync reports success and the page quietly
    loses the colour it exists to show.

    Caught exactly this on 10 SEP 2026: the options were Up/Unknown/Down while
    this script was writing "Untested".

    The API cannot fix it from here -- /columns is GET-only in the spec -- so
    the only safe move is to stop and say which option is missing.
    """
    if fmt.get('type') != 'select':
        return []                      # a plain text column takes anything
    options = set(o['name'] for o in fmt.get('options') or [])
    missing = sorted(set(wanted) - options)
    if missing:
        print('  %s: Status is a select list missing option(s) %s'
              % (table_name, ', '.join(repr(m) for m in missing)))
        print('     it offers: %s' % ', '.join(sorted(options)))
    return missing


def chunk_ops(ops, cap):
    """Split update operations into payloads of at most `cap` rows each.

    Splits ACROSS tables as well as within one, because the cap counts every
    row in the payload, not per operation.
    """
    batch, count = [], 0
    for op in ops:
        rows = op['rows']
        while rows:
            room = cap - count
            take, rows = rows[:room], rows[room:]
            batch.append({'op': op['op'], 'table': op['table'], 'rows': take})
            count += len(take)
            if count >= cap:
                yield batch
                batch, count = [], 0
    if batch:
        yield batch


def main():
    commit = '--commit' in sys.argv
    data = bl.load(bl.PUBLIC_DATA, 'the public data file')
    private = bl.load(bl.PRIVATE_DATA, 'the private overlay')
    cfg = bl.sh_target(private)
    doc, page = cfg['doc'], cfg['page']

    _changed, measured = bl.merge_status(data, private)
    # Status the developer page should show, per LRPS id. Rows the runner has
    # never launched fall back to whatever the public page carries.
    want = {}
    for s in data['skills']:
        if s['section'] != 'demo':
            want[s['id']] = bl.SH_STATUS[s['status']]
    for sid, (mapped, _at, _v) in measured.items():
        want.setdefault(sid, bl.SH_STATUS[mapped])

    token = get_token(doc)
    ops, report, blocked = [], [], []
    for t in tables_on_page(doc, page, token):
        cols, fmts = columns(doc, t['id'], token)
        if 'LRPS ID' not in cols or 'Status' not in cols:
            report.append('  %-26s skipped (not a link table)' % t['name'])
            continue
        missing = check_select_options(t['name'], fmts.get('Status', {}),
                                       set(bl.SH_STATUS.values()))
        rows = read_rows(doc, t['id'], token)
        updates = []
        for r in rows:
            vals = r.get('values', {})
            sid = str(vals.get(cols['LRPS ID']) or '').strip()
            now = str(vals.get(cols['Status']) or '').strip()
            target = want.get(sid)
            if not target or now == target:
                continue
            if target in missing:
                # Writing this would succeed and render colourless. Skip the
                # cell, keep the rest of the table in sync, and say so.
                blocked.append('  %-26s %-10s %-9s -> %s  SKIPPED, not an option'
                               % (t['name'], sid, now or '(blank)', target))
                continue
            updates.append({'rowId': r['id'],
                            'cells': [{'column': cols['Status'], 'value': target}]})
            report.append('  %-26s %-10s %-9s -> %s'
                          % (t['name'], sid, now or '(blank)', target))
        if updates:
            ops.append({'op': 'update', 'table': t['id'], 'rows': updates})
    if blocked:
        print('BLOCKED -- add these options to the select list first:')
        print('\n'.join(blocked))
        print()

    if report:
        print('status cell changes:')
        print('\n'.join(report))
    else:
        print('every Status cell already matches; nothing to update')

    # maintenance mode refuses a payload touching more than 25 rows, and that
    # guard is worth keeping rather than waving through with --confirm-large:
    # 44 rows in one shot is exactly the kind of write that is unreviewable if
    # it goes wrong. Send it as consecutive payloads under the cap instead, each
    # one a complete, self-consistent write.
    for batch_no, chunk in enumerate(chunk_ops(ops, BATCH), 1):
        rows = sum(len(o['rows']) for o in chunk)
        pf = os.path.join(bl.tempfile.gettempdir(),
                          'skillproof-sh-rows-%d.json' % batch_no)
        json.dump({'doc': doc, 'operations': chunk},
                  io.open(pf, 'w', encoding='utf-8', newline='\n'), indent=2)
        cmd = [WRITER_PY, 'sh_write.py', pf, '--maintenance']
        if commit:
            cmd.append('--commit')
        print('\n--- batch %d: %d row(s) ---' % (batch_no, rows))
        proc = subprocess.run(cmd, cwd=WRITER, capture_output=True, text=True,
                              env=dict(os.environ, PYTHONIOENCODING='utf-8'))
        sys.stdout.write(proc.stdout)
        if proc.stderr.strip():
            sys.stdout.write(proc.stderr)
        if proc.returncode != 0:
            print('ROW WRITE FAILED on batch %d (exit %d) -- stopping here so the '
                  'page is not left half-updated by a repeating error'
                  % (batch_no, proc.returncode))
            return proc.returncode

    # The roll-up. Inserted once above the DEV heading, then SET in place, so a
    # rerun updates the counts instead of stacking another line on the page.
    body = bl.rollup_html(data)
    rf = os.path.join(bl.tempfile.gettempdir(), 'skillproof-sh-rollup.html')
    io.open(rf, 'w', encoding='utf-8', newline='\n').write(body)
    shcfg = private.get('superhuman') or {}
    if shcfg.get('rollupEnabled') is False:
        print('\nroll-up: disabled (removed from the page); skipping')
        return 0

    eid = shcfg.get('rollupElement')
    # A roll-up we created and Brady has since DELETED must stay deleted. He
    # replaced the text line with a pie chart view of the master table on
    # 10 SEP 2026; silently re-adding it every run would be the tool arguing
    # with the person using it. Record the decision so it is not re-litigated.
    if eid and not element_exists(doc, page, eid):
        private['superhuman']['rollupEnabled'] = False
        json.dump(private, io.open(bl.PRIVATE_DATA, 'w', encoding='utf-8',
                                   newline='\n'), indent=2, ensure_ascii=False)
        print('\nroll-up: element %s no longer on the page -- it was deleted '
              'deliberately, so it will not be re-added. Recorded '
              'rollupEnabled=false.' % eid)
        return 0

    # An existing roll-up is SET in place. A new one is inserted AFTER the page
    # description, so the page reads: what this is, then what state it is in.
    verb = 'set' if eid else 'after'
    anchor = eid or shcfg.get('rollupAnchor') or first_element(doc, page)
    cmd = [WRITER_PY, 'sh_page.py', verb, doc, page, anchor, rf,
           '--html', '--maintenance']
    if commit:
        cmd.append('--commit')
    print('\nroll-up: %s %s' % (verb, anchor))
    proc = subprocess.run(cmd, cwd=WRITER, capture_output=True, text=True,
                          env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    sys.stdout.write(proc.stdout)
    if proc.stderr.strip():
        sys.stdout.write(proc.stderr)
    if commit and proc.returncode == 0 and not eid:
        # Learn the id just created and record it. Leaving this to a human is
        # how a page ends up with a stack of roll-ups, one per run.
        found = find_element(doc, page, shcfg.get('rollupMarker') or 'LINK STATUS')
        if found:
            private['superhuman']['rollupElement'] = found
            json.dump(private, io.open(bl.PRIVATE_DATA, 'w', encoding='utf-8',
                                       newline='\n'), indent=2, ensure_ascii=False)
            print('recorded roll-up element %s; future runs update it in place' % found)
        else:
            print('WARNING: could not find the roll-up element just written. '
                  'Record its id as superhuman.rollupElement before the next run, '
                  'or that run will add a second roll-up.')
    return proc.returncode


def element_exists(doc, page, element_id):
    """Is this element still on the page?

    Reads the live element list rather than trusting the recorded id. Note the
    listing can lag a write by about a minute, so this is only ever used to
    detect a DELETION made earlier by a person -- never to confirm something
    this script just wrote.
    """
    out = subprocess.run([WRITER_PY, 'sh_page.py', 'list', doc, page],
                         cwd=WRITER, capture_output=True, text=True,
                         env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    if out.returncode != 0:
        # Could not tell. Assume it exists: wrongly skipping an update is
        # recoverable, wrongly re-adding a deleted block is the thing to avoid.
        return True
    return element_id in out.stdout


def find_element(doc, page, marker):
    """Find a page element by a stable marker in its text."""
    import re
    out = subprocess.run([WRITER_PY, 'sh_page.py', 'list', doc, page],
                         cwd=WRITER, capture_output=True, text=True,
                         env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout
    for line in out.split('\n'):
        if marker.lower() in line.lower():
            m = re.match(r'\s{2}(cl-[\w-]+)\s', line)
            if m:
                return m.group(1)
    return None


def first_element(doc, page):
    out = subprocess.run([WRITER_PY, 'sh_page.py', 'list', doc, page],
                         cwd=WRITER, capture_output=True, text=True,
                         env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout
    import re
    m = re.search(r'^\s{2}(cl-[\w-]+)\s', out, re.M)
    if not m:
        sys.exit('could not find the first element on the page')
    return m.group(1)


if __name__ == '__main__':
    sys.exit(main())
