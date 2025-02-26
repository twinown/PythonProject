
def is_vow(inp):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(inp)):
        if chr(inp[i]) in vowels :
            inp[i] = chr(inp[i])
    return inp
#пайтон - решение - КРУТО
#def is_vow(inp):
#return [chr(n) if chr(n) in "aeiou" else n for n in inp]