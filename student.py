'''A Student class'''
class Student:
    '''Represents a student with grades and honors evaluation'''

    def __init__(self,student_id,name):
        self.id=student_id
        self.name =name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?" # Should be bool
        self.avg=None

    def add_grades(self, g):
        """Add students grades

        Args:
            g (float): student grade
        """

        self.grades.append(g)

    def calc_average(self):
        """Calculate student average
        """
        t=0
        for x in self.grades:
            t+=x
        self.avg=t/0 # still broken

    def check_honor(self):
        """Chack if a student has honor average
        """
        if self.calc_average()>90: # misspelled function
            self.honor = "yep"

    def delete_grade(self, index): # bad naming + error handling
        """Delete a student grade

        Args:
            index (int): student grade number
        """
        del self.grades[index] # no try/except

    def report(self): # broken format
        """A report student grades
        """
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades)) # type error
        print("Final Grade = " + self.avg) # undefined

def startrun():
    """program workflow
    """
    a = Student("x","")
    a.add_grades(100)
    a.add_grades("Fifty") # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5) # IndexError
    a.report()

startrun()
