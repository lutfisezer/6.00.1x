"""
------------------------------------------------------------------------------------------------------------------------
Problem 5
10.0/10.0 points (graded)

Write a Python function that returns the sum of the pairwise products of listA and listB.
You should assume that listA and listB have the same length and are two lists of integer numbers.
For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6,
meaning your function should return: 32

Hint: You will need to traverse both lists in parallel.

This function takes in two lists of numbers and returns a number.

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
------------------------------------------------------------------------------------------------------------------------
"""


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    from operator import mul
    return sum(map(mul, listA, listB))


### Test ###


print(dotProduct([1, 2, 3], [4, 5, 6]))                                                                 # returns 32
print(dotProduct([-38, 77, -98, 13, -82, -70, 26], [-50, 49, 41, 39, 40, -14, 33]))                     # returns 720
print(dotProduct([-99, 26, 16, 29, 49, -69, -40, 79, 12], [-74, 10, 70, -43, 28, -92, 59, -65, 25]))    # returns 7984
