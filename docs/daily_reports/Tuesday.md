| Time | Activity |
| 13:00-15:00|run "git status" in WSL before and after changing "README.md"|
| 16:00-17:00|review knowledge in Git concepts(commit, branch, pull request); think and answer questions for mentor and student in page 22; write daily report on Tuesday; check mistakes on hand-on task|

WSL instructions:
"git remote show origin", "git remote -v", "git config --get remote.origin.url";
If it says "No such remote" or git remote -v shows nothing, your repo doesn't have a remote configured yet — you'd add one with:
git remote add origin https://github.com/user(e.g. wangdaoz)/repo.git

## Today's Goal

 Learn Git branch and pull request workflow.

## Completed
 - Created feature branch
 - Added hello robot script
 - Updated README
 - Opened pull request

## Problems Encountered
   1. did not know switch between branches
   2. did not know how to display all branches
   3. In page 22, I didn't know the solutions to the question: Can the student explain what `if __name__ == "__main__"` means?

## How I Solved Them
   Q1: I asked Claude "In WSL, how to switch between two branches?", the relevant instructions in WSL:
     *switch to an existing branch:
        "git checkout branch-name" or "git switch branch-name"
     *Create a new branch and switch to it:
         "git checkout -b new-branch-name" or "git switch -c new-branch-name"
    
    Q2: I ask Claude: "how to show all branches", it answers:
        Local branches only: "git branch"

        All branches including remote-tracking ones: "git branch -a"

        Remote branches only: "git branch -r"

        With more detail: "git branch -vv"

        Sorted by most recently used: "git branch --sort=-committerdate"

    Q3: I referred to previous material about python 3.0 or above but no relevant explaination for the question. Then I asked      Claude code, it gave detailed explaination.

    ## Claude Code Usage
      -asked "In WSL, how to switch between two branches?"
      -asked "how to show all branches"
      -asked "In python for "main" function, there is always a segment of code: "if __name__ == “__main__:" , what does it mean?
    
    ## What I Learned
       1. run "git status" constantly, it tells me what git sees(what changed in files)
       2. a commit is a saved checkpoint
       3. Branch: A branch lets you work on a change without breaking `main`
           Why use branches?
             •	Main stays clean.
             •	Work can be reviewed.
             •	Mistakes are isolated.
             •	Multiple features can happen independently.
       4. Pull Request(PR)
          A pull request, or PR, is a request to merge a branch into the main project.
             A PR should answer:
                 1. What changed?
                 2. Why was it changed?
                 3. How was it tested?
                 4. What should the reviewer look at?
       5. Python: 'if __name__ == "__main__"'

    ## Plan for Tomorrow
       Build a more serious Python utility with argparse and logging.


      