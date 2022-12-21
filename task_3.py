def min_max(data):
    low = data[0]
    high = data[0]
    for element in data:
        if element > high:
            high = element
        elif element < low:
            low = element
    return low, high
