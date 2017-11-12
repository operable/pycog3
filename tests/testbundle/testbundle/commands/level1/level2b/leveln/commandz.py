from testbundle.commands.level1.level2b.leveln.base import Leveln


class Commandz(Leveln):
    def __init__(self):
        super().__init__()

    def run(self):
        self.run_command()

    def run_command(self):
        level = self.leveln_function()
        level = level + "z"
        self.response.content(level, template="template").send()