# Object-Orientated-Programming
# class Set:

#     def __init__(self, values=None):
#         """This is the constructor.
#         It gets called when you create a new Set.
#         You would use it like
#         s1 = Set()              # empty set
#         s2 = Set([1,2,3,4,5,])  # initialize with values"""
#         self.dict = {}

#         if values is not None:
#             for value in values:
#                 self.add(value)

#     def __repr__(self):
#         """this is the string representation of a Set object
#         if you type it at the python prompt or pass it to str()"""
#         return "Set: " + str(self.dict.keys())
    
#     # we'll represent membership by being a key in self.dict with value True
#     def add(self, value):
#         self.dict[value] = True

#     def contains(self, value):
#         return value in self.dict
    
#     def remove(self, value):
#         del self.dict[value]

# s = Set([1,2,3])
# s.add(4)
# print(s.contains(4))
# s.remove(3)
# print(s.contains(3))

# Functional Tools

def exp(base, power):
    return base ** power

def two_to_the(power):
    return exp(2, power)

from functools import partial
two_to_the = partial(exp, 2)    # is now a function a one variable
print(two_to_the(3))            # 8

square_of = partial(exp, power=2)
print(square_of(3))             # 9

def double(x):
    return 2*x

xs = [1,2,3,4]
twixe_xs = [double(x) for x in xs]      #[2, 4, 6, 8]
twixe_xs = map(double, xs)              #same as above
list_doubler = partial(map, double)     #*function* that doubles a list
twixe_xs = list_doubler(xs)

