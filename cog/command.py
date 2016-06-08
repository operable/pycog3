import abc
import os
import sys

from cog.request import Request
from cog.response import Response

class FailedCommandError(Exception):
    def __init__(self):
        self.msg = "Command execution failed"

    def __str__(self):
        return self.msg


class Command(metaclass=abc.ABCMeta):
    def __init__(self, getenv=os.getenv):
        self.req_ = Request(getenv=getenv)
        self.resp_ = Response()

    def execute(self):
        try:
            self.prepare()
            self.run()
        except FailedCommandError:
            sys.stdout.flush()
            sys.stderr.flush()
            sys.exit(1)

    @abc.abstractmethod
    def run(self):
        pass

    def prepare(self):
        pass

    @property
    def request(self):
        return self.req_

    @property
    def response(self):
        return self.resp_

    def config(self, name):
        return os.getenv(name, None)

    def fail(self, message):
        print("%s\n" % (message), file=sys.stderr)
        raise FailedCommandError
