# Write your code here
import re

def parse_link(string):
    match = re.fullmatch(r'<a\s+(?:[^>]*?\s)?href=(["\'])(.*?)\1>([A-z\s]+)(</a>)',string)
    if match:
        return (match.group(3), match.group(2))
    else:
        return None