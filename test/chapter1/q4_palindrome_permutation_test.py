from unittest import TestCase

from CTCIPythonPlayground.src.chapter1.q4_palindrome_permutation import checkPalindrome


class TestPalindromePermutation(TestCase):

    def testStandardPalindrome(self):
        is_palindrome = checkPalindrome('tacocat')
        self.assertTrue(is_palindrome)

    def testPalindromeWithSpaces(self):
        is_palindrome = checkPalindrome('taco cat')
        self.assertTrue(is_palindrome)

    def testPalindromePermutation(self):
        is_palindrome = checkPalindrome('acto tac')
        self.assertTrue(is_palindrome)

    def testNonPalindrome(self):
        is_palindrome = checkPalindrome('not a palindrome')
        self.assertFalse(is_palindrome)
