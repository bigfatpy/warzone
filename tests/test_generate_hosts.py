import unittest

from warzone.utils.misc import generate_hosts


class Test(unittest.TestCase):
    result = generate_hosts(inventory='my[0001..1000].domain.com')

    def test_format(self):
        self.assertIn('my0003.domain.com', self.result)

    def test_size(self):
        self.assertEqual(len(self.result), 1000)


if __name__ == "__main__":
    unittest.main()
