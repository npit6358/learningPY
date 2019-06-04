"""Problem 1 from Day01.docx
   Assuming you've already had your birthday this year."""

def year65(name: str, age: int) -> str:

    curYear = 2019
    yearsToGo = 65 - age
    bigYear = curYear + yearsToGo


    return "Hi, " + name + ".  " + "You turn 65 in the year " + str(bigYear) + "!"



