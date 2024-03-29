# You are to write a function, reverse_string(string), that returns the reverse of the string provided. If the reverse of the string is the same as the original string, as in the case of palindromes, return true instead.

class ReverseStringTest(TestCase):
    """docstring for ReverseStringTest"""

    def test_empty_string(self):
        self.assertIsNone(reverse_string(''),
                          msg='should return `None` for empty string')

    def test_palidromes1(self):
        self.assertTrue(
            reverse_string('anna'),
            msg='should return true for `anna`'
        )

    def test_palidromes2(self):
        self.assertTrue(
            reverse_string('NaN'),
            msg='should return true for `NaN`'
        )

    def test_palidromes3(self):
        self.assertTrue(
            reverse_string('civic'),
            msg='should return true for `civic`'
        )

    def test_non_palidromes1(self):
        self.assertEqual(
            'skoob',
            reverse_string('books'),
            msg='should return `skoob` for `books`'
        )

    def test_non_palidromes2(self):
        self.assertEqual(
            'nomolos',
            reverse_string('solomon'),
            msg='should return `nomolos` for `solomon`'
        )

    def test_non_palidromes3(self):
        self.assertEqual(
            'csim',
            reverse_string('misc'),
            msg='should return `csim` for `misc`'
        )