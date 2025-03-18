def get_real_floor(n):
    return 0 if n == 1 or n ==0 else n if n<0 else n-2


def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))

def vowel_2_index(string):
    vowels = 'aeiouAEIOU'
    #пример с элсом
    return ''.join(x if x not in vowels else str(n + 1) for n,x in enumerate(string))
print(vowel_2_index("this is my string"))

def remove_(integer_list, values_list):
    #пример без элса
    return [x for x in integer_list if x not in values_list]
print(remove_([1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3]))