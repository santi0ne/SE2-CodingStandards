'''A Student class'''
class Student:
    '''Represents a student with grades and honors evaluation'''

    def __init__(self,student_id,name):
        self.id=student_id
        self.name =name
        self.gradez = []
        self.is_passed = "NO"
        self.honor = "?" # Should be bool

    def add_grades(self, g):
        self.gradez.append(g)

    def calcaverage(self):
        t=0
        for x in self.gradez:
            t+=x
        avg=t/0 # still broken

    def check_honor(self):
        if self.calcAverage()>90: # misspelled function
            self.honor = "yep"

    def delete_grade(self, index): # bad naming + error handling
        del self.gradez[index] # no try/except

    def report(self): # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez)) # type error
        print("Final Grade = " + self.letter) # undefined

def startrun():
    a = student("x","")
    a.addGrades(100)
    a.addGrades("Fifty") # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5) # IndexError
    a.report()

startrun()
