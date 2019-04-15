class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def __repr__(self):
        return repr(self._value)

    def __eq__(self, other):
        if self._value == other:
            return True
        return False

    def __ne__(self, other):
        return not self == other

    def __iter__(self):
        return iter(self._value)

    def __next__(self):
        return next(self._value)

    def __getattr__(self, item):
        return getattr(self._value, item)

    def __getitem__(self, item):
        return self._value[item]

    def __delitem__(self, key):
        del(self._value[key])

    def __len__(self):
        return len(self._value)

    def __setitem__(self, key, value):
        self._value[key] = value


class LinkedList:
    def __init__(self, *args):
        self.first = self.head = None
        for arg in args:
            self.append(arg)

    def append(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
        if self.head is not None:
            self.head._next = new_node
        self.head = new_node

    def remove(self, value):
        if self.first._value == value:
            if self.first._next is None:
                self.first = None
                return
            self.first = self.first._next
            return

        previous = self.first
        node = self.first._next

        while node is not None:
            if node._value == value:
                previous._next = node._next
                return
            previous = node
            node = node._next

        raise ValueError(f'{value} not in LinkedList')

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def clear(self):
        self.first = self.head = None

    def __delitem__(self, key):
        if key == 0:
            if self.first._next is None:
                self.first = None
                return
            self.first = self.first._next
            return

        previous = self.first
        node = self.first._next

        count = 1
        while node is not None:
            if count == key:
                previous._next = node._next
                return
            previous = node
            node = node._next
            count += 1

        raise IndexError('list index out of range')

    def __getitem__(self, item):
        node = self.first
        count = 0
        while node is not None:
            if count == item:
                return node
            node = node._next
            count += 1
        raise IndexError('list index out of range')

    def __len__(self):
        node = self.first
        count = 0
        while node is not None:
            node = node._next
            count += 1
        return count

    def __repr__(self):
        items = ''
        for item in self:
            items += f'{item}, '
        items = items.rstrip(', ')
        return f'{self.__class__.__name__}({items})'

    def __eq__(self, other):
        if not any([isinstance(other, type(self)),
                    isinstance(other, list)]):
            return False

        if len(self) != len(other):
            return False
        for index, node in enumerate(self):
            if node != other[index]:
                return False
        return True

    def __ne__(self, other):
        return not self == other
