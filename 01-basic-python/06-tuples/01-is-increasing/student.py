# Write your code here
def is_increasing(ns):
    tups = zip(ns,ns[1:])
    for thing in tups:
        if(thing[0]>thing[1]):
            return False
    return True