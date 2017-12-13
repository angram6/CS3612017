"""
#a
print(2000.3**200)
# Output: OverflowError, ‘Result too large’ because in python floats have a defined length, unlike ints
"""
#b
print(1.0 + 1.0 - 1.0)
# Output: 1.0 because since all values are floats, it will return a float

#c
print(1.0+1.0e20 - 1.0e20)
# Output: 0.0 because it rounds the values of 1.0e20

