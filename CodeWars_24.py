def check_exam(arr1, arr2):
    total_score = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            total_score += 4
        elif arr2[i] == "":
            total_score += 0
        else:
            total_score -= 1
    return 0 if total_score<0 else total_score


print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))
