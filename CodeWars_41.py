def open_or_senior(data):
    return ["Senior" if i>=55 and v>7 else "Open" for i,v in enumerate(data)]

print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))