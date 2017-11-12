from distutils.core import setup

setup (
    name = "pycog3",
    version = "0.1.28",
    scripts = ["bin/cog-command"],
    description = "Command library for the Cog ChatOps platform for Python3",
    author = "Kevin Smith",
    author_email = "kevin@operable.io",
    url = "https://github.com/cog-bundles/pycog3",
    download_url = "https://github.com/cog-bundles/pycog3/tarball/0.1.28",
    packages = ["cog"],
    keywords = ["bot", "devops", "chatops", "automation"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License"
    ]
)
