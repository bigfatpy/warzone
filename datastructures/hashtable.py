import math
import time
import typing
import unittest

from dataclasses import dataclass


@dataclass
class HashTableItem:
    key: typing.Any
    value: typing.Any


def is_prime(n):
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def get_next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


class HashTable:
    def __init__(self):
        self._size = 1
        self._hash_table = [[] for _ in range(self._size)]
        self._counter = 0
        self._resizing = False

    def __setitem__(self, key, value):
        hash_key = hash(key) % self._size
        for member in self._hash_table[hash_key]:
            if member.key == key:
                member.value = value
                return
        self._hash_table[hash_key].append(HashTableItem(key, value))
        self._counter += 1
        self._resize_table()

    def __getitem__(self, item):
        hash_key = hash(item) % self._size
        for member in self._hash_table[hash_key]:
            if member.key == item:
                return member.value
        raise KeyError(item)

    def __delitem__(self, key):
        hash_key = hash(key) % self._size
        for index, member in enumerate(self._hash_table[hash_key]):
            if member.key == key:
                del(self._hash_table[hash_key][index])
                self._counter -= 1
                return
        raise KeyError(key)

    def __len__(self):
        return self._counter

    def __iter__(self):
        for bucket in self._hash_table:
            for item in bucket:
                yield item.key

    def keys(self):
        table_keys = []
        for bucket in self._hash_table:
            for item in bucket:
                table_keys.append(item.key)
        return table_keys

    def items(self):
        table_items = []
        for bucket in self._hash_table:
            for item in bucket:
                table_items.append((item.key, item.value))
        return table_items

    def _resize_table(self):
        if self._resizing:
            return

        # Extend only when total items is greater than 70% of the current size
        if (self._size * 0.7) < self._counter:
            self._resizing = True
            self._extend_table()
            self._resizing = False

        # Shrink only when total items is less than 30% of the current size
        if (self._size * 0.3) > self._counter:
            self._resizing = True
            self._shrink_table()
            self._resizing = False

    def _extend_table(self):
        # New size is the next prime after 2 times the old size
        self._size = get_next_prime(self._size * 2)

        # Backing up the old table
        old_hash_table = self._hash_table

        # Generating the new table
        self._hash_table = [[] for _ in range(self._size)]
        self._counter = 0

        # Re-hashing the old table into the new table
        for item in old_hash_table:
            for member in item:
                self[member.key] = member.value

    def _shrink_table(self):
        # New size is the next prime after the 150% of the current counter
        self._size = get_next_prime(int(self._counter * 1.5))

        # Backing up the old table
        old_hash_table = self._hash_table

        # Generating the new table
        self._hash_table = [[] for _ in range(self._size)]
        self._counter = 0

        # Re-hashing the old table into the new table
        for item in old_hash_table:
            for member in item:
                self[member.key] = member.value


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

    def test_get_item_time(self):
        ht = HashTable()
        # Adding 100000 items to the table
        for i in range(100000):
            ht[i] = i

        # Calculating the time to pick one item with low index
        start = time.perf_counter()
        # Doing it a million times
        for _ in range(1000000):
            ht[10]
        time_taken_low_index = time.perf_counter() - start

        # Calculating the time to pick one item with high index
        start = time.perf_counter()
        # Doing it a million times
        for _ in range(1000000):
            ht[98000]
        time_taken_high_index = time.perf_counter() - start

        self.assertAlmostEqual(time_taken_low_index, time_taken_high_index, places=1)

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


if __name__ == "__main__":
    unittest.main()
