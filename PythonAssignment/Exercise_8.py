a = [4,30,17,22,8,31]
b = a
b[1] = 6

print(a)

# Since list a was changed to b, changing the value of b[1] to 6 changed its value.

c = a[:]
c[2] = 60

print(a)
print(c)

# Nothing happened to list a,
# but the items in list a were transferred to list c so the item in index 2 of list c changed.

def set_first_elem_to_zero(l):
    l[0] = 0
    return print(l)

set_first_elem_to_zero(a)

# The first element in the original list is changed to 0
