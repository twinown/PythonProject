

# for i in range(1,6):
#   print(i)


def find_multiples(integer, limit):
    myArray = []
    for i in range(integer, limit + integer, integer):
        myArray.append(i)
    return myArray

#так можно
#list(range(integer, limit+1, integer))