import re

def ten_or_more_abc(s):
    return re.fullmatch("(abc){10,}",s)