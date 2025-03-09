def last(s):
    lst = s.split(' ')
    sorted_lst = sorted(lst, key=lambda x: x[len(x) - 1])
    return sorted_lst

print(last("man i need a taxi up to ubud"))