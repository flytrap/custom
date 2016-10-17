# coding: utf8
# auto: flytrap
import unittest
from custom import CustomCarry, Seed, change_custom_seed, _default_custom_seed


class CustomTest(unittest.TestCase):
    def test_custom_class(self):
        print('custom_class:1')
        custom = CustomCarry()
        c = custom.next()
        self.assertEqual(c, '1')
        c1 = CustomCarry('99')
        c2 = CustomCarry('01')
        self.assertEqual(c1 + c2, '100')
        c1 = CustomCarry('88')
        c2 = CustomCarry('11')
        self.assertEqual(c1 + c2, '99')
        c1 = CustomCarry('b')
        c1.SEED_LIST = ['ab']
        c2 = CustomCarry('b')
        c2.SEED_LIST = ['ab']
        self.assertEqual(c1 + c2, 'ba')

    def test_seed(self):
        print('seed:2')
        seed = Seed('abc')
        CustomCarry.SEED_LIST = seed
        c = CustomCarry()
        self.assertEqual(c.SEED_LIST, 'abc')
        _default_custom_seed()

    def test_change_custom_seed(self):
        print('change_custom_seed:3')
        change_custom_seed(['abc', 'd'])
        self.assertEqual(CustomCarry.SEED_LIST, 'abcd')
        _default_custom_seed()

    def test_iter_password(self):
        print('iter_password:4')
        import string
        change_custom_seed(string.printable)
        c = CustomCarry(CustomCarry.SEED_LIST[0] * 6)
        self.assertEqual(c.next(), '000001')
        self.assertEqual(c.next(), '000002')
        for i in xrange(100):
            c.next()
        self.assertEqual(c.next(), '000013')
        for i in xrange(10000):
            c.next()
        self.assertEqual(c.next(), '000114')
        _default_custom_seed()


if __name__ == '__main__':
    unittest.main()
