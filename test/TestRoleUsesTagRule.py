import os
import unittest

from ansiblelint import RulesCollection, Runner


class TestRoleUsesTagRule(unittest.TestCase):

    def setUp(self):
        rulesdir = os.path.join('rules')
        self.rules = RulesCollection.create_from_directory(rulesdir)

    def test_requirements_use_tags(self):
        filename = 'test/good_requirements.yml'
        good_runner = Runner(self.rules, filename, [], [], [])
        self.assertEqual([], good_runner.run())

    def test_requirements_use_branches(self):
        filename = 'test/bad_requirements.yml'
        bad_runner = Runner(self.rules, filename, [], [], [])
        errs = bad_runner.run()
        self.assertEqual(3, len(errs))
