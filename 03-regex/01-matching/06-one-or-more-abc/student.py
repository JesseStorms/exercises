# Write your code here
import re

def one_or_more_abc(s):
    return re.fullmatch("(abc)+",s)