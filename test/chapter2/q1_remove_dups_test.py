from unittest import TestCase

from CTCIPythonPlayground.src.chapter2.q1_remove_dups import Q1RemoveDups


def generateTestList():
    q1_list = Q1RemoveDups()
    q1_list.add(2)
    q1_list.add(1)
    q1_list.add(3)
    q1_list.add(1)
    q1_list.add(2)
    q1_list.add(4)

    solo_list = Q1RemoveDups()
    solo_list.add(1)
    solo_list.add(1)
    solo_list.add(1)
    return q1_list, solo_list


class TestQ1RemoveDups(TestCase):

    def setUp(self):
        self.q1_list, self.solo_list = generateTestList()

    def testSetup(self):
        list_str = self.q1_list.print_list()
        expected_str = '[2 -> 1 -> 3 -> 1 -> 2 -> 4 -> None]'
        self.assertEqual(list_str, expected_str)

    def testRemoveDups(self):
        self.q1_list.remove_dups()
        list_str = self.q1_list.print_list()
        expected_str = '[2 -> 1 -> 3 -> 4 -> None]'
        self.assertEqual(list_str, expected_str)

    def testRemoveDupsMonoElementList(self):
        self.solo_list.remove_dups()
        list_str = self.solo_list.print_list()
        expected_str = '[1 -> None]'
        self.assertEqual(list_str, expected_str)
