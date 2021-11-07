import os
from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def setup_package():
    setup(
        name = "My App",
        version = "0.1.0"
    )


if __name__ == "__main__":
    setup_package()
