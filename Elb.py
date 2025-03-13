def reverse(lst):
    new_lst = []
    for i in range(len(lst)-1,-1,-1):
        new_lst.append(lst[i])
    return new_lst

#print(reverse(['B','a','o','b','a','b']))


def count(lst):
    cache = 0
    for i in lst:
        if lst.count(lst[i])>cache:
           cache = lst[i]
    return cache
print(count([1,2,1,3,2,1]))







def fizzbuzz(lst):
    for i in range(len(lst)):
        if lst[i]%3==0 and len[i]%5==0:
            lst[i] = "fizzbuzz"
        elif lst[i]%3==0:
             lst[i] = "fizz"
        elif  lst[i]%5==0:
             lst[i] = "buzz"
    return lst


def custom_sort(lst):
    str_lst = []
    int_lst = []
    for i in lst:
        if isinstance(i,int):
            int_lst.append(i)
        else:
            str_lst.append(i)
    str_lst.sort()
    int_lst.sort()
    return int_lst.extend(str_lst)

print(custom_sort([5,"abc",2,1,"d","ac"]))


def count_file_types(lst):
    word  = "hoiop.jpg"
    count_jpg = 0
    count_pptx = 0
    for i in lst:
      if i[-3:len(lst)]=="jpg":
          count_jpg+=1
      else:
            count_pptx+=1
    return word[-3:len(word)]


print(count_file_types(["dwsfwad.jpg"]))
