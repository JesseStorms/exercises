# Write your code here
import re

def is_number(s):
    return re.fullmatch("[0-9]+(\.[0-9]+)?",s)