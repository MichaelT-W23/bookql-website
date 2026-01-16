import os
import subprocess
from termcolor import colored as c
import sys

def run(cmd, critical=False):
    print(c(f"> {cmd}", "cyan"))
    code = os.system(cmd)
    if critical and code != 0:
        print(c("\n❌ Command failed, aborting deploy.\n", "red"))
        sys.exit(1)

process = subprocess.run('git branch --show-current', shell=True, capture_output=True, text=True)
branch = process.stdout.strip()

print('On branch ', end="")

if branch == 'main':
    print(c(branch, 'green'))
else:
    print(c(branch, 'red'))
    print('Switch to main branch before deploying.')
    sys.exit(1)

commit_msg = input("Enter your commit message: ")

# Commit source
run('git add .', critical=True)
run(f'git commit -m "{commit_msg}" || true')
run('git push origin main', critical=True)

# Clean old build
run('rm -rf dist', critical=True)

# Build
run('npm run build', critical=True)

# Verify output
if not os.path.exists('dist/assets'):
    print(c("\n❌ Build failed: dist/assets missing\n", "red"))
    sys.exit(1)

assets = os.listdir('dist/assets')
js_files = [f for f in assets if f.endswith('.js')]

if not js_files:
    print(c("\n❌ Build failed: JS bundle missing\n", "red"))
    sys.exit(1)

print(c(f"\n✔ JS bundle found: {js_files[0]}", "green"))

# SPA fallback
run('cp dist/index.html dist/404.html', critical=True)

# CNAME
run('echo "vue.bookql.com" > dist/CNAME', critical=True)

# Deploy: orphan branch method
run('git checkout --orphan temp-gh-pages', critical=True)
run('git rm -rf . --quiet || true')
run('cp -r dist/* .', critical=True)
run('git add .', critical=True)
run('git commit -m "Deploy"', critical=True)
run('git push -f origin temp-gh-pages:gh-pages', critical=True)
run('git checkout main', critical=True)
run('git branch -D temp-gh-pages', critical=True)

print(c("\n🚀 Deployment complete and verified", "green"))
