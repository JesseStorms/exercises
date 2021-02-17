# Write your code here
def from_lists(keys,vals):
    res = {}
    for(x,y) in zip(keys,vals):
        res[x]=y
    return res