
def unique_in_order(sequence):
    lst = list(sequence)
    new_lst = []
    for i in range(0,len(lst)-1):
            if lst[i]==lst[i+1]:
                lst[i] = None
    for i in range(0,len(lst)):
        if lst[i] is not None:
            new_lst.append(lst[i])
    return new_lst

#unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

print(unique_in_order([1, 2, 2, 3, 3,2,2]))