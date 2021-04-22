# Write your code here
def slug(name):
    namearr = name.split(' ')
    fnam = namearr[0]
    lnam = namearr[1:]
    return '-'.join(s.lower() for s in lnam + [fnam])