def solution(value):
    res= str(value)
    while(len(res)<5):
          res ="0"+res
    return "Value is " + res

#or
#  return "Value is %05d" % value
#0 - это что будет перед числом d ,5-общее число в форматируемой строке % value

def highest_rank(arr):
    arr_dict = {}
    for i in arr:
        arr_dict[i] = arr.count(i)
        #максимум из значений словаря
    max_value = max(arr_dict.values())
    #список ключей с максимальным значением
    keys_with_max_value = [key for key, value in arr_dict.items() if value == max_value]
    #максимальный ключ
    return max(keys_with_max_value)



def array(string):
    return None if len(string)<5 else string[2:len(string)-2].replace(","," ")
#def array(strng):
#Когда используется or, Python сначала проверяет, является ли первое выражение 
# истинным. Если первое выражение не пустое или не ложное (например, 
# непустая строка, непустой список, число, не равное нулю), оно возвращается как
# результат. Если первое выражение ложное (например, пустая строка "", пустой 
# список [], None, 0), то возвращается второй операнд (в данном случае None).
 #   return ' '.join(strng.split(',')[1:-1]) or None

