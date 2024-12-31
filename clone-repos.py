import subprocess, os
from pathlib import Path

p_repos = Path('./repos')

os.chdir(p_repos.name)

print(p_repos.cwd())

with open('../repourls.txt', 'r') as file:
    url_list = file.readlines()

url_list = [line.strip() for line in url_list]

for this_url in url_list:
    subprocess.run(["git", "clone", this_url])
