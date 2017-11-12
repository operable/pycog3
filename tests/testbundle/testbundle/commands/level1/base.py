from testbundle.commands.base import Testbundle

class Level1(Testbundle):
    def run(self):
        pass

    def __init__(self):
        super().__init__()

    def level1_function(self):
        return "1"
