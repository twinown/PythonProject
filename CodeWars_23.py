def to_float_array(arr):
    for i in range(len(arr)):
        arr[i] = float(arr[i])
    return arr

#easy way  return [float(n) for n in arr]