import inspect
import sys


class Number:
    def __init__(self, x=0):
        x += 100
        pass


def introspection_info(obj):
    print(f'{{\n\ttype: {type(obj)}, \n\tattributes: {obj.__getattribute__}, \n\tmethods: {dir(obj)}, \n\tmodule: {inspect.getmodule(obj)}, \n\tsize: {sys.getsizeof(obj)}\n}}')
    return obj


a = Number(10)
number_info = introspection_info(a)
