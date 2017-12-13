animals = ["cat", "otter", "panda", "llama"]

def show_list(l):
        for items in l:
            print(items)
show_list(animals)

print("\n")

def reverse_list(l):
    for items in reversed(l):
        print(items)
reverse_list(animals)

print("\n")

def list_length(list):
    elements = 0
    for numbers in list:
        elements += 1
    print('There are', elements, 'elements in this list.')

list_length(animals)
