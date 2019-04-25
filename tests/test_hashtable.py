import unittest
import time

from warzone.datastructures.hashtable import HashTable


class TestHashTable(unittest.TestCase):
    def test_table_resize(self):
        ht = HashTable()
        # Initially the internal table has one member only
        self.assertEqual(len(ht._hash_table), 1)

        # After inserting one item, the new size is the next prime number
        # after doubling the previous size
        ht['foo'] = 'bar'
        self.assertEqual(len(ht._hash_table), 3)

        # With two items, no need to grow the table
        ht['foo2'] = 'bar2'
        self.assertEqual(len(ht._hash_table), 3)

        # With three items, the new size is the next prime number
        # after doubling the previous size
        ht['foo3'] = 'bar3'
        self.assertEqual(len(ht._hash_table), 7)

        # At this point we added 3 items, so the length of the
        # object has to be 3
        self.assertEqual(len(ht), 3)

        # Removing two items then adding a new item will make the
        # table size to shrink to 5 (resize happens only when adding items)
        del(ht['foo2'])
        del(ht['foo3'])
        ht['foo4'] = 'bar4'
        self.assertEqual(len(ht._hash_table), 5)

        # At this point we have 2 items in total
        self.assertEqual(len(ht), 2)

    def test_keys(self):
        ht = HashTable()
        ht['foo'] = 'bar'
        ht['foo2'] = 'bar2'
        ht['foo3'] = 'bar3'
        ht['foo4'] = 'bar4'
        ht['foo5'] = 'bar5'
        keys = ht.keys()

        self.assertEqual(len(keys), 5)

        self.assertIn('foo', keys)
        self.assertIn('foo2', keys)
        self.assertIn('foo3', keys)
        self.assertIn('foo4', keys)
        self.assertIn('foo5', keys)

    def test_items(self):
        ht = HashTable()
        ht['foo'] = 'foo'
        ht['foo2'] = 'foo2'
        ht['foo3'] = 'foo3'
        ht['foo4'] = 'foo4'
        ht['foo5'] = 'foo5'

        items = ht.items()

        self.assertEqual(len(items), 5)

        for key, value in ht.items():
            self.assertEqual(key, value)

    def test_args(self):
        ht = HashTable(foo='bar', foo2='bar2', foo3='bar3')
        self.assertEqual(len(ht), 3)
        self.assertEqual(ht['foo'], 'bar')
        self.assertEqual(ht['foo2'], 'bar2')
        self.assertEqual(ht['foo3'], 'bar3')

    def test_repr(self):
        ht = HashTable(foo='bar', foo2='bar2', foo3='bar3')
        self.assertIn("HashTable(", repr(ht))
        self.assertIn("foo='bar'", repr(ht))
        self.assertIn("foo2='bar2'", repr(ht))
        self.assertIn("foo3='bar3'", repr(ht))


if __name__ == "__main__":
    unittest.main()
