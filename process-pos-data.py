from posclasses import *

myfile = open('demodata.csv', 'r')
# This file contains information about the plans of study of PhD students.
# Open the file to see the format. Each line is one course enrollment.
# Course enrollments are grouped by student, and separated by a line with "%%"
# The demo file (demodata.csv) contains information for 3 fake students.

# Make a list of students.
students = []

# Make a dictionary of courses.
# The dictionary keys will be the department and course number.
# For instance, "ENE69500"
courses = {}

# Read in the data file line by line.
for line in myfile:
    # If the line contains "%%", it indicates a new student.
    if "%%" in line:
        # Add a new student to the list of students.
        # The new student's ID number is that student's position in the list.
        students += [Student(len(students))]
    # Otherwise, the line represents a new course enrollment for
    # the newest student in the list of students (students[-1]).
    else:
        # Add that enrollment to the student's list of enrollments.
        students[-1].enrollments += [Enrollment(line)]
        # NOTE: We only care about Purdue courses for the course catalog.
        # However, we keep non-Purdue courses on a student's enrollments.
        # So, ONLY if the course is a Purdue course...
        if students[-1].enrollments[-1].institution == "PURDUE":
            # Check to see if that course already exists in the dict of courses.
            # We check uniqueness by coursestring.
            if students[-1].enrollments[-1].coursestring not in courses:
                # If it's not in the dict of courses, add it.
                courses[students[-1].enrollments[-1].coursestring] = []
                # TODO: This is a kludge that doesn't use the Course class.
                # We're simply using a dict with the coursestring as a key
                # and with values consisting of a list of students who've
                # taken the class. If you revisit this code, rewrite this.
            # Now add the student to that course.
            courses[students[-1].enrollments[-1].coursestring] += [students[-1]]

# TODO: Consider pickling the file upon completion.
