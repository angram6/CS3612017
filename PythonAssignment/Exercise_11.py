num_list = [1, 2, 3, 4]

def i_multiply(n):
    if len(n) == 0:
        return "Nothing in this list"
    x = 1
    for num in n:
        x = x * num
    return x
print(i_multiply(num_list))

print('\n')

num_list = [1, 2, 3, 4]

def r_multiply(n):
    if len(n) == 1:
        return n[0]
    else:
        return r_multiply([n[0]]) * r_multiply(n[1:])
print(r_multiply(num_list))