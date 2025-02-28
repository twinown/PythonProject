def find_digit(num, nth):
    return 0 if nth>len(str(num))\
         else int(str(abs(num))[-nth]) if nth>0 else -1

print(find_digit(10, 1))
