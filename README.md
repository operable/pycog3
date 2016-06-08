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
directory layout:

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
## Examples

See the [cog-bundles/statuspage](https://github.com/cog-bundles/statuspage) repository for an example of this library in action.

## Installation

Add this line to your application's setup.py or requirements.txt:

```
pycog3>=0.1.25
```

## TODO

- Add [Cog service](http://docs.operable.io/docs/services) support
- Add transparent accumulation support a la [cog-bundles/cog-rb](https://github.com/cog-bundles/cog-rb)
