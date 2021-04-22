# Write your code here
import re

def contains_three_digits(s):
    return re.fullmatch(".*\d.*\d.*\d.*",s)