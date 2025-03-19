def arithmetic(a, b, operator):
    match operator:
        case "add":
             return a+b
        case "subtract":
             return a-b
        case "multiply":
             return a*b
        case "divide":
             return a/b
         
def sp_eng(sentence): 
    return "english" in sentence.lower()

def array_leaders(numbers):
    new_arr = []
    for i in range(len(numbers)-1):
        if numbers[i] > sum(numbers[i+1:]):
           new_arr.append(i)
    return new_arr

#один из вариантов решения, круче
#def array_leaders(numbers):
#    return [n for (i,n) in enumerate(numbers) if n>sum(numbers[(i+1):])]


def get_order(order):
    menu_arr = ["Burger","Fries","Chicken","Pizza","Sandwich","Onionrings","Milkshake","Coke"]
    #сразу делаем словарь с количеством каждого элемента из строки
    res = {item: order.count(item.lower()) for item in menu_arr}
    #делаем список из ключей, умноженных на количество
    fin = [key for key, value in res.items() for _ in range(value)]
    return " ".join(fin)

print(get_order("milkshakepizzachickenfriesburger"))