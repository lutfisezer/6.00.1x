L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
bList = []

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    copy = aList[:]
    for i in aList:
        if type(i) == list:
            flatten(i)
        else:
            bList.append(copy.pop(copy.index(i)))
    return bList


print(flatten(L))
