def div_con(x):
    return (sum(i for i in x if isinstance(i, int))
            - sum(int(j) for j in x if isinstance(j, str)))