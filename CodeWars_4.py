def derive(coefficient, exponent):
    return str(coefficient*exponent)+"x^"+str(exponent-1)

print(derive(7,8))