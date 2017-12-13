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

def new_animal(l):
    if (len(animals) <= 4):
        animals.insert(4, "sugar glider")
        print(animals)
    else:
        print(animals)

new_animal(animals)