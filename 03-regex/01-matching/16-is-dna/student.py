# Write your code here
import re

def is_dna(s):
    return re.fullmatch("([GATC])*",s)