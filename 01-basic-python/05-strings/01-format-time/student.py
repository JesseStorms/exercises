# Write your code here
def format_time(h,m,s):
    def formatSingle(x):
        return str(x).rjust(2,'0')
    h = formatSingle(h)
    m = formatSingle(m)
    s = formatSingle(s)
    return f'{h}:{m}:{s}'
format_time(3,4,5)