def zero_fuel(distance_to_pump, mpg, fuel_left):
    return  mpg * fuel_left >= distance_to_pump

print(zero_fuel(50,25,2))