import re


def func(value, type_var):
    if not isinstance(value, type_var):
        var = re.findall(r" '([_.a-z]+)'", str(type(value)))[0]
        tmp = "должно быть целым, а не {}".format(var)
        raise TypeError(tmp)


class Integer:
    def __set_name__(self, owner, name):
        self.var_name = '_' + name

    def __set__(self, instance, value):
        func(value, int)
        instance.__dict__[self.var_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.var_name]


class String:
    def __set_name__(self, owner, name):
        self.var_name = '_' + name

    def __set__(self, instance, value):
        func(value, str)
        instance.__dict__[self.var_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.var_name]


class PositiveInteger:
    def __set_name__(self, owner, name):
        self.var_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.var_name]

    def __set__(self, instance, value):
        func(value, int)
        if value <= 0:
            raise TypeError('должно быть положительным')
        instance.__dict__[self.var_name] = value


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()
    
