# Write your code here
import re

def one_or_more_a(s):
    return re.fullmatch("a+",s)