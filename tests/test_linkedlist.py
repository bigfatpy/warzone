import unittest

from warzone.datastructures.linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_list_append(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        ll.append(40)

        self.assertEqual(ll[0], 10)
        self.assertEqual(ll[1], 20)
        self.assertEqual(ll[2], 30)
        self.assertEqual(ll[3], 40)

        with self.assertRaises(IndexError):
            ll[4]

    def test_list_length(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        ll.append(40)

        self.assertEqual(len(ll), 4)

    def test_repr(self):
        ll = LinkedList()
        ll.append(1)
        ll.append('foo')
        ll.append(2)
        ll.append('bar')

        self.assertEqual(repr(ll), "LinkedList(1, 'foo', 2, 'bar')")

    def test_remove(self):
        ll = LinkedList()
        ll.append(1)
        ll.append('foo')
        ll.append(2)
        ll.append('bar')

        ll.remove(2)
        ll.remove('bar')

        self.assertEqual(repr(ll), "LinkedList(1, 'foo')")
        with self.assertRaises(ValueError):
            ll.remove(2)

    def test_delete(self):
        ll = LinkedList()
        ll.append(1)
        ll.append('foo')
        ll.append(2)
        ll.append('bar')

        del(ll)[0]
        del(ll)[2]

        self.assertEqual(repr(ll), "LinkedList('foo', 2)")
        with self.assertRaises(IndexError):
            del(ll[5])

    def test_node_eq_ne(self):
        ll = LinkedList()
        ll.append(1)
        ll.append('foo')

        self.assertEqual(ll[0], 1)
        self.assertEqual(ll[1], 'foo')
        self.assertNotEqual(ll[0], 2)
        self.assertNotEqual(ll[1], 'bar')

    def test_args(self):
        ll = LinkedList('foo', 1, 'bar', '2')

        self.assertEqual(ll[0], 'foo')
        self.assertEqual(ll[1], 1)
        self.assertEqual(ll[2], 'bar')
        self.assertEqual(ll[3], '2')
        self.assertEqual(len(ll), 4)

    def test_qe_ne(self):
        ll = LinkedList(1, 2, 3)
        ll_other = LinkedList()
        ll_other.append(1)
        ll_other.append(2)
        ll_other.append(3)

        self.assertEqual(ll, ll_other)
        self.assertEqual(ll, [1, 2, 3])
        self.assertNotEqual(ll, LinkedList(1, 2, 4))
        self.assertNotEqual(ll, (1, 2, 3))

    def test_extend(self):
        ll = LinkedList(1, 2, 3)
        ll_other = LinkedList(4, 5, 6)
        ll.extend(ll_other)

        self.assertEqual(len(ll), 6)
        self.assertEqual(ll, LinkedList(1, 2, 3, 4, 5, 6))
        self.assertNotEqual(ll, LinkedList(1, 2, 3))
        self.assertNotEqual(ll, LinkedList(4, 5, 6))

    def test_clear(self):
        ll = LinkedList(1, 2, 3)
        ll.clear()

        self.assertEqual(len(ll), 0)

    def test_sub_list(self):
        ll = LinkedList(LinkedList(1, 1), LinkedList(1, 1))
        self.assertEqual(ll[0][0], 1)
        self.assertEqual(ll[1][0], 1)
        for item in ll:
            for sub_item in item:
                self.assertEqual(sub_item, 1)
        del(ll[1][1])
        self.assertEqual(len(ll[1]), 1)

        ll[0].append({})
        ll[0][2]['foo'] = 'bar'
        self.assertEqual(ll[0][2]['foo'], 'bar')


if __name__ == "__main__":
    unittest.main()
