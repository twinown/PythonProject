def spin_words(sentence):
    lst = sentence.split(" ")
    for i in range(len(lst)):
        if len(lst[i])>=5:
            lst[i] =lst[i][::-1]
    word = " ".join(lst)
    return word


print(spin_words("Welcome to the jungle"))