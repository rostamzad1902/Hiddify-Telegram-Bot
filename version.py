import argparse

# Define the version number
__version__ = "5.1.0"


def version():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=f"{__version__}")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    version()
