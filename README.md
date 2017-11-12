[![Build Status](https://travis-ci.org/operable/pycog3.svg?branch=master)](https://travis-ci.org/operable/pycog3)

# pycog3

Simple, opinionated library for building Cog commands in Python3.

## Usage

pycog3 combines information available in the Cog runtime environment
with assumptions about Python project structure to simplify command
development.

pycog3 includes a driver executable, [bin/cog-command](https://github.com/cog-bundles/pycog3/blob/master/bin/cog-command), which dynamically
imports, instantiates, and runs Python command code based on the
values of `$COG_BUNDLE` and `$COG_COMMAND`.

`cog-command`'s magic requires that Python projects follow a strict
directory layout (basic):

```
<bundle_name>
  |
  |-- <bundle_name>
       |-- __init__.py
       |-- commands
           |
           |-- __init__.py
           |-- <command1>.py
           |-- <command2>.py

```

pycog3 also supports more advanced, multi-level structure when using the `-` field separator in the command name. 
For example, defining:
 * `commands\commanda.py` - maps to `!commanda`
 * `commands\level1\commandb.py` - maps to `!level1-commandb`
 * `commands\level1\level2a\commandc.py` - maps to `!level1-level2a-commandb`
 * `commands\level1\level2b\leveln\commandz.py` - maps to `!level1-level2b-leveln-commandz`
 

```
<bundle_directory>
  |
  |-- <bundle_name>
       |-- __init__.py
       |-- commands
           |
           |-- __init__.py
           |-- <commanda>.py
           |-- <commandb>.py
           .
           .
           |-- <commandz>.py
           |
           |-- <level1>
                |
                |-- __init__.py
                |-- <commanda>.py
                |-- <commandb>.py
                .
                .
                |-- <commandz>.py
                |
                |-- <level2a>
                |    |
                |    |-- <commanda>.py
                |    |-- <commandb>.py
                |    |-- <commandc>.py
                |    .
                |    .
                |    |-- <commandz>.py
                |
                |-- <level2b>
                     |
                     |-- __init__.py
                     |-- <...>
                         |
                         |-- __init__.py
                         | -- <leveln>
                              |
                              |-- __init__.py
                              |-- <commanda>.py
                              |-- <commandb>.py
                              .
                              .
                              |-- <commandz>.py

```

The only requirement is a class with the same name of the filename should exist (first letter capital).

## Examples

See the [cog-bundles/statuspage](https://github.com/cog-bundles/statuspage) repository for an example of this library in action.

If you're interested in the multi-level usage, check the cog-bundle [pi-bundle](https://github.com/pan-net-security/pi-bundle) or the test bundle in `test/`.

## Installation

Add this line to your application's setup.py or requirements.txt:

```
pycog3>=0.1.28
```

## TODO

- Add [Cog service](http://docs.operable.io/docs/services) support
- Add transparent accumulation support a la [cog-bundles/cog-rb](https://github.com/cog-bundles/cog-rb)
