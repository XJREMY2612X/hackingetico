students = [
    {"name": "Alice", "score": 8.5},
    {"name": "Bob", "score": 9.2},
    {"name": "Charlie", "score": 6.5},
    {"name": "Diana", "score": 9.5},
    {"name": "Eve", "score": 8.8},
    {"name": "Frank", "score": 9.1}
]

print(students[2])

for student in students:
    if student['score'] > 7.0:
        print(f"{student['name']}: The Student PASSED the course")
    else:
        print(f"{student['name']}: The student FAILED the course")