# Write your code here

import re


def ababa(s):
    return re.fullmatch(r'(.+)(.+)\1\2\1',s)