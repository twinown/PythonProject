def reverse_alternate(st):
    lst = st.split(" ")
    lst = list(filter(None, lst))
    for i in range(len(lst)):
        if i%2!=0:
            lst[i] = lst[i][::-1]
    return " ".join(lst)
#return " ".join(y[::-1] if x%2 else y for x,y in enumerate(string.split()))


print(reverse_alternate("This       is a  test "))