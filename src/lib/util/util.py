import math

class Util(object):
    def __init__(self):
        self
    
    @classmethod
    def perimeter(shape, *args):
        pass

    @classmethod
    def area(cls, shape, *args):
        area = 0
        if shape == "square" or shape == "rectangle":
            area = reduce(lambda x, y: x*y, args)
        elif shape == "circle":
            area = 2 * math.pi * (args[0] ** 2)
        else:
            print "The shape, %s, is not supported" %(shape)
        return area

    @classmethod
    def volume(arg1, arg2, arg3):
        pass

    @classmethod
    def speed(arg1, arg2):
        pass

    @classmethod
    def distance(arg1, arg2):
        pass

    @classmethod
    def time(arg1, arg2):
        pass
