"""
def TreeSearch(x,k):
    if x == None or k == key[x]:
        return x
    if k < key[x]:
        return TreeSearch(left[x], k)
    else:
        return TreeSearch(right[x],k)

def IterativeTreeSearch(x,k):
    while x!=None and k!=key[x]:
        if k<key[x]:
            x=left[x]
        else:x=right[x]
    return x

def TreeMinimum(x):
    while left[x]!=None:
        x=left[x]
    return x

def TreeMaximum(x):
    while left[x]!=None:
        x=right[x]
    return x

def TreeSuccessor(x):
    if right[x]!=None:
        return TreeMinimum(right[x])
    y=parent[x]
    while y!=None and x == right[y]:
        x=y
        y=parent[y]
    return y
"""
