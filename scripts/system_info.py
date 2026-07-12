"""System information utility for Week 1 engineering onboarding."""
import argparse
import logging
import platform


logger = logging.getLogger(__name__) # create a logger object after the current module(__name__ is evaluation to the module's name)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Print basic system information"
    )
    parser.add_argument("--name", required=True, help="Name of the user")
    return parser.parse_args()

def collect_system_info():
    return {
        "python_version": platform.python_version(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "machine": platform.machine(),
    }

def main():
    logging.basicConfig(level=logging.INFO)
    args = parse_args()

    logger.info("Collecting system information")
    info = collect_system_info()

    print(f"Hello {args.name}")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()