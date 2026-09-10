# -*- coding: utf-8 -*-
"""Render the LRPS link list onto both surfaces from one data file.

The same 39 provisioning links live on two pages that were, until now, both
maintained by hand:

    index.html                          the public human view (status, dates)
    Superhuman "SkillProof Link List"   the developer view (Client IDs, OIDC and
                                        LTI endpoints, direct launch URLs)

Adding one Skill meant editing 70 KB of hand-authored HTML and a 93-element page
in two formats without drifting. This compiles both from skills.json instead.

    skills.json          PUBLIC, in this repo. Exactly the fields index.html
                         already shows, so publishing it exposes nothing new.
    skills.private.json  PRIVATE, in brady-browser-kit. Client IDs, API
                         hostnames and direct launch URLs, joined on LRPS id.
                         It NEVER reaches the public render -- see assert_clean().

Same contract as build_prototypes.py, deliberately: Python, run by hand at dev
time, commits static HTML. GitHub Pages stays build-free. There is no CI in this
repo and this script does not add any.

    python build_links.py --check                    render and diff, write nothing
    python build_links.py --write                    update index.html
    python build_links.py --status                   merge the runner's verdicts in
    python build_links.py --superhuman               render the developer page
    python build_links.py --superhuman --publish     WRITE it to the live page

The rendered developer body carries Client IDs and internal hostnames, so it
is written to the system temp dir, never inside this repo.

Status is MEASURED, not typed. --status reads the sentry runner's store and maps
its verdicts onto three states. Three, not two, because sentry distinguishes "the
link is dead" from "our test account was the wrong type for it", and publishing
the second as Broken would put a red mark on a world-readable page for a link
that works fine.
"""
import argparse
import difflib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(REPO, 'index.html')
PUBLIC_DATA = os.path.join(REPO, 'skills.json')

# The private overlay lives outside this repo on purpose: this one is public.
PRIVATE_DATA = os.environ.get(
    'SKILLPROOF_PRIVATE',
    r'C:\dev\repos\brady-browser-kit\skills.private.json')

# The nightly runner's verdict state. sentry never writes into this repo -- it
# writes its own store, and this script is the only thing that moves a
# measurement onto a published page. That keeps a scheduled task from dirtying a
# git working tree at 02:30 with nobody watching.
SENTRY_STORE = os.environ.get(
    'SENTRY_STORE',
    r'C:\dev\scratch\skillproof-qa-tools\sentry\store\last-verdict.json')

# ---------------------------------------------------------------------------
# Status vocabulary
# ---------------------------------------------------------------------------
# Three states. The public page had two, and a two-state mapping is actively
# wrong: on 10 SEP 2026 auth::stage::student returned FAIL_LTI while that link
# was perfectly healthy -- the account we launched it with was the wrong type.
# Publishing that as "Broken" tells a reader the product is down when it is not.
#
# Wording and colour match the Superhuman developer page exactly, on
# instruction (10 SEP 2026). One link described in two vocabularies across two
# pages is worse than one page, because a reader has to work out whether
# "Broken" and "Down" mean the same thing.
#
# Down is RED here, where it used to be amber. Amber now carries Unknown,
# where caution is the right reading; a dead link showing caution-yellow
# understated it.
STATUS_UI = {
    'active':     ('green', 'Up'),
    'unverified': ('amber', 'Unknown'),
    'broken':     ('red',   'Down'),
}



VERDICT_MAP = {
    'RENDERED_OK':         'active',
    'EMPTY_BUT_CORRECT':   'active',      # PROD is a student-only pilot; empty
                                          # admin screens are correct, not broken.
    'PASS':                'active',
    'FAIL_LINK_STALE':     'broken',      # "Tool not found" -- registration gone.
    'FAIL_AUTH':           'broken',
    'ERROR_STATE':         'broken',
    'FAIL_LTI':            'unverified',  # link fine, account type mismatched.
    'NOT_CONFIGURED':      'unverified',  # no test account of that type exists.
    'SKELETON_OR_LOADING': 'unverified',
}

ROW = (
    '                <tr class="live" tabindex="0" data-launch="%(url)s" aria-label="%(aria)s">\n'
    '                  <td class="id-cell">%(id)s</td>\n'
    '                  <td class="name-cell lrps-name">%(name)s</td>\n'
    '                  <td><span class="status-pill"><span class="dot %(dot)s"></span>%(label)s</span></td>\n'
    '                  <td class="desc-cell">%(display)s</td>\n'
    '                  <td class="date-cell">%(added)s</td>\n'
    '                </tr>\n'
)

DIVIDER = (
    '                <tr class="section-divider">\n'
    '                  <td colspan="5"><span class="material-icons-outlined" '
    'style="font-size:13px; vertical-align:-2px; margin-right:6px;">%(icon)s</span>%(label)s</td>\n'
    '                </tr>\n'
)


def esc(s):
    """Escape for HTML text and double-quoted attributes alike.

    Deliberately NOT html.escape(quote=True): that also rewrites ' to &#x27;,
    which would churn every apostrophe in the file on the first run and bury the
    real diff. & < > " is the full set this page actually needs.
    """
    return (s.replace('&', '&amp;').replace('<', '&lt;')
             .replace('>', '&gt;').replace('"', '&quot;'))


def load(path, what):
    if not os.path.exists(path):
        sys.exit('missing %s: %s' % (what, path))
    return json.load(io.open(path, encoding='utf-8'))


# ---------------------------------------------------------------------------
# Public render
# ---------------------------------------------------------------------------
def render_tbody(data):
    by_section = {}
    for s in data['skills']:
        by_section.setdefault(s['section'], []).append(s)

    out = []
    for sec in data['sections']:
        # Whatever sat between the previous row and this divider, verbatim:
        # blank lines and the hand-written <!-- SECTION n --> banners. Four
        # banners cover five dividers and one runs to five lines of prose, so
        # they are preserved rather than regenerated. A generator that reformats
        # a human's comments is a generator people stop running.
        out.append(sec['preamble'])
        # label is stored as raw HTML, not text: the dividers use &middot;
        # while the same character appears literally elsewhere in the file,
        # and no escaper can know which form a given spot wants. Store what
        # the file has, write it back unchanged.
        out.append(DIVIDER % {'icon': sec['icon'], 'label': sec['label']})
        for s in by_section.get(sec['slug'], []):
            dot, label = STATUS_UI[s['status']]
            out.append(ROW % {
                'url': esc(s['url']), 'aria': esc(s['ariaLabel']),
                'id': esc(s['id']), 'name': esc(s['name']),
                'dot': dot, 'label': label,
                'display': esc(s['display']), 'added': esc(s['added']),
            })
    out.append(data['tbodyTail'])
    return ''.join(out)


def assert_clean(html_text):
    """Refuse to publish anything from the private overlay onto the public page.

    This is the guard that matters most here. The repo is world-readable; a
    Client ID or an internal API hostname leaking into it is not undone by a
    later commit, because by then it is cloned and indexed.
    """
    banned = [
        (r'teamjft\.com', 'an internal API/app hostname'),
        (r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b',
         'a UUID (Client ID?)'),
        (r'auth/lti/(?:login|launch)', 'a direct LTI endpoint'),
    ]
    for pat, why in banned:
        m = re.search(pat, html_text, re.I)
        if m:
            sys.exit('REFUSED: the rendered public HTML contains %s -- %r'
                     % (why, m.group(0)))


def splice(current, tbody):
    a = current.index('<tbody>') + len('<tbody>')
    b = current.index('</tbody>')
    out = current[:a] + tbody + current[b:]

    # The sidebar advertises a row count. It is the single most likely thing to
    # rot, because nothing forces a human to update it when they add a row.
    n = out.count('<tr class="live"')
    out = re.sub(r'(<span class="badge-count">)\d+(</span>)',
                 r'\g<1>%d\g<2>' % n, out, count=1)
    return out


# ---------------------------------------------------------------------------
# Status merge
# ---------------------------------------------------------------------------
def _persona_of(label):
    """Which sentry persona a Superhuman entry label corresponds to, if any."""
    low = label.lower()
    if 'super admin' in low:
        return 'superadmin'
    if 'school admin' in low or 'tenant admin' in low:
        return 'schooladmin'
    if 'instructor' in low:
        return 'instructor'
    if 'python skill' in low:
        return 'student'
    return None


def merge_status(data, private):
    """Fold the nightly runner's verdicts into skills.json.

    sentry launches one LRPS link per persona per environment, not all 39. Only
    ids it actually launched are touched; every other row keeps what it had, so
    a partial run can never silently blank the page.
    """
    state = load(SENTRY_STORE, 'the sentry store')
    measured = {}
    for scope in state.get('scopes', {}).values():
        at = scope.get('at')
        for check_id, verdict in scope.get('verdicts', {}).items():
            parts = check_id.split('::')
            if len(parts) != 3 or parts[0] != 'auth':
                continue
            env, persona = parts[1], parts[2]
            for sid, rec in private['byId'].items():
                # An explicit persona wins over sniffing the label. "Python
                # (PROD)" is the student entry link but reads nothing like one,
                # so label-sniffing alone silently skips it and PROD Student
                # keeps a hand-typed status forever.
                rec_persona = rec.get('persona') or _persona_of(rec['label'])
                if rec['env'] != env or rec_persona != persona:
                    continue
                mapped = VERDICT_MAP.get(verdict)
                if mapped:
                    measured[sid] = (mapped, at, verdict)

    changed = 0
    for s in data['skills']:
        if s['id'] not in measured:
            continue
        mapped, at, verdict = measured[s['id']]
        if s['status'] != mapped or s.get('statusSource') != 'measured':
            changed += 1
        s['status'] = mapped
        s['statusCheckedAt'] = at
        s['statusSource'] = 'measured'
        s['lastVerdict'] = verdict
    return changed, measured


# ---------------------------------------------------------------------------
# Superhuman render
# ---------------------------------------------------------------------------
def render_superhuman(data, private, measured=None):
    """One HTML table per environment, for sh_page.py --html.

    HTML, never a markdown table: a markdown table imports with columns named
    "Column 1..N" plus a junk data row, and no API route can rename a table or a
    column, so repairing it is UI-only work. sh_page.py's own header says so.
    """
    names = dict((s['id'], s['name']) for s in data['skills'])
    status = dict((s['id'], s['status']) for s in data['skills'])
    # The PROD links are not on the public page, so they have no row in
    # skills.json to carry a status -- but sentry measures them every night.
    # Without this the developer view would print "Unverified" for four links
    # the runner authenticated end-to-end hours earlier.
    for sid, (mapped, _at, _verdict) in (measured or {}).items():
        status.setdefault(sid, mapped)

    out = {}
    for env, meta in private['environments'].items():
        rows = []
        for sid, rec in private['byId'].items():
            if rec['env'] != env:
                continue
            # The public page's name wins. Superhuman still says "Tenant Admin"
            # in one place; one canonical name means that drift cannot return.
            name = names.get(sid, rec['label'])
            note = (' <em>%s</em>' % esc(rec['note'])) if rec.get('note') else ''
            # A direct launch URL we have never resolved is left blank on
            # purpose. Deriving one from the STAGE pattern would look right and
            # publish a link nobody has ever followed, on a page people launch
            # from -- the exact failure the DEV rows already demonstrate.
            if rec.get('directUrl'):
                launch = ('<a href="%s">%s</a>'
                          % (esc(rec['directUrl']), esc(rec['directUrl'])))
            else:
                launch = esc(rec.get('directUrlNote') or 'not captured')
            rows.append(
                '<tr><td>%s</td><td>%s%s</td><td>%s</td>'
                '<td><a href="https://lrps.wgu.edu/provision/%s">%s</a></td>'
                '<td>%s</td></tr>'
                % (esc(sid), esc(name), note,
                   esc(SH_STATUS[status.get(sid, 'unverified')]),
                   esc(sid), esc(sid), launch))
        table = ('<table><thead><tr><th>LRPS ID</th><th>Skill</th><th>Status</th>'
                 '<th>LRPS Link</th><th>Direct LTI Launch</th></tr></thead>'
                 '<tbody>%s</tbody></table>' % ''.join(rows))
        out[env] = {'table': table, 'meta': meta, 'count': len(rows)}

    # The public pages the developer view has never carried: the published
    # landing page and the four click-through walkthroughs. Brady, 10 SEP 2026 --
    # every link belongs in both places; only Client IDs, OIDC/LTI endpoints and
    # internal hosts stay confidential. These have none of those, so the only
    # reason they were missing here is that nobody copied them across.
    pub = []
    for p in data.get('publicPages', []):
        pub.append('<tr><td>%s</td><td>%s</td><td><a href="%s">%s</a></td></tr>'
                   % (esc(p['name']), 'Landing page',
                      esc(p['url']), esc(p['url'])))
    for s in data['skills']:
        if s['section'] != 'demo':
            continue
        url = s['url'] if s['url'].startswith('http') else \
            'https://brady-wgu.github.io/SkillProof/' + s['url']
        pub.append('<tr><td>%s</td><td>%s</td><td><a href="%s">%s</a></td></tr>'
                   % (esc(s['name']), 'Click-through walkthrough, no login',
                      esc(url), esc(url)))
    if pub:
        out['public'] = {
            'table': ('<table><thead><tr><th>Page</th><th>Kind</th><th>URL</th>'
                      '</tr></thead><tbody>%s</tbody></table>' % ''.join(pub)),
            'meta': {}, 'count': len(pub)}
    return out


# The Superhuman doc and page ids live in the PRIVATE overlay, not here. They
# are internal document identifiers and this repo is public; an id alone grants
# nobody access, but it does not belong in a world-readable file either.
def sh_target(private):
    cfg = private.get('superhuman') or {}
    if not cfg.get('doc') or not cfg.get('page'):
        sys.exit('skills.private.json has no superhuman.doc / superhuman.page')
    # Let the overlay override the status wording without touching this file.
    for k, v in (cfg.get('statusLabels') or {}).items():
        if k in SH_STATUS:
            SH_STATUS[k] = v
    return cfg

# Superhuman uses Brady's operational vocabulary, which is not the public page's.
# A reader of the developer page wants "is it up right now"; a reader of the
# public page wants "is this link usable". Same three states, different words,
# so the two are mapped rather than sharing one label.
#
# These strings are not cosmetic. The Status column is a SELECT list whose
# options carry the green/amber/red conditional formatting, and colour is
# applied by exact string match -- a value that is not an option renders
# unstyled. The API cannot create or edit a column (the spec exposes /columns
# as GET only), so the options are set by hand in the UI and this side must
# follow them exactly. Overridable from the private overlay so renaming an
# option is a data edit, not a code change.
SH_STATUS = {'active': 'Up', 'unverified': 'Unknown', 'broken': 'Down'}
SH_DOT = {'active': '🟢', 'unverified': '🟡', 'broken': '🔴'}


ENV_TITLE = {
    'dev':    'DEV',
    'stage':  'STAGE',
    'prod':   'PROD',
    'public': 'Public pages',
}
ENV_ORDER = ['dev', 'stage', 'prod', 'public']


WRITER = r'C:\dev\repos\superhuman-docs-writer'
WRITER_PY = os.path.join(WRITER, '.venv', 'Scripts', 'python.exe')


def publish_superhuman(body_path, doc, page):
    # REFUSED, permanently. This existed to do the one-time conversion of 93
    # bullets into 4 tables, on 10 SEP 2026. It has now done that.
    #
    # The page has since been shaped by hand: H1 headings per environment,
    # horizontal rules between them, CONFIDENTIAL sub-headings, three renamed
    # tables and a description block at the top. replace-all deletes every
    # element and every table and rebuilds from this renderer, which knows about
    # none of it -- so running it again destroys that work and hands back new
    # table ids, taking any conditional formatting with them.
    #
    # sync_superhuman.py is the steady-state path: it changes cell VALUES in the
    # tables that already exist and leaves structure alone.
    sys.exit(
        'REFUSED: replace-all would destroy the hand-built page structure and\n'
        'every table (and its formatting) along with it. The one-time conversion\n'
        'is done. Use:  python sync_superhuman.py --commit')
    """Write the rendered body to the live page, in-process.

    This used to print a command for someone to paste into a terminal. That is
    the wrong shape for this tool: the person who owns this page does not drive
    work from a shell, so a printed command is an unfinished job handed back.

    replace-all rather than element-scoped edits because the page is being
    restructured wholesale -- 93 bullets become 4 tables. It is refused outright
    on a page carrying a table view, since no API can rebuild one; `sh_page.py
    views` reports none on this canvas. The writer emits a rollback file either
    way.
    """
    cmd = [WRITER_PY, 'sh_page.py', 'replace-all', doc, page,
           os.path.abspath(body_path), '--html', '--maintenance', '--commit']
    print('publishing to Superhuman page %s ...' % page)
    # PYTHONIOENCODING is not optional: listing or writing this page crashes on
    # cp1252 against the warning glyph in the D522-13 entry.
    proc = subprocess.run(cmd, cwd=WRITER, capture_output=True, text=True,
                          env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    sys.stdout.write(proc.stdout)
    if proc.stderr.strip():
        sys.stdout.write(proc.stderr)
    if proc.returncode != 0:
        print('PUBLISH FAILED (exit %d) -- the page is unchanged' % proc.returncode)
    return proc.returncode


def rollup_counts(data):
    """Counts behind the roll-up. LRPS links only.

    The four click-through walkthroughs are pages, not launches; folding them
    in would inflate the green number with things the runner never tests.
    """
    lrps = [s for s in data['skills'] if s['section'] != 'demo']
    n = dict((k, 0) for k in SH_STATUS)
    for s in lrps:
        n[s['status']] = n.get(s['status'], 0) + 1
    measured = sum(1 for s in lrps if s.get('statusSource') == 'measured')
    when = max([s.get('statusCheckedAt') or '' for s in lrps] or [''])
    return lrps, n, measured, when


ENV_SHORT = {'dev': 'DEV', 'stage': 'STAGE', 'prod': 'PROD'}


def rollup_html(data):
    """The one line that answers "is anything down", above the three pie charts.

    Brady, 10 SEP 2026: "I expect all links to be up 100% of the time, so if any
    link is DOWN, then we have a problem. The issue isn't the proportion of
    broken links, it's whether the site is down or not."

    So this leads with a VERDICT and names the offenders. It deliberately does
    not lead with a proportion: "36 of 44 up" reads as reassuring when the true
    statement is "five links are down". The counts still appear, after the
    verdict, because the pie charts below break them down per environment.

    Nothing is excluded or acknowledged away, on instruction. Four of the five
    down are the DEV links that have been stale since 01 Jul 2026, so this stays
    red until DEV is reprovisioned -- which is the point of it.

    Colour is emoji, not conditional formatting: the API cannot write a
    conditional format, and those live on tables, which this line is not.

    Counts cover LRPS links only. The four click-through walkthroughs are pages,
    not launches; folding them in would inflate the green number with things the
    runner never tests.
    """
    lrps = [s for s in data['skills'] if s['section'] != 'demo']
    n = dict((k, 0) for k in SH_STATUS)
    for s in lrps:
        n[s['status']] = n.get(s['status'], 0) + 1
    measured = sum(1 for s in lrps if s.get('statusSource') == 'measured')
    when = max([s.get('statusCheckedAt') or '' for s in lrps] or [''])
    down = [s for s in lrps if s['status'] == 'broken']

    if down:
        verdict = ('%s <b>%d LINK%s DOWN</b>'
                   % (SH_DOT['broken'], len(down), '' if len(down) == 1 else 'S'))
        who = '; '.join('%s %s %s' % (ENV_SHORT.get(s['section'], s['section']),
                                      s['id'], esc(s['name']))
                        for s in down)
        detail = ' &nbsp; %s' % who
    else:
        verdict = '%s <b>ALL %d LINKS UP</b>' % (SH_DOT['active'], len(lrps))
        detail = ''

    tail = ('%d %s &nbsp;&middot;&nbsp; %d %s &nbsp;&middot;&nbsp; %d measured by the '
            'nightly runner%s, %d hand-entered'
            % (n['active'], SH_STATUS['active'], n['unverified'], SH_STATUS['unverified'],
               measured, (' as of ' + esc(when[:16].replace('T', ' '))) if when else '',
               len(lrps) - measured))

    # ONE paragraph. Each <p> becomes its own page element, and a two-element
    # roll-up cannot be updated in place: `set` replaces the first with both and
    # strands the old second below it as a duplicate.
    return '<p>%s%s &nbsp;&mdash;&nbsp; <i>%s</i></p>' % (verdict, detail, tail)


def superhuman_body(blocks):
    """The whole developer page: per-environment config, then its link table.

    The page was 93 hand-maintained bullets, two per link -- one for the direct
    launch URL and one for the LRPS URL underneath it. That shape cannot carry a
    status column at all, which is why the developer view had no status.

    The confidential fields stay here and only here. Client IDs, the OIDC and
    LTI endpoints and the internal hostnames never reach the public render;
    assert_clean() enforces that on the other side.
    """
    out = []
    for env in ENV_ORDER:
        blk = blocks.get(env)
        if not blk:
            continue
        out.append('<h2>%s</h2>' % esc(ENV_TITLE[env]))
        meta = blk.get('meta') or {}
        bullets = []
        for key, human in (('clientId', 'Client ID'),
                           ('oidcLoginUrl', 'OIDC Login Initiation URL'),
                           ('ltiLaunchUri', 'LTI Launch / Redirect URI')):
            if meta.get(key):
                val = meta[key]
                shown = (esc(val) if key == 'clientId'
                         else '<a href="%s">%s</a>' % (esc(val), esc(val)))
                bullets.append('<li>%s: %s</li>' % (esc(human), shown))
        if meta.get('note'):
            bullets.append('<li>%s</li>' % esc(meta['note']))
        if bullets:
            out.append('<ul>%s</ul>' % ''.join(bullets))
        out.append(blk['table'])
    return '\n'.join(out) + '\n'


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true',
                    help='render and diff, write nothing')
    ap.add_argument('--write', action='store_true',
                    help='apply the render to index.html')
    ap.add_argument('--status', action='store_true',
                    help='merge sentry verdicts before rendering')
    ap.add_argument('--superhuman', action='store_true',
                    help='print the Superhuman body instead')
    ap.add_argument('--out', metavar='FILE',
                    help='with --superhuman, write the page body to FILE')
    ap.add_argument('--publish', action='store_true',
                    help='with --superhuman, write it to the LIVE page')
    args = ap.parse_args()
    if not any([args.check, args.write, args.superhuman]):
        ap.error('pass --check, --write or --superhuman')

    data = load(PUBLIC_DATA, 'the public data file')
    private = load(PRIVATE_DATA, 'the private overlay')

    measured = {}
    if args.status:
        changed, measured = merge_status(data, private)
        print('status: %d link(s) measured by the runner, %d changed'
              % (len(measured), changed))

    if args.superhuman:
        blocks = render_superhuman(data, private, measured)
        body = superhuman_body(blocks)
        # NEVER default this inside REPO. The rendered developer body carries
        # Client IDs and internal hostnames, and this repo is public -- one
        # `git add -A` would commit them. It goes to the system temp dir, and
        # .gitignore names it too in case someone passes --out by hand.
        out = args.out or os.path.join(tempfile.gettempdir(),
                                       'skillproof-sh-body.html')
        io.open(out, 'w', encoding='utf-8', newline='\n').write(body)
        print('rendered %d bytes -> %s' % (len(body), out))
        for env in ENV_ORDER:
            if env in blocks:
                print('  %-12s %2d rows' % (ENV_TITLE[env], blocks[env]['count']))
        if args.publish:
            cfg = sh_target(private)
            return publish_superhuman(out, cfg['doc'], cfg['page'])
        print('not published (pass --publish)')
        return 0

    current = io.open(INDEX, encoding='utf-8', newline='').read()
    tbody = render_tbody(data)
    assert_clean(tbody)
    # index.html is CRLF throughout (1278/1278 lines). The templates above are
    # written with plain \n for legibility, so the newline style is applied here,
    # taken from the file itself rather than hardcoded. Without this every single
    # line reads as changed and the diff is useless for review.
    if '\r\n' in current:
        tbody = tbody.replace('\r\n', '\n').replace('\n', '\r\n')
    rendered = splice(current, tbody)

    if rendered == current:
        print('index.html: no change (round-trip is byte-exact)')
    else:
        diff = list(difflib.unified_diff(
            current.splitlines(True), rendered.splitlines(True),
            'index.html (current)', 'index.html (rendered)', n=1))
        sys.stdout.write(''.join(diff[:400]))
        print('\n%d diff line(s)%s'
              % (len(diff), '' if len(diff) <= 400 else ' -- truncated'))

    if args.write:
        if rendered == current:
            print('nothing to write')
        else:
            io.open(INDEX, 'w', encoding='utf-8', newline='').write(rendered)
            print('wrote index.html')
        if args.status:
            json.dump(data, io.open(PUBLIC_DATA, 'w', encoding='utf-8',
                                    newline='\n'), indent=2, ensure_ascii=False)
            print('wrote skills.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
