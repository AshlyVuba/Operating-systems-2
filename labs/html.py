#!/usr/bin/python

import cgitb
import cgi

cgitb.enable()

# Import the function to fetch student data
from your_module import fetch_students_data

# Get student data
students_data = fetch_students_data()

# Start printing HTML content
print("Content-Type: text/html")  # Set the content type
print()  # Blank line required, indicates the start of the HTML content

print('<script>')
print('var studentDetails = document.getElementById("student-details");')
if students_data is not None:
    for student in students_data:
        student_name = student.get("student_name", "")
        student_age = student.get("student_age", "")
        student_major = student.get("student_major", "")

        print(f'var studentInfo = document.createElement("p");')
        print(f'studentInfo.innerHTML = "<b>Student Name:</b> {student_name}, <b>Age:</b> {student_age}, <b>Major:</b> {student_major}";')
        print(f'studentDetails.appendChild(studentInfo);')
else:
    print('studentDetails.innerHTML = "No student data available.";')
print('</script>')
