"""
------------------------------------------------------------------------------------------------------------------------
Problem 6
15.0/15.0 points (graded)

Implement a function that meets the specifications below.

def deep_reverse(L):
    '''
    assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    '''
    # Your code here

For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
------------------------------------------------------------------------------------------------------------------------
"""


def deep_reverse(L):
    """
    assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    for lis in L:
        lis.reverse()
    L.reverse()


### Test ###


L1 = [[1, 2], [3, 4], [5, 6, 7]]
L2 = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L1)
deep_reverse(L2)
print(L1)
print(L2)
