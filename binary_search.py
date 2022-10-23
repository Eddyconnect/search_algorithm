from re import M


def binary_search(list, target):
    """
    Returns the index position of the target if found, else it returns None.
    """

    first = 0
    last = len(list) - 1

    while first <= last:
        mid_point = (first + last) // 2
        if list[mid_point] == target:
            return mid_point
        elif mid_point < target:
            first = mid_point + 1
        else:
            last = mid_point - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target is not found in the list")

"""
Below is a small code example to test the above binary_search algorithim
"""

numb = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numb, 12)
verify(result)

numb = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numb, 9)
verify(result)