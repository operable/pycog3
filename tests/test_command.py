import os
import unittest
import subprocess


# test summary for command
# !commanda
# !level1 - commanda
# !level1 - level2a - commandc
# !level1 - level2b - leveln - commandz
# !nonexistent
# COG_COMMAND env var no set
# COG_COMMAND env var set but empty

class TestCommand(unittest.TestCase):

    fixed_output_prefix = "COG_TEMPLATE: template\nJSON\n"
    bundle_name = 'testbundle'

    def setUp(self):
        os.environ['dyn_config_var1'] = '1'
        os.environ['COG_BUNDLE'] = self.bundle_name
        self.maxDiff=None
        pass

    def test_level0_commanda(self):
        os.environ['COG_COMMAND'] = 'commanda'
        result = subprocess.check_output(["cog-command"])

        self.assertEqual(result.decode("utf-8"), self.fixed_output_prefix + '"0a"\n')

    def test_level1_commandb(self):
        os.environ['COG_COMMAND'] = 'level1-commandb'
        result = subprocess.check_output(["cog-command"])

        self.assertEqual(result.decode("utf-8") , self.fixed_output_prefix+'"1b"\n')

    def test_level1_level2a_commandc(self):
        os.environ['COG_COMMAND'] = 'level1-level2a-commandc'
        result = subprocess.check_output(["cog-command"])

        self.assertEqual(result.decode("utf-8"), self.fixed_output_prefix + '"2ac"\n')

    def test_level1_level2b_leveln_commandz(self):
        os.environ['COG_COMMAND'] = 'level1-level2b-leveln-commandz'
        result = subprocess.check_output(["cog-command"])

        self.assertEqual(result.decode("utf-8"), self.fixed_output_prefix + '"nz"\n')

    def test_missing_cog_command_env_var(self):
        os.environ.pop("COG_COMMAND")
        result=subprocess.run(["cog-command"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.stderr.decode("utf-8"), "ERROR: COG_COMMAND env var is not set\n")

    def test_empty_cog_command_env_var(self):
        os.environ['COG_COMMAND'] = ''
        result=subprocess.run(["cog-command"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.stderr.decode("utf-8"), "ERROR: COG_COMMAND env var is set but empty\n")

    def test_invalid_command(self):
        os.environ['COG_COMMAND'] = 'nonexisting'
        full_path = "%s.commands.%s" % (self.bundle_name, os.environ.get("COG_COMMAND"))
        result=subprocess.run(["cog-command"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.stderr.decode("utf-8"), 'ERROR: Unable to import module "' + str(full_path) + '"\n')

if __name__ == '__main__':
    unittest.main()