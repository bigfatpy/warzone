"""
Hosts Generation

Input: my[001..900].domain.com

Output: my001.domain.com, my002.domain.com, ... my900.domain.com
"""
import re
import unittest


def generate_hosts(inventory):
    """
    Function that will generates a list of hosts based
    in the specific string 'my[001..900].domain.com'
    
    :param inventory: specific string

    returns a list with hosts names.  
    """
    groups = re.search(r'^'
                       r'(?P<prefix>.*)' # everything before [
                       r'\['
                       r'(?P<first>[0-9]+)' # numbers between [ and ..
                       r'..'
                       r'(?P<last>[0-9]+)' # number between .. and ]
                       r'\]'
                       r'(?P<suffix>.*)' # everthing after ] 
                       r'$',
                       inventory)
    size = len(groups.group('first')) 

    hosts = []

    for x in range(int(groups.group('first')), int(groups.group('last')) + 1):
        hosts.append('{0}{1:0{2}}{3}'.format(groups.group('prefix'),
                                              x,
                                              size,
                                              groups.group('suffix')))

    return hosts


class Test(unittest.TestCase):
    result = generate_hosts(inventory='my[0001..1000].domain.com')
    
    def test_format(self):
        self.assertIn('my0003.domain.com', self.result)
    
    def test_size(self):
        self.assertEqual(len(self.result), 1000)


if __name__ == "__main__":
    unittest.main()
