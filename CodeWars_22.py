def data_reverse(data):
    res = []
    for i in range(len(data) - 8, -1, -8):
        res.extend(data[i:i + 8])
    return res

print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))