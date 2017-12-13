#a
print(float(123))
# Output: 123.0 because it converted int 123 into a float

#b
print(float('123'))
# Output: 123.0 because it converted the string '123' into a float

#c
print(float('123.23'))
# Output: 123.23 because it is already a float, it returns the same value

#d
print(int(123.23))
# Output: 123 because it converted the float into the equivalent rounded down int


#e
print(int('123.23'))
"""
File "/Users/gigithe1st/PycharmProjects/PythonAssignment/Exercise_3.py", line 14, in <module>
    print(int('123.23'))
ValueError: invalid literal for int() with base 10: '123.23'

This is because there is no way to directly convert the string "123.23" into an int.
It has to be converted into a float, then an int.
"""

#f
print(int(float('123.23')))
# Output: 123 because it converted the string into a float
# and then the float was rounded down and converted into an int

#g
print(str(12))
# Output: 12 because the int was converted into a string

#h
print(str(12.2))
# Output: 12.2 because the float was converted into a string

#i
print(bool('a'))
# Output: True because only 0 and empty data sets return false

#j
print(bool(0))
# Output: False because 0 returns false

#k
print(bool(0.1))
# Output: True because only 0 and empty data sets return false
