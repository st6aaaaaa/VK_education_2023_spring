import re


class CustomMeta(type):

    @staticmethod
    def custom_name(key):
        # для пременных вида: _var
        if re.match(r"^_[a-z0-9]+$", key, flags=re.I):
            return '_custom' + key
        # для обычных пременных вида: var
        if re.match(r"^[a-z0-9]+$", key, flags=re.I):
            return 'custom_' + key
        # для private пременных вида: _CustomClass__var
        if re.match(r"^_[a-z0-9]+__[a-z0-9]+$", key, flags=re.I):
            return '__custom' + key[key.rfind('_'):]
        # для магических методов вида: __MagicMethod__
        return key

    def __setattr__(cls, key, value):
        object.__setattr__(cls, CustomMeta.custom_name(key), value)

    def __new__(cls, name, bases, cls_dict, **kwg):
        new_dict = dict()
        for key, val in cls_dict.items():
            new_dict[CustomMeta.custom_name(key)] = val
        new_dict['__setattr__'] = cls.__setattr__
        return super().__new__(cls, name, bases, new_dict, **kwg)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, protect=1, private=2, val=99):
        self.val = val
        self._protect = protect
        self.__private = private

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"

    def __repr__(self):
        return 'testing __repr__ of CustomClass'
