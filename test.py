# coding: utf8
# auto: flytrap
import unittest
from custom import Custom


class CustomTest(unittest.TestCase):
    def test_custom_class(self):
        custom = Custom()
        c = custom.next()
        self.assertEqual(c, '0')
        c1 = Custom('99')
        c2 = Custom('01')
        self.assertEqual(c1 + c2, '100')
        c1 = Custom('88')
        c2 = Custom('11')
        self.assertEqual(c1 + c2, '99')
        Custom.SEED_LIST = 'ab'
        c1 = Custom('b')
        c2 = Custom('b')
        self.assertEqual(c1 + c2, 'ba')


if __name__ == '__main__':
    unittest.main()
