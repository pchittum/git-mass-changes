import subprocess, os, sys
from pathlib import Path

working_branch = sys.argv[1]

not_staged_txt = "Changes not staged for commit"
p_repos = Path('./repos')
folder_list = []

all_folders = [folder for folder in p_repos.iterdir() if folder.is_dir()]

for folder in all_folders:
    #folder_list.append(folder.name)
    os.chdir(folder)

    status_output = subprocess.run(["git", "status"], stdout=subprocess.PIPE, text=True)

    stdout_str = "".join(status_output.stdout)

    if not_staged_txt in stdout_str:

        # subprocess.run(["git", "checkout", "-b", working_branch])
        subprocess.run(["git", "add", "README.md"])

        #lazy here...I'm just gonna run this, and if it fails, it fails.         
        subprocess.run(["git", "add", "README.ja.md"])

        subprocess.run(["git", "commit", "-m", "'fixed registration url'"])

        output = subprocess.run(["git", "status"], stdout=subprocess.PIPE, text=True)
        print(output.stdout)

        push = input(f'Push changes for {os.getcwd()} (y/n):')
        
        if push == "y":
            subprocess.run(["git", "push", "origin", working_branch])
            print(f'pushed branch {working_branch} to repo {folder.name}')
        else: 
            print("skipped this repo")

    else:
        print('no changes detected by git')


    os.chdir('../..')
    


# os.chdir(p_repos.name)


print(folder_list)

"""
Steps to take: 
X. pass parameter for branch name
X. change working director to repos
X. get the children names into an array
4. for each item in the array
    5. git status to check for changes
    6. checkout new branch based on passed in param
    7. add and commit README.md and README.jp.md
    8. push working branch

Might be good to store results somewhere so we can go back over them. 
"""


# p_repos = Path('./repos')

# os.chdir(p_repos.name)

# # print(p_repos.is_dir())
# # print(p_repos.name)
# # print(p_repos.root)
# print(p_repos.cwd())

# with open('../repourls.txt', 'r') as file: 
#     url_list = file.readlines()


# url_list = [line.strip() for line in url_list ]

# for this_url in url_list:
#     subprocess.run(["git", "clone", this_url])

