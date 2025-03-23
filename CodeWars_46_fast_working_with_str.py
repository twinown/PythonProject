def solution(s):
    s_arr = list(s)
    new_arr = []
    for i in s_arr:
        if i.isupper():
            new_arr.append(" ")
            new_arr.append(i)
        else:
            new_arr.append(i)
    return "".join(new_arr)

#def solution(s):
#    return ''.join(' ' + c if c.isupper() else c for c in s)

def sort_my_string(s):
    return s[::2] + ' ' + s[1::2]

def swap(st):
    return "".join(x.upper() if "aeiou".find(x)!=-1 else x for x in st )
#return "".join( c.upper() if c in "aeiou" else c for c in st)


