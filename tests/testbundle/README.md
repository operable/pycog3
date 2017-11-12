testbundle 
=======================================

# Overview

This is a dummy cog bundle used to test pycog3 python module. 
 

# Configuring

There is one dynamic configuration variable `dyn_config_var1` which should be set in the environmental variables:

# Executing

Should be executed after `pycog3` is installed. 
If running outside cog's environment, at the root of the project `/`, do:

```bash
$ export PYTHONPATH=tests/testbundle
$ export COG_BUNDLE="testbundle"
$ export COG_COMMAND="commanda"
$ export dyn_config_var1="foo"
$ cog-command
COG_TEMPLATE: template
JSON
"0a"
```



