from testbundle.commands.base import Testbundle


class Commanda(Testbundle):
    def __init__(self):
        super().__init__()

    def run(self):
        self.run_command()

    def run_command(self):
        level = self.level0_function()
        level = level + "a"
        self.response.content(level, template="template").send()