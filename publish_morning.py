# -*- coding: utf-8 -*-
"""Morning publish: one command from last night's measurements to both link surfaces.

08 OCT 2026 (Brady). The nightly runner (sentry) never writes to this repo or to
Superhuman, on purpose: nothing should change a public page at 02:30 with nobody
watching. This script is the human step, collapsed into two commands with a stop
between them.

    publish_morning.py              REVIEW. Merges last night's verdicts into
                                    skills.json, rebuilds index.html (local files
                                    only), dry-runs the Superhuman sync, lists any
                                    Live PROD Skill with no published link, then
                                    STOPS. Nothing leaves this machine.
    publish_morning.py --commit     PUBLISH what was reviewed: refuses if either
                                    file changed since the review, then applies the
                                    Superhuman sync, commits and pushes.

Run it with the Superhuman writer's venv python, which the sync needs:
    C:\\dev\\repos\\superhuman-docs-writer\\.venv\\Scripts\\python.exe publish_morning.py
"""
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.abspath(__file__))
FILES = ['skills.json', 'index.html']
MARKER = os.path.join(tempfile.gettempdir(), 'skillproof-morning-review.json')
UNLINKED = os.environ.get(
    'SENTRY_UNLINKED',
    r'C:\dev\scratch\skillproof-qa-tools\sentry\store\inventory\prod\unlinked.json')


def run(args, check=True):
    p = subprocess.run(args, cwd=REPO, capture_output=True, text=True,
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    if check and p.returncode != 0:
        sys.stdout.write(p.stdout + p.stderr)
        sys.exit('STOPPED: %s exited %d' % (' '.join(args[:3]), p.returncode))
    return p


def digest():
    h = {}
    for f in FILES:
        h[f] = hashlib.sha256(io.open(os.path.join(REPO, f), 'rb').read()).hexdigest()
    return h


def changed_files():
    out = run(['git', 'status', '--porcelain', '--'] + FILES).stdout
    return [l[3:].strip() for l in out.splitlines() if l.strip()]


def status_changes():
    """Rows whose status differs from the committed skills.json."""
    old = json.loads(run(['git', 'show', 'HEAD:skills.json']).stdout)
    new = json.load(io.open(os.path.join(REPO, 'skills.json'), encoding='utf-8'))
    before = dict((s['id'], s.get('status')) for s in old.get('skills', []))
    rows = []
    for s in new.get('skills', []):
        if s['id'] in before and before[s['id']] != s.get('status'):
            rows.append('%s  %s: %s -> %s' % (s['id'], s['name'], before[s['id']], s.get('status')))
    return rows


def unlinked_report():
    try:
        u = json.load(io.open(UNLINKED, encoding='utf-8'))
    except (IOError, OSError, ValueError):
        return ['(no unlinked list yet; the nightly PROD check writes it)']
    if not u.get('unlinked'):
        return ['every Live PROD Skill (%s) has a published link' % u.get('liveSkills')]
    out = ['%d Live PROD Skill(s) with NO published link (draft rows in %s):' % (len(u['unlinked']), UNLINKED)]
    for x in u['unlinked']:
        out.append('  %s  (%s, %s)  slug %s' % (x['name'], x.get('school'), x.get('courseCode'), x.get('slug')))
    out.append('  Each needs its LRPS id from the provisioning reply; add it to skills.json by hand.')
    return out


def review():
    if changed_files():
        sys.exit('STOPPED: skills.json or index.html already has uncommitted changes. '
                 'Commit or discard them first, so this review shows only last night.')
    py = sys.executable
    p = run([py, 'build_links.py', '--write', '--status'])
    print('\n'.join(l for l in p.stdout.splitlines() if l.startswith(('status:', 'wrote', 'nothing'))))
    sh = run([py, 'sync_superhuman.py'], check=False)
    print('\n--- Superhuman sync (dry run) ---')
    sys.stdout.write(sh.stdout[-3000:])
    if sh.returncode != 0:
        sys.stdout.write(sh.stderr[-1500:])
        print('Superhuman dry run FAILED (exit %d); --commit will refuse.' % sh.returncode)
    print('\n--- status changes vs the last commit ---')
    rows = status_changes()
    print('\n'.join(rows) if rows else '(none)')
    print('\n--- files changed ---')
    print(run(['git', 'diff', '--stat', '--'] + FILES).stdout or '(none)')
    print('--- Live PROD Skills without a link ---')
    print('\n'.join(unlinked_report()))
    json.dump({'at': datetime.now(timezone.utc).isoformat(), 'digest': digest(), 'superhumanOk': sh.returncode == 0,
               'changed': changed_files()}, io.open(MARKER, 'w', encoding='utf-8'))
    print('\nSTOPPED for review. Nothing was committed, pushed or written to Superhuman.')
    print('Full diff:  git -C "%s" diff -- skills.json index.html' % REPO)
    print('Publish:    %s publish_morning.py --commit' % py)
    print('Discard:    git -C "%s" checkout -- skills.json index.html' % REPO)


def commit():
    try:
        m = json.load(io.open(MARKER, encoding='utf-8'))
    except (IOError, OSError, ValueError):
        sys.exit('STOPPED: no review on record. Run publish_morning.py (no flags) first.')
    if m['digest'] != digest():
        sys.exit('STOPPED: skills.json or index.html changed since the review. Run the review again.')
    if not m.get('superhumanOk'):
        sys.exit('STOPPED: the Superhuman dry run failed at review time. Fix it and review again.')
    files = changed_files()
    py = sys.executable
    sh = run([py, 'sync_superhuman.py', '--commit'])
    print('\n'.join(sh.stdout.splitlines()[-6:]))
    if not files:
        print('Repo: nothing to commit (statuses unchanged).')
    else:
        day = datetime.now().strftime('%d %b %Y').upper()
        run(['git', 'add', '--'] + files)
        run(['git', 'commit', '-m', 'Link statuses measured by the nightly run (%s)\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>' % day])
        print(run(['git', 'log', '--oneline', '-1']).stdout.strip())
        push = run(['git', 'push'], check=False)
        print('pushed' if push.returncode == 0 else 'PUSH FAILED: ' + push.stderr.strip()[-400:])
    os.remove(MARKER)


if __name__ == '__main__':
    commit() if '--commit' in sys.argv[1:] else review()
