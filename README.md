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

7-11/12:
 1. argparse:
   `argparse` lets a Python script accept command-line options.
    E.g. 
        import argparse

        parser = argparse.ArgumentParser() # create an ArgumentParser object with relevant parameters
        parser.add_argument("--name", required=True) # how a single command line element be parsed
        """
        Reads the actual arguments from sys.argv (what the user typed on the command line), validates them against the rules defined above, and returns a Namespace object. You'd then access the value with args.name.
        """
        args = parser.parse_args() #

        """
         f — the prefix before the opening quote marks this as an f-string. It tells Python to scan the string for {...} placeholders and evaluate them as expressions.
         "Hello, ..." — the literal text portion, inserted as-is.
        {args.name} — a placeholder containing a Python expression. At runtime, Python evaluates args.name (accessing the name   attribute on the args object returned by parse_args()) and substitutes its string representation directly into the string.
        """
        print(f"Hello {args.name}")
  2. logging
      Beginners use `print()` for everything. Engineers use `logging`
      Why logging?
        •	It separates normal output from debug information.
        •	It can include timestamps.
        •	It can be filtered by level.
        •	It can later be written to files.
     E.g.
         import logging

         logging.basicConfig(level=logging.INFO)
         """
            Configures the root logger with default settings — this only has an effect the first time it's called in a program (subsequent calls are no-ops unless you pass force=True).

            basicConfig() is designed to configure the root logger's handlers only once. The function checks internally: "does the root logger already have handlers attached?"

             If no handlers exist yet → it configures them (first call, does real work).
             If handlers already exist (meaning basicConfig() was called before, or something else configured logging) → the call becomes a no-op: it just returns immediately and changes nothing, silently ignoring whatever arguments you passed (like a different level)

             if you call basicConfig(level=logging.INFO) and later call basicConfig(level=logging.DEBUG) elsewhere in your code expecting to change the level, the second call won't work — it's a no-op because the root logger was already configured. This is a common gotcha. To force reconfiguration, you'd need:
                logging.basicConfig(level=logging.DEBUG, force=True)
                The force=True argument (Python 3.8+) removes existing handlers first, so the call isn't skipped.
            level=logging.INFO sets the minimum severity of messages that will actually get output. Logging levels, from lowest to highest severity:
               DEBUG (10)
               INFO (20)
               WARNING (30)
               ERROR (40)
               CRITICAL (50)
               Setting level=logging.INFO means messages at INFO and above are shown; DEBUG messages are suppressed.
               Without any other arguments, this also implicitly sets up a default handler that prints to stderr with a basic format like INFO:root:message
         """
         logger = logging.getLogger(__name__)
         """
          logger = logging.getLogger(__name__)
             Creates (or retrieves) a logger object named after the current module (__name__ evaluates to the module's name, e.g. "myapp.utils", or "__main__" if run directly).

             Using __name__ is the standard convention because it creates a hierarchical logger namespace matching your package structure — so log messages show which module they came from, and you can configure logging differently per-module if needed (e.g., silence a noisy third-party module while keeping your own at DEBUG).
         """

         logger.info("Starting script")
         logger.warning("This is a warning")
         logger.error("This is an error")

## Purpose

## Repository Structure

## Setup

## Running Examples

## Testing

## Current Status

## Next Steps