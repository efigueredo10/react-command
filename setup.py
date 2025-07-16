from setuptools import setup, find_packages

setup(
    name="react_command",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "rc = react_command.main:main",  # comando = arquivo:função
        ],
    },
)