# Write your code here
# Write your code here
import re

def two_or_more_abc(s):
    return re.fullmatch("(abc){2,}",s)