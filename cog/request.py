import json
import os
import re
import string
import sys

class Request(object):
    def __init__(self, getenv=os.getenv):
        self.getenv_ = getenv
        self.populate_options_()
        self.populate_args_()
        if sys.stdin.isatty() == False:
            self.input = json.load(sys.stdin)
        else:
            self.input = {}
        self.service_key = self.getenv_("COG_SERVICE_TOKEN")
        self.step = self.getenv_("COG_INVOCATION_STEP", None)

    def populate_options_(self):
        names = self.getenv_("COG_OPTS")
        if names is None:
            self.options = None
            return
        names = re.sub(r'(^"|"$)', r'', names)
        names = names.split(",")
        self.options = {}
        for name in names:
            self.options[name] = self.getenv_(option_name_to_var(name))

    def populate_args_(self):
        arg_count = int(self.getenv_("COG_ARGC", "0"))
        if arg_count == 0:
            self.args = None
            return
        self.args = []
        for i in range(arg_count):
            self.args.append(self.getenv_(arg_index_to_var(i)))

    def get_optional_option(self, name):
        if name in self.options.keys():
            return self.options[name]
        return None

def option_name_to_var(name):
    return "COG_OPT_%s" % (name.upper())

def arg_index_to_var(index):
    return "COG_ARGV_" + str(index)

