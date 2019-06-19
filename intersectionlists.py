"""
The intersection of two lists
"""
def intersection():
    arr1 = [input('item: ') for x in range(int(input('how many items?')))]
    arr2 = [input('item: ') for x in range(int(input('how many items?')))]

    return [x for x in arr1 for y in arr2 if x == y]

if __name__ == "__main__":
    print(intersection())
