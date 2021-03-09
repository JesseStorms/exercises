# Write your code here
import re

def ten_times_abc(s):
    return re.fullmatch("(abc){10}",s)