"""
------------------------------------------------------------------------------------------------------------------------
Problem 9
15.0/15.0 points (graded)

Write a function to flatten a list. The list contains other lists, strings, or ints.
For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''

Paste your entire function, including the definition, in the box below.
Do not leave any debugging print statements. Note that we ask you to write a function only
-- you cannot rely on any variables defined outside your function for your code to work correctly.
------------------------------------------------------------------------------------------------------------------------
"""


def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    bList = []
    if type(aList) == list:
        for i in aList:
            bList.extend(flatten(i))
    else:
        bList.append(aList)
    return bList


### Test ###


aList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(aList))
