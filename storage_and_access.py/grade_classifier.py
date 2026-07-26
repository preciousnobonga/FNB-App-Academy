# collect learner name and marks for three subjects (as floats) using input()
# calculate the average mark across the three subjects
# assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
# assign Pass status if the average is 50 or above, Fail otherwise
# flag any individual subject mark below 40 as 'needs intervention'
# display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags


# collect learner name and marks for three subjects as floats
learner_name = input("Enter your name: ")
subject1 = float(input("Enter mark for first subject: "))
subject2 = float(input("Enter mark for second subject: "))
subject3 = float(input("Enter mark for third subject: "))

# calculate the average mark across the three subjects
average_mark = (subject1 + subject2 + subject3) / 3

# assign a letter grade
if average_mark >= 80:
    grade = "A"
elif average_mark >= 70:
    grade = "B"
elif average_mark >= 60:
    grade = "C"
elif average_mark >= 50:
    grade = "D"
else:
    grade = "F"

# assign Pass/Fail status is avg is 50 or above
if average_mark >= 50:
    status = "Pass"
else:
    status = "Fail"

# flag any individual subject mark below 40 as 'needs intervention'
needs_intervention = False

if subject1 < 40 or subject2 < 40 or subject3 < 40:
    needs_intervention = True 


# display formatted report card
print("\n---Report Card ---")
print(f"Learner: {learner_name}")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Average: {average_mark}")
print(f"Grade: {grade}")
print(f"Status: {status}")

if needs_intervention:
    print("Needs Intervention")
else:
    print("No Intervention Required")
