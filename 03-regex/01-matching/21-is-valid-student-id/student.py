# Write your code here
import re

def is_valid_student_id(s):
    return re.fullmatch("^(s|S|r|R)+\d{7}",s)