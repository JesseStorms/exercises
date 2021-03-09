# Write your code here
import re

def contains_no_a(s):
    return re.fullmatch(r'[^a]*',s)