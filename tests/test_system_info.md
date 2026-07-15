## Test 1: Basic Run

Command:

python3 scripts/system_info.py --name Student --age  20

Expected:

- Program exits without error
- Output includes "Hello Student, your age is Age. Here is your system information:"
- Output includes Python version
- Output includes operating system
- Output includes platform release
- Output includes platform machine

## Test 2: Missing Name

Command:

python3 scripts/system_info.py

Expected:

- argparse shows an error about missing --name
Manual tests are acceptable at this stage. Later weeks can introduce automated tests.