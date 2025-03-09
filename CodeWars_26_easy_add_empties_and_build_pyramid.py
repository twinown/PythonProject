def tower_builder(n_floors):
    floors = []
    for i in range(n_floors):
        if i!=0:
            floors.append(floors[i-1]+'**')
        else: floors.append('*')
    return floors

print(tower_builder(10))

def tower_builder_correct(n):
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]