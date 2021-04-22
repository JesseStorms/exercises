# Write your code here
import re

def zero_or_more_abc(s):
    return re.fullmatch("(abc)*",s)