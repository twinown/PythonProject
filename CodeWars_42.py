def quote(fighter):
    return "I'd like to take this chance to apologize.. To absolutely NOBODY!" if fighter.lower()==conor mcgregor else \
             "I am not impressed by your performance."  

def men_from_boys(arr):
    arr = list(set(arr))
    even_arr = sorted([x for x in arr if x%2==0])
    odd_arr = sorted([x for x in arr if x%2!=0])[::-1]
    return even_arr+odd_arr

def count_sheep(n):
    str_ = ""
    if n!=0:
        for i in range(1,n+1):
            str_ += str(i)+ " sheep..."
    return str_
