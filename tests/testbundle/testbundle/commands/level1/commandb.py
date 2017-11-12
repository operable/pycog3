from testbundle.commands.level1.base import Level1

class Commandb(Level1):
    def __init__(self):
        super().__init__()

    def run(self):
        self.level1_function()
        self.run_command()

    def run_command(self):
        level = self.level1_function()
        level = level + "b"
        self.response.content(level, template="template").send()