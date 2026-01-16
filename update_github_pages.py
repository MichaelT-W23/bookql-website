import os
import subprocess
from termcolor import colored as c

def run(cmd):
    print(c(f"> {cmd}", "cyan"))
    os.system(cmd)

process = subprocess.run('git branch --show-current', shell=True, capture_output=True, text=True)
branch = process.stdout.strip()

print('On branch ', end="")

if branch == 'main':
    print(c(branch, 'green'))
else:
    print(c(branch, 'red'))
    print('Move changes to the main branch, then switch to the main branch.')
    exit(0)

commit_msg = input("Enter your commit message: ")

# Commit source
run('git add .')
run(f'git commit -m "{commit_msg}" || true')
run('git push origin main')

# Clean old build
run('rm -rf dist')

# Build
run('npm run build')

# Verify build output
run('ls dist/assets')

# SPA fallback
run('cp dist/index.html dist/404.html')

# CNAME for GitHub Pages
run('echo "vue.bookql.com" > dist/CNAME')

# Deploy: hard replace gh-pages with dist contents
run('git checkout --orphan temp-gh-pages')
run('git rm -rf . --quiet || true')
run('rm -rf .gitignore')
run('cp -r dist/* .')
run('git add .')
run('git commit -m "Deploy"')
run('git push -f origin temp-gh-pages:gh-pages')
run('git checkout main')
run('git branch -D temp-gh-pages')

print(c("\nDeployment complete 🚀", "green"))
