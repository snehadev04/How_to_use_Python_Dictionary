# Student scores dictionary with student names as keys and their scores as values
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Dictionary to store student grades
student_grades = {}

# Loop through each student in the student_scores dictionary
for student in student_scores:
  # Get the score of the current student
  score = student_scores[student]

  # Assign grades based on score ranges
  if 91 <= score <= 100: 
    student_grades[student] = "Outstanding"
  elif 81 <= score <= 90:
    student_grades[student] = "Exceeds Expectations"
  elif 71 <= score <= 80:
    student_grades[student] = "Acceptable"
  elif score <= 70:
    student_grades[student] = "Fail"

# Print the student grades
print(student_grades)
