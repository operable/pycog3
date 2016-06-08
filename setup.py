from setuptools import setup, find_packages

setup (
    name = "pycog3",
    version = "0.1.25",
    scripts = ["bin/cog-command"],
    description = "Command library for the Cog ChatOps platform for Python3",
    author = "Kevin Smith",
    author_email = "kevin@operable.io",
    url = "http://operable.io",
    packages = find_packages(),
    install_requires = ["requests>=2.10", "PyYAML>=3.11"],
    keywords = ["bot", "devops", "chatops", "automation"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License"
    ]
)
