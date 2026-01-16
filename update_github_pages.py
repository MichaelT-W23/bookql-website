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
    print('git stash')
    print('git checkout main')
    print('git pull origin main')
    print(f'git merge {branch}')
    print('git stash apply')
    print('git push origin main')
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

# Deploy using split + force
run('git subtree split --prefix dist -b temp-gh-pages')
run('git push -f origin temp-gh-pages:gh-pages')
run('git branch -D temp-gh-pages')

print(c("\nDeployment complete 🚀", "green"))
