# the program must process a list of student dictionaries (each with name and marks for three subjects),
# generate a grade and status for each student, and produce a full class summary report.

# 1. store at least 5 students as a list of dictionaries : [{name, maths, english, science}, ...]
# 2. use a loop to iterate over all over students and calculate each student's average
# 3. apply the grade/status logic from Unit 5 inside the loop
# 4. build a results list of dictionaries containing: name, average, status
# 5. after the main loop, calculate: class average, highest mark, lowest mark
# 6. display a formatted class report showing individual results and class statistics
# 7. use a while loop to let the user search for a student by name after the report is shown


# grade_report.py

# grade_report.py

# 1. Store at least 5 students as a list of dictionaries
students = [
    {"name": "Potso", "maths": 85, "english": 78, "science": 92},
    {"name": "Lerato", "maths": 67, "english": 74, "science": 58},
    {"name": "Tebogo", "maths": 45, "english": 39, "science": 55},
    {"name": "Lindiwe", "maths": 90, "english": 88, "science": 95},
    {"name": "Thandi", "maths": 52, "english": 61, "science": 47}
]

# Results list
results = []

# 2–3. Loop through students, calculate average, apply grade/status logic
for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "Pass" if average >= 50 else "Fail"

    # 4. Build results list
    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })

# 5. Class statistics
class_averages = [r["average"] for r in results]
class_average = sum(class_averages) / len(class_averages)
highest_mark = max(class_averages)
lowest_mark = min(class_averages)

# 6. Display formatted class report
print("\n--- Class Report ---")
for r in results:
    print(f"{r['name']}: Average={r['average']:.2f}, Grade={r['grade']}, Status={r['status']}")

print("\n--- Class Statistics ---")
print(f"Class Average: {class_average:.2f}")
print(f"Highest Average: {highest_mark:.2f}")
print(f"Lowest Average: {lowest_mark:.2f}")

# 7. Search for a student by name using while loop
while True:
    search_name = input("\nEnter a student name to search (or 'exit' to quit): ")
    if search_name.lower() == "exit":
        print("Exiting search.")
        break

    found = False
    for r in results:
        if r["name"].lower() == search_name.lower():
            print(f"Found: {r['name']} → Average={r['average']:.2f}, Grade={r['grade']}, Status={r['status']}")
            found = True
            break

    if not found:
        print("Student not found. Try again.")
