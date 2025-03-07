def find_outlier(integers):
    #быстрое формирование списка с условием
    odds = [x for x in integers if x % 2 != 0]
    evens= [x for x in integers if x % 2 == 0]
    return odds[0] if len(odds)<len(evens) else evens[0]