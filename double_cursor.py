def double_cursor(array):
    for i in range(len(array)//2):
        array[i], array[len(array)-1-i]= array[len(array)-1-i], array[i]
    return array


print(double_cursor([1,2,3,4,5]))