from testbundle.commands.level1.base import Level1


class Level2b(Level1):
    def run(self):
        pass

    def __init__(self):
        super().__init__()

    def level2b_function(self):
        return "2b"
