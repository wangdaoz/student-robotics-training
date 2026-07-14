•	Operating system used
     windows subsytem for Linuex
•	Python version
     3.12.3
•	Commands
      ## Git
         Check:
           git --version
           Expected result: Git prints a version number.
          
          Configure Git:
           "ssh-keygen -t ed25519 -C "your_email@example com"
           "ssh-add ~/.ssh/id_ed25519"
           "cat ~/.ssh/id_ed25519.pub"
           add the public key to Github
          Test
            ssh -T git@github.com
      
       ## Python
          Check:
             python3 --version
          Expected result: Python 3.10 or newer is preferred.

          Install:
             sudo apt install python3 python3-pip python3-venv -y

          verify installation:
            python3 --version
            pip3 --version
          
          Optional: make python point to python3
              sudo apt install python-is-python3 -y

          Optional: install a specific Python version
            sudo apt install software-properties-common -y
            sudo add-apt-repository ppa:deadsnakes/ppa -y
            sudo apt update
            sudo apt install python3.14 python3.14-venv -y

      ## Install Python Dependencies
        sudo apt update
        sudo apt install python3-venv python3-pip
        python3 -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
         
•	   Expected output
          a new folder "student-robotics-training/.venv" is created
     
      ## Claude Code
          curl -fsSL https://claude.ai/install.sh | bash
          claude
          exit

•	Common errors
         ensurepip error: venv module is not fully installed

•	Fixes attempted
       before inputting "python3 -m venv .venv" input the following instruction:
        sudo apt update
        sudo apt install python3-venv python3-pip