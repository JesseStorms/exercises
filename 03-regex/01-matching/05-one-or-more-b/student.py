# Write your code here
import re

def one_or_more_b(s):
    return re.fullmatch("b+",s)