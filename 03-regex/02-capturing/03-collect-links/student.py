# Write your code here
import re
def collect_link(string):
       return re.findall(r'<a\s+(?:[^>]*?\s)?href=(["\'])(.*?)\1>([A-z\s]+)(</a>)',string)
