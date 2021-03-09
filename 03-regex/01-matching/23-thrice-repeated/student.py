import re

def thrice_repeated(s):
    return re.fullmatch(r'(.+)\1\1',s)