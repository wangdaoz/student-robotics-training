•	Operating system used
     windows subsytem for Linuex
•	Python version
     3.12.3
•	Commands
      ## Install Python Dependencies
        sudo apt update
        sudo apt install python3-venv python3-pip
        python3 -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
         
•	Expected output
        a new folder "student-robotics-training/.venv" is created

•	Common errors
         ensurepip error: venv module is not fully installed

•	Fixes attempted
       before inputting "python3 -m venv .venv" input the following instruction:
        sudo apt update
        sudo apt install python3-venv python3-pip