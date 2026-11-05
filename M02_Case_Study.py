# Name: Brianna Hubble
# File Name: M02_Case_Study.py
# Description: This app accepts student names and GPAs and determines whether each student qualifies for the Dean's List or Honor Roll.

while True:
    last_name = input("Enter student's last name (or ZZZ to quit): ")

    if last_name.upper() == "ZZZ":
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List!")

    if gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll!")

    if gpa < 3.25:
        print(first_name, last_name, "does not qualify for either list.")

    print()

print("Student record processing complete.")
