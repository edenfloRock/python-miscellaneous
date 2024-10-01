# Example 1
s = """w'o'w"""
print (repr(s)) # a representation of x. eval will usually convert the result of this function back to the original object.

print(str(s)) #  a human-readable string that describes the object. This may elide some technical detail.

print(eval(repr(s)))
# print(eval(str(s))) # Error


# Example 2

import datetime
today = datetime.datetime.now()
print(str(today)) # 2024-10-01 15:26:38.220339
print(repr(today)) # datetime.datetime(2024, 10, 1, 15, 26, 38, 220339)

# Example 3
class Represent (object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Represent(x={}), y=\"{}\")".format(self.x, self.y)

    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)

r = Represent(1, "Hooper")
print(r) # prints __str__
print(r.__repr__) # prints __repr__: '<bound method Represent.__repr__ of Represent(x=1, y="Hopper")>'

rep = r.__repr__() # sets the execution of __repr__ to a new variable
print(rep) # prints 'Represent(x=1, y="Hooper")'
r2 = eval(rep) # evaluates rep
print(r2) # prints __str__ from new object
print(r2 == r ) # prints 'False' because they are different object
