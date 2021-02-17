# Write your code here
def remove_duplicates(xs):
    seen = set()
    res = []
    for thing in xs:
        if thing not in seen:
            seen.add(thing)
            res.append(thing)
    return res