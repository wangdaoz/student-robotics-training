## Test 1: Basic Run

Command:

python scripts/system_info.py --name Student

Expected:

- Program exits without error
- Output includes "Hello Student"
- Output includes Python version
- Output includes operating system

## Test 2: Missing Name

Command:

python scripts/system_info.py

Expected:

- argparse shows an error about missing --name
Manual tests are acceptable at this stage. Later weeks can introduce automated tests.