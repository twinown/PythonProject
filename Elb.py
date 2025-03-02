def reverse(lst):
    new_lst = []
    for i in range(len(lst)-1,-1,-1):
        new_lst.append(lst[i])
    return new_lst

print(reverse(['B','a','o','b','a','b']))