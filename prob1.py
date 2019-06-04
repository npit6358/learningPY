"""Problem 1 from Day01.docx"""

print("Hello.  Please enter your name, then your current age\
 and I'll tell you when the government pretends you get to retire.")


def year65(name: str, age: int) -> str:

    curYear = 2019
    yearsToGo = 65 - age
    bigYear = curYear + yearsToGo
    
    return "Hi, " + name + ".  " + "You turn 65 in the year " + bigYear + "!"



