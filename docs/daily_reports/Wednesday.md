## Today's Goal

Build a Python command-line utility using argparse and logging.

## Completed

- Created system_info.py
- Added config example
- Added manual tests
- Updated README
- Opened PR

## Problems Encountered

 when created file "system_info.py", I didn't create in the folder: "scripts"

## How I Solved Them

   After I realiized my error, I created same file in the folder "scripts" and deleted the previous one.

## Claude Code Usage

  What prompts did you use? What did you verify?
  In the modules: argparse, logging, pathlib, I didn't understand the roles of those functions. I figure out the roles of them and what arguments could be passed.

## What I Learned

   1. Argumentparser object, Argumentparser(xxx,xxx,...), add_argument(...) and parse_args(...) methods
   
   2. Why logging?
       •	It separates normal output from debug information.
       •	It can include timestamps.
       •	It can be filtered by level.
       •	It can later be written to files.
   3. `pathlib` is the modern way to work with file paths
       project_root = Path(__file__).resolve().parents[1]

   4. platform module
   
   5. https://docs.python.org/ to look up various modules/libraries for different python versions

## Plan for Tomorrow

Improve project documentation.





Python Concepts:
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

  3. pathlib
      `pathlib` is the modern way to work with file paths.
      E.g. 
         from pathlib import Path
         """
         from pathlib import Path — imports the modern, object-oriented path-handling class (preferred over the older os.path string-based functions).
         Path(__file__)
          __file__ is a built-in variable that holds the path to the current .py file (as a string, possibly relative).
         Wrapping it in Path(...) turns it into a Path object so you can use path operations on it.
         .resolve()
          Converts the path to an absolute path and resolves any symlinks or ../. segments. So no matter whether the script was run from a different working directory, this gives a clean, fully-qualified path.
         .parents[1]
           .parents is a sequence of ancestor directories, indexed from the immediate parent outward.
           .parents[0] = the directory containing the file
           .parents[1] = that directory's parent (i.e., one level up)
            So this walks up two levels from the file itself: once to its containing folder, once more to that folder's parent — which is being treated as the project root.
             Example: if __file__ is /home/user/project/src/script.py, then:

              .parents[0] → /home/user/project/src
              .parents[1] → /home/user/project
         """
         project_root = Path(__file__).resolve().parents[1]
         config_path = project_root / "config" / "example_config.yaml"

         print(config_path)
      Robotics projects have many files:
      •	config files
      •	logs
      •	robot descriptions
      •	calibration files
      •	datasets
      •	simulation assets
