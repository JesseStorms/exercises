# Write your code here
import re

def only_digits(s):
    return re.fullmatch("[0-9]*",s)