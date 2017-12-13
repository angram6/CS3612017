list_inception = [[1,3],[3,6]]

def merge_lists(megaList):
    new_list = []
    for lists in megaList:
        for elements in lists:
         new_list.append(elements)
    return print(new_list)

merge_lists(list_inception)
