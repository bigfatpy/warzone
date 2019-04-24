import unittest

from warzone.datastructures.odict import ODict


class TestODict(unittest.TestCase):
    def test_order(self):
        odict = ODict()

        odict['1'] = 'foo1'
        odict['2'] = 'foo2'
        odict['3'] = 'foo3'
        odict['4'] = 'foo4'
        odict['5'] = 'foo5'
        odict['6'] = 'foo6'
        odict['7'] = 'foo7'
        odict['8'] = 'foo8'

        del(odict['5'])

        expected = ("{'1': 'foo1', '2': 'foo2', '3': 'foo3', '4': 'foo4', "
                    "'6': 'foo6', '7': 'foo7', '8': 'foo8'}")

        assert repr(odict) == expected
