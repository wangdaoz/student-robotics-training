## Purpose
    Learn to design software system for Berkeley Humanoid Lite system
## Repository Structure
   
├── README.md↓
├── config/↓
│   └── example_config.yaml↓
├── docs/↓
│   ├── setup.md↓
│   ├── project_structure.md↓   
|   ├── changelog.md↓
│   ├── daily_reports/↓
│   │   ├── monday.md↓
│   │   ├── Tuesday.md↓
│   │   ├── wednesday.md↓
│   │   ├── thursday.md↓
│   │   └── friday.md↓
│   └── weekly_report.md↓
├── scripts/↓
│   └── system_info.py↓
    └── hello_robot.py↓
├── tests/↓
│   └── test_system_info.md↓
└── requirements.txt

## Setup
    ## Git
         Check
           <git --version>
           Expected result: Git prints a version number.
          
          Configure Git
           <ssh-keygen -t ed25519 -C "your_email@example com">
           <ssh-add ~/.ssh/id_ed25519>
           <cat ~/.ssh/id_ed25519.pub>
           add the public key to Github
          Test
            <ssh -T git@github.com>
      
    ## Python
          Check
             <python3 --version>
          Expected result: Python 3.10 or newer is preferred.

          Install
             <sudo apt install python3 python3-pip python3-venv -y>

          verify installation
            <python3 --version>
            <pip3 --version>
          
          Optional: make python point to python3
              <sudo apt install python-is-python3 -y>

          Optional: install a specific Python version
            <sudo apt install software-properties-common -y>
            <sudo add-apt-repository ppa:deadsnakes/ppa -y>
            <sudo apt update>
            <sudo apt install python3.14 python3.14-venv -y>

      ## Install Python Dependencies
        <sudo apt update>
        <sudo apt install python3-venv python3-pip>
        <python3 -m venv .venv>
        <source .venv/bin/activate>
        <pip install -r requirements.txt>
         
•	   Expected output
          a new folder "home/kevin-lianhu/.venv" is created
     
      ## Claude Code
          <curl -fsSL https://claude.ai/install.sh | bash>
          <claude>
          <exit>

•	Common errors
         ensurepip error: venv module is not fully installed

•	Fixes attempted
       before inputting "python3 -m venv .venv" input the following instruction:
        <sudo apt update>
        <sudo apt install python3-venv python3-pip>
         
•	   Expected output
          a new folder "student-robotics-training/.venv" is created
     
      ## Claude Code
          <curl -fsSL https://claude.ai/install.sh | bash>
          <claude>
          <exit>

## Running Examples
    scripts: hello_robot.py, system-info.py

## Testing
     Program exits without error
    - Output includes "Hello Student, your age is Age. Here is your system information:"
    - Output includes Python version
    - Output includes operating system
    - Output includes platform release
    - Output includes platform machine

## Current Status
   The structure of the repository is built and explained in the file: project_structure.md and README.md.
   Two scripts can be correctly ran or tested.
   Daily reports, weekly report are finished.

## Next Steps
    Prepare for ROS 2
Week1 Goals
1. A GitHub repository with a clean structure.
2. A `README.md` explaining the project.
3. A `docs/setup.md` file explaining how the environment was installed.
4. A `docs/project_structure.md` file explaining the folders.
5. A `scripts/system_info.py` Python utility.
6. A `config/example_config.yaml` configuration file.
7. A `tests/` folder with at least one simple test or manual test procedure.
8. Daily reports for Monday through Friday.
9. A weekly report.
