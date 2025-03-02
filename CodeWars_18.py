def gimme(input_array):
    cache_array = []
    cache_array.extend(input_array)
    cache_array.sort()
    return input_array.index(cache_array[1])

print(gimme([2,3,1]))