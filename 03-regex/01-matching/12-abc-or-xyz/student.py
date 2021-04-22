# Write your code here
import re

def abc_or_xyz(s):
    return re.fullmatch("(abc)|(xyz)",s)