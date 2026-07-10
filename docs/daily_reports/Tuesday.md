| Time | Activity |
| 13:00-15:00|run "git status" in WSL before and after changing "README.md"|git


WSL instructions:
"git remote show origin", "git remote -v", "git config --get remote.origin.url";
If it says "No such remote" or git remote -v shows nothing, your repo doesn't have a remote configured yet — you'd add one with:
git remote add origin https://github.com/user(e.g. wangdaoz)/repo.git