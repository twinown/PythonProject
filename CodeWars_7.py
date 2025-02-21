def lowercase_count(strng):
    #java style
    """count = 0
    for i in strng:
        if i.isupper():
            count+=1
            return count"""
    # python style или еще
    # return sum(a.islower() for a in strng)
    return sum(1 for i in strng if i.islower())


print(lowercase_count("heLlo"))