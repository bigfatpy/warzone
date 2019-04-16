import math
import typing

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
    def __init__(self, **kwargs):
        self._size = 1
        self._hash_table = [[] for _ in range(self._size)]
        self._counter = 0
        self._resizing = False
        for key, value in kwargs.items():
            self[key] = value

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

    def __repr__(self):
        items = [f'{key}={repr(value)}' for key, value in self.items()]
        return f'{self.__class__.__name__}({", ".join(items)})'

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
