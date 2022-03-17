from unittest import TestCase

from CTCIPythonPlayground.src.chapter1.q9_string_rotation import isRotated


class TestStringRotation(TestCase):

    def testRotatedStrings(self):
        is_rotated = isRotated('waterbottle', 'erbottlewat')
        self.assertTrue(is_rotated)

    def testNotRotatedStrings(self):
        is_rotated = isRotated('waterbottle', 'rsbottlewata')
        self.assertFalse(is_rotated)
