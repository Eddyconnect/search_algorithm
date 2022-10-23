def linear_search(list, target):
    """
    Returns the index position of a target in a list if found, else it returns None.
    """

    for i in range(0, len(list)):
        if i == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the list")

"""
Below is a small code example to test the above linear_search algorithm
"""

numb = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numb, 12)
verify(result)

numb = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numb, 6)
verify(result)