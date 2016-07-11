import json
from sys import stdout

class Response(object):
    def __init__(self):
        self.template_ = None
        self.content_ = None
        self.message_ = None
        self.aborted_ = False

    def abort(self):
        self.aborted_ = True

    def string(self, message):
        self.message_ = message
        return self

    def content(self, value, template=None):
        self.content_ = value
        self.template_ = template
        return self

    def send(self):
        if self.aborted_:
            self.write_("COGCMD_ACTION: abort")
        if self.template_ is not None:
            self.write_("COG_TEMPLATE: %s" % (self.template_))
        if self.content_ is not None:
            self.write_json_()
        else:
            if self.message_ is not None:
                self.write_string_()

    def write_string_(self):
        self.write_(json.dumps(self.message_))

    def write_json_(self):
        encoded = json.dumps(self.content_)
        self.write_("\n".join(["JSON", encoded]))

    def write_(self, message):
        print(message)
        stdout.flush()

    def debug(self, message):
        self.log_("debug", message)

    def info(self, message):
        self.log_("info", message)

    def warn(self, message):
        self.log_("warn", message)

    def error(self, message):
        self.log_("error", message)

    def log_(self, level, message):
        print("COGCMD_%s: %s" % (level.upper(), message))
