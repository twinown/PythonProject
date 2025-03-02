# def move_zeros(lst):
#     new_lst = []
#     i = 0
#     while i<len(lst):
#         if lst[i] == 0:
#             new_lst.append(lst[i])
#             lst.pop(i)
#         else: i+=1
#     lst.extend(new_lst)
#     return lst

def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i)  # Remove the element from the array
            array.append(i)  # Append the element to the end
    return array

print(move_zeros([1,2,3,0,0,2,0,5,8,0,1]))

