# coding: utf8
# auto: flytrap
import string


class Seed(object):
    def __init__(self):
        super(Seed, self).__init__()
        self.__seed_list = string.digits

    def __set__(self, instance, value):
        try:
            if len(value) == 0:
                return
            if not isinstance(value, (basestring, list, tuple)):
                return
            if len(set(value)) != len(value):
                return
            self.__seed_list = list(value)
        except (ValueError, IndexError):
            pass

    def __get__(self, instance, owner):
        return self.__seed_list

    def __len__(self):
        return len(self.__seed_list)


class Custom(object):
    # Iterable class
    SEED_LIST = Seed()

    def __init__(self, start=None):
        super(Custom, self).__init__()
        if len(self.SEED_LIST) == 0:
            self.SEED_LIST = string.digits
        if not start:
            start = self.SEED_LIST[0]
        self.seed_len = len(self.SEED_LIST)
        self.start = str(start)
        self.__cur_num = self.start[:]

    def __iter__(self):
        return self

    def next(self):
        return self.__add__(self.__class__(self.SEED_LIST[0]))

    def __add__(self, other):
        other = self.__revise_object(other)
        max_len = max(len(self), len(other))
        my_str = self.__create_len_string(self, max_len)[::-1]
        other_str = self.__create_len_string(other, max_len)[::-1]
        cf_flag = 0
        new_string = []
        for my_char, other_char in zip(my_str, other_str):
            my_char, other_char = self.__revise_char(my_char), self.__revise_char(other_char)
            seed_index = self.SEED_LIST.index(my_char) + self.SEED_LIST.index(other_char) + cf_flag
            cf_flag, index = divmod(seed_index, self.seed_len)
            new_string.insert(0, self.SEED_LIST[index])
        if new_string[0] == self.SEED_LIST[0]:
            return ''.join(new_string[1:])
        else:
            return ''.join(new_string)

    def __str__(self):
        return self.__cur_num

    def __len__(self):
        return len(self.__cur_num)

    def __create_len_string(self, old_str, length):
        # Create point length string
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
