# Write your code here

import re


def twice_repeated(s):
    return re.fullmatch(r'(.)\1',s)