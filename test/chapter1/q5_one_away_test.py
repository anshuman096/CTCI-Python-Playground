from unittest import TestCase

from CTCI.src.chapter1.q5_one_away import isOneAway


class TestOneAway(TestCase):

    def testOneDeletionAway(self):
        one_away = isOneAway('pale', 'ple')
        self.assertTrue(one_away)

    def testOneInsertionAway(self):
        one_away = isOneAway('pales', 'pale')
        self.assertTrue(one_away)

    def testOneSubstitutionAway(self):
        one_away = isOneAway('bale', 'pale')
        self.assertTrue(one_away)

    def testMoreThanOneAway(self):
        one_away = isOneAway('pale', 'bake')
        self.assertFalse(one_away)
