from testbundle.commands.level1.level2a.base import Level2a

class Commandc(Level2a):
    def __init__(self):
        super().__init__()

    def run(self):
        self.run_command()

    def run_command(self):
        level = self.level2a_function()
        level = level + "c"
        self.response.content(level, template="template").send()