import json
from sys import stdout

class Response(object):
    def __init__(self):
        self.template_ = None
        self.content_ = None
        self.message_ = None
        self.log_msgs_ = []

    def string(self, message):
        self.message_ = message
        return self

    def content(self, value, template=None):
        self.content_ = value
        self.template_ = template
        return self

    def send(self):
        try:
            for lm in self.log_msgs_:
                self.write_(lm)
            if self.template_ is not None:
                self.write_("COG_TEMPLATE: %s" % (self.template_))
            if self.content_ is not None:
                self.write_("JSON")
            # Write empty line to separate "headers" from content
            self.write_("")
            if self.content_ is not None:
                self.write_(self.content_)
            else:
                self.write_(self.message_)
        finally:
            stdout.flush()

    def write_(self, message):
        print(message)

    def debug(self, message):
        self.log_("debug", message)

    def info(self, message):
        self.log_("info", message)

    def warn(self, message):
        self.log_("warn", message)

    def error(self, message):
        self.log_("error", message)

    def log_(self, level, message):
        self.log_msgs_.append("COGCMD_%s: %s" % (level.upper(), message))
