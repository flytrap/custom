# coding: utf8
# auto: flytrap
import string

DEFAULT_SEED = string.digits


class Seed(object):
    """
    Use to CustomCarry:
    seed = Seed()
    seed = Seed('abc')
    seed = Seed([1,2,3])
    CustomCarry.SEED_LIST = seed()
    """

    def __init__(self, value=None):
        super(Seed, self).__init__()
        if value:
            self.__set__(self, value)
        else:
            self.__seed_list = DEFAULT_SEED

    def __set__(self, instance, value):
        if isinstance(value, (list, tuple)):
            value = ''.join(value)
        if len(set(value)) != len(value):
            value = ''.join(set(value))
        if len(value) < 2:
            self.__seed_list = DEFAULT_SEED
        else:
            self.__seed_list = value

    def __get__(self, instance, owner):
        return self.__seed_list

    def __len__(self):
        return len(self.__seed_list)


class CustomCarry(object):
    """
    A Iter object
    c = CustomCarry()
    c = CustomCarry('000000') # c.next() == '000001'
    print(c.next())
    """
    # Iterable class
    SEED_LIST = Seed()

    def __init__(self, start=None):
        super(CustomCarry, self).__init__()
        if len(self.SEED_LIST) < 2:
            self.SEED_LIST = DEFAULT_SEED
        if not start:
            start = self.SEED_LIST[0]
        self.start = ''.join(start)
        self.__cur_num = self.start[:]

    def __iter__(self):
        return self

    def next(self):
        self.__cur_num = self.__add__(self.__class__(self.SEED_LIST[1]))
        return self.__cur_num

    def __add__(self, other):
        other = self.__revise_object(other)
        max_len = max(len(self), len(other))
        my_str = self.__create_len_string(self, max_len)[::-1]
        other_str = self.__create_len_string(other, max_len)[::-1]
        cf_flag = 0
        # temp strong string char
        new_string = []
        for my_char, other_char in zip(my_str, other_str):
            my_char, other_char = self.__revise_char(my_char), self.__revise_char(other_char)
            # calc new index
            seed_index = self.SEED_LIST.index(my_char) + self.SEED_LIST.index(other_char) + cf_flag
            cf_flag, index = divmod(seed_index, len(self.SEED_LIST))
            new_string.insert(0, self.SEED_LIST[index])
        if new_string[0] == self.SEED_LIST[0]:
            # not over flower
            return ''.join(new_string[1:])
        else:
            return ''.join(new_string)

    def __str__(self):
        return self.__cur_num

    def __len__(self):
        return len(self.__cur_num)

    def __create_len_string(self, old_str, length):
        # insert index 0 char
        str_len = len(old_str)
        return str((length + 1 - str_len) * self.SEED_LIST[0]) + str(old_str)

    def __revise_object(self, ob):
        # Try return a new class
        if not isinstance(ob, self.__class__):
            if isinstance(ob, basestring):
                return self.__class__(str(ob))
            if isinstance(ob, (list, tuple)):
                return self.__class__(''.join(ob))
            return self.__class__(self.SEED_LIST[0])
        return ob

    def __revise_char(self, char):
        # Not found return index 0 char
        if char not in self.SEED_LIST:
            char = self.SEED_LIST[0]
        return char


def change_custom_seed(seed):
    """
    change CustomCarry seed
    example:
    change_custom_seed([1,2,3])  # then CustomCarry.SEED_LIST == '123' is True
    :param seed:
    :return:
    """
    if isinstance(seed, (basestring, list, tuple)):
        seed = Seed(seed)
    if isinstance(seed, Seed):
        CustomCarry.SEED_LIST = seed


def _default_custom_seed():
    change_custom_seed(DEFAULT_SEED)
