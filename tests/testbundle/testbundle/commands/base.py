from cog.command import Command


class Testbundle(Command):
    def run(self):
        pass

    def __init__(self):
        super().__init__()
        self.dyn_config_var1 = None

    def prepare(self):
        self.dyn_config_var1 = self.config("dyn_config_var1")
        if self.dyn_config_var1 is None:
            self.fail('Missing dyn_config_var1')

    def level0_function(self):
        return "0" #string 0 representing level 0
