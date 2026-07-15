## Today's Goal

Set up development tools and create the first repository.

## Completed

- Installed/verified Git
- Installed/verified Python
- Installed/verified VS Code
- Created GitHub repository
- Made first commit

## Problems Encountered
   1. The git disabled the username--password authentication in August 2021, so I initially failed to push the changes of the directory to the repository in Github. Then, I asked claude for help it reminds me two solutions; Generating a personal token in Github ,copying it and paste it in the iterm "password"; Generating a ssh key my home directory in WSL.
   
   2. Some empty folders (config., script, tests) can not be committed after the command: "git commit -m "Initialize student robotics training repository"

## How I Solved Them
   For problem 1, I inputted relevant commands ("ssh-keygen -t ed25519 -C "your_email@example.com", "ssh-add ~/.ssh/id_ed25519", "cat ~/.ssh/id_ed25519.pub") to set private and public ssh keys. Then, add the public key to Github. Finally, inputted command: "ssh -T git@github.com" to test the connection. After setting ssh keys, I input the command "git push" again to update the repository in Github.
   
   For problem 2, 
   First, I input "git log --stat" to check which files in my last commit. The result is that all empty folders were never committed in last commit, whcih confirms that those folders weren't included in the last commit. Then, I add a ".gitkeep" file in each of those folders, committed them and pushed them again. 

## Claude Code Usage

   Claude helped me analyze those problems I met in the work and guided me to found actual causes. Futhermore, teached me to solved problems.

## What I Learned

  Write at least 5 bullet points.
 * Environment Setup
 * Install and verify tools in WSL
 * Student Robotic Training: basic structure of the directory: student-robotics-training
 * Dev environment Setup
 * Daily Report

## Plan for Tomorrow
 Learn Git branches and pull requests.
