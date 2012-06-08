class Student:
    """The plan of study for an individual student"""
    def __init__(self, posid):
        self.posid = posid
        self.enrollments = []

class Enrollment:
    """A course entered into a student's plan of study"""
    def __init__(self, enrollmentstring):
        """Create a new enrollment from an enrollment string.
        Here's a sample enrollment string:
        PRIMARY,EXPERIMENTAL STAT I,STAT,501,3,RE,-,-,Dec 2007
        The variables, in order:
        * primary
        * title, department, course number, credits (course string)
        * regular
        * masters
        * institution
        * date
        """
        # the variables are comma-delimited. Split them.
        enrollmentvars = enrollmentstring.split(',')

        # Is the course primary (True) or secondary (False)?
        if "PRIMARY" in enrollmentvars[0]:
            self.primary = True     # Primary course
        else:
            self.primary = False    # Secondary course

        # Create a course string with the relevant info.
        # TODO: This is terribly inefficient. Fix it.
        self.coursestring = enrollmentvars[1] + ',' + enrollmentvars[2] + ',' + enrollmentvars[3] + ',' + enrollmentvars[4]

        # Is the course regular or transfer?
        if "RE" in enrollmentvars[5]:
            self.regular = True     # Regular hours
        else:
            self.regular = False    # Transfer hours
        
        # Was the course used for a Masters degree?
        if "YES" in enrollmentvars[6]:
            self.masters = True     # From a MA/MS
        else:
            self.masters = False    # Not from a MA/MS

        # Is the course from Purdue?
        if '-' == enrollmentvars[7]:
            self.institution = "PURDUE"
        else:
            self.institution = enrollmentvars[7]

        # When was it taken?
        # TODO: Standardize and encode in YYYYMMDD format.
        self.date = enrollmentvars[8]

class Course:
    """A course entered in a student's plan of study"""
    def __init__(self, title, dept, courseno, numcredits):
        """Create a new course."""
        # a dictionary where the keys are the semesters the course
        # was taken, and the values assigned to those keys are
        # lists of students who were enrolled in the course
        # during that particular semester
        self.studentsenrolled = {} 
        
        # attributes for the course that are the same for all students
        self.title = title
        self.dept = dept
        self.courseno = int(courseno)
        self.numcredits = int(numcredits)

    def addstudent(self, student, date):
        """Add a student to the list of students who've enrolled in
        this course, keeping track of when they took it"""
        # if this is the first student who's taken the class
        # during that particular term, initialize that term
        if date not in self.studentsenrolled.keys():
            self.studentsenrolled[date] = []

        # add the student to the list of students enrolled that term
        self.studentsenrolled[date] += [student]

    def allstudentsenrolled(self):
        """Return a list of all the students ever enrolled in the course
        without regard to when they took it. Note that if a student took
        the course more than once (for instance, ENE 590), they will appear 
        multiple times in thelist that is returned. Therefore, the length 
        of this list is an accurate count of how many times this course has 
        been taken. If you remove redundant items from the list returned
        here, you'll get the number of unique students who've taken it."""
        students = []
        for key in self.studentsenrolled:
            students += self.studentsenrolled[key]
        return students
