## Summary
   From 9th to 13th June, I mainly did these tasks; I set up development tools and created the repository with its specific structure; Learn git branch(create, delete, switch) and pull requests in Github; Build a python command line utility/script to deal with command form users; Learn how to write project documentation.

## Deliverables Completed

   - Repository setup
   - Git workflow
   - Python utility
   - Documentation
   - Pull requests

## Technical Skills Practiced

  - Git
  - Python
  - argparse
  - logging
  - Markdown
  - Claude Code

## Problems Encountered
   
   1. The git disabled the username--password authentication in August 2021, so I initially failed to push the changes of the directory to the repository in Github.

   2. Some empty folders (config., script, tests) can not be committed after the command: "git commit -m "Initialize student robotics training repository"

   3. did not know switch between branches

   4. did not know how to display all branches

   5. In page 22, I didn't know the solutions to the question: Can the student explain what `if __name__ == "__main__"` means?

   6. when created file "system_info.py", I didn't create in the folder: "scripts"

   7. On 13th June, I was not sure whether I should create a new branch or not.

## Lessons Learned
  
   * Environment Setup
   * Install and verify tools in WSL
   * Student Robotic Training: basic structure of the directory: student-robotics-training
   * Dev environment Setup
   * Daily Report
   run "git status" constantly, it tells me what git sees(what changed in files)
   * a commit is a saved checkpoint
   * Branch: A branch lets you work on a change without breaking `main`
   * Why use branches?
         •	Main stays clean.
         •	Work can be reviewed.
         •	Mistakes are isolated.
         •	Multiple features can happen independently.
   * Pull Request(PR)
        A pull request, or PR, is a request to merge a branch into the main project.
           A PR should answer:
             1. What changed?
             2. Why was it changed?
             3. How was it tested?
             4. What should the reviewer look at?
   * Python: 'if __name__ == "__main__"'

   Argumentparser object, Argumentparser(xxx,xxx,...), add_argument(...) and parse_args(...) methods
   
   * Why logging?
       •	It separates normal output from debug information.
       •	It can include timestamps.
       •	It can be filtered by level.
       •	It can later be written to files.
   * `pathlib` is the modern way to work with file paths
       project_root = Path(__file__).resolve().parents[1]

   * platform module
   
   * https://docs.python.org/ to look up various modules/libraries for different python versions

   * what contents of documentation in different files

   * in "setup.md", add instructions for all python dependencies' installation

## What I Would Improve
  1. familiarity to use commands/instructions in WSL

  2. Python: use functions/methods in (argparse, logging, pathlin, platform) modules

## Plan for Week 2

Prepare for ROS 2.