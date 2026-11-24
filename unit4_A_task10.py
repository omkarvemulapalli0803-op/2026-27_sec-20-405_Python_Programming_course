students = [
    {"name": "Omkar", "marks": 90},
    {"name": "Rahul", "marks": 75},
    {"name": "Ram", "marks": 85}
]

print(sorted(students, key=lambda x: x["marks"]))
print(sorted(students, key=lambda x: x["marks"], reverse=True))