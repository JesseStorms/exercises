# Write your code here
def contains_duplicates(xs):
    xIndex=0
    for x in xs:
        yIndex=0
        for y in xs:
            if yIndex == xIndex:
                yIndex=+1
                continue
            if x == y:
                return True
            yIndex+=1
        xIndex+=1
    return False
# doesnt work wtf???
contains_duplicates([3, 6, 2, 1, 6])


# def contains_duplicates(xs):
#     for i in range(len(xs)):
#         for j in range(i + 1, len(xs)):
#             if xs[i] == xs[j]:
#                 return True

#     return False
