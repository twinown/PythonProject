def sum_digits(number):
    res = 0
    for el in str(number):
        if el.isdigit():
         res+=int(el)
    return res

#можно было просто так
#return sum(int(d) for d in str(abs(number)))