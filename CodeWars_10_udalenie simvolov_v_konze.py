def no_boring_zeros(n):
    word = str(n)
    if n != 0:    # то же , если if n
      while word[-1]=='0':
            word = word[0:-1]
            #можно просто вот так
   # return int(str(n).rstrip('0')) if n else n
    return 0 if n==0 else int(word)