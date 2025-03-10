def bubble_sort(lst):
    for _ in lst:
        for j in range(1,len(lst)):
            if lst[j]<lst[j-1]:
                lst[j-1],lst[j] = lst[j],lst[j-1]
    return lst

print(bubble_sort([3,1,2,4,7,6,5]))

