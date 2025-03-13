def kebabize(string):
    a = ''
    for i in string:
        if i.isupper():
            a += '-' + i.lower()
        if i.islower():
            a += i
    return a.strip('-')

#print(kebabize("camelsHaveThreeHumps"))

def capitalize(s, ind):
  return ''.join(c.upper() if i in ind else c for i, c in enumerate(s))

 # for i in ind:
 #        s = s[:i] + s[i:].capitalize()
 #    return s

#print(capitalize("abcdef",[1,2,5,100]))

# def power_of_two(x):
#     # прикинь , в двоичной сстеме у числа. которое явл степенью двойкивсего 1 единица
#     #return bin(x).count('1') == 1
#     while x > 1 and x % 2 == 0:
#         x = x // 2
#     return x == 1
# print(power_of_two(4096))

def digital_root(n):
    str_n = str(n)
    sum_n = 0
    while len(str_n)>1:
           for i in str_n:
               sum_n += int(i)
               str_n = str(sum_n)
           sum_n = 0
    return int(str_n)



#print(digital_root(942)) #6


def dublicate_count(s):
    s = s.lower()
    lst = list(s)
    another_lst = []
    for i in lst:
        count = 0
        cache = i
        for j in lst:
          if j == cache:
            count+=1
            lst.remove(i)
        if count>1:
           another_lst.append(count)
    return len(another_lst)

print(dublicate_count("Indivisibilities"))