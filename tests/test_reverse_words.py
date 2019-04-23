import unittest

from warzone.utils.reverse_words import reverse_words

class Test(unittest.TestCase):
    result = reverse_words(value='I am a software engineer. But,, I am also an operations engi.neer.')

    def test_result(self):
        self.assertEqual(self.result, 'I ma a erawtfos reenigne. tuB,, I ma osla na snoitarepo igne.reen.')


if __name__ == "__main__":
    unittest.main()
