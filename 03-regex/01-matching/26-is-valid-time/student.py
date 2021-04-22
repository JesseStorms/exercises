# Write your code here
import re

def is_valid_time(s):
    return re.fullmatch(r'([0-2]+[0-9]+:)([0-5]+[0-9]+:)([0-5]+[0-9])(\.\d{3})?',s)