# Write your code here
def format_grades(grades):
    def getAvg(ar):
        return round(sum(ar)/len(ar))
    return "\n".join(f'{name}: {getAvg(grades)}' for name, grades in grades.items())