# Write your code here
def frequencies(xs):
    res = {}
    for thing in xs:
        if(thing not in res):
            res[thing] = 1
        else:
            res[thing] += 1
    return res

frequencies([1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1])