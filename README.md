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

Instructions on day2 Hands-On Task

 Create a branch:
 git checkout -b feature/hello-robot
 Create `scripts/hello_robot.py`:
 def main():
     print("Hello, Berkeley Humanoid Lite software project!")

 if __name__ == "__main__":
     main()
 Run it:
 python scripts/hello_robot.py
 Update `README.md` with instructions:
 ## Running the Hello Robot Script

 python scripts/hello_robot.py