# Student Result Analyzer - Menu Driven with Rank List

students = []

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    m1 = int(input("Enter marks for Subject 1: "))
    m2 = int(input("Enter marks for Subject 2: "))
    m3 = int(input("Enter marks for Subject 3: "))

    total = m1 + m2 + m3
    average = total / 3
    grade = calculate_grade(average)
    result = "Pass" if average >= 60 else "Fail"

    student = {
        "roll": roll,
        "name": name,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    }

    students.append(student)
    print("Student record added successfully!\n")

def display_students():
    if not students:
        print("No records found.\n")
        return

    print("\nRoll  Name   Total  Average  Grade  Result")
    print("-" * 50)
    for s in students:
        print(f"{s['roll']}  {s['name']}  {s['total']}  {s['average']:.2f}  {s['grade']}  {s['result']}")
    print()

def generate_rank_list():
    if not students:
        print("No records to rank.\n")
        return

    ranked = sorted(students, key=lambda x: x["total"], reverse=True)

    print("\nRank  Roll  Name   Total")
    print("-" * 30)
    rank = 1
    for s in ranked:
        print(f"{rank}  {s['roll']}  {s['name']}  {s['total']}")
        rank += 1
    print()

def class_statistics():
    if not students:
        print("No data available.\n")
        return

    total_marks = sum(s["total"] for s in students)
    class_avg = total_marks / len(students)
    topper = max(students, key=lambda x: x["total"])

    print("\nClass Statistics")
    print("----------------")
    print(f"Class Average Marks: {class_avg:.2f}")
    print(f"Topper: {topper['name']} (Total: {topper['total']})\n")

def menu():
    while True:
        print("Student Result Analyzer")
        print("1. Add Student")
        print("2. Display All Results")
        print("3. Generate Rank List")
        print("4. Class Statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            generate_rank_list()
        elif choice == "4":
            class_statistics()
        elif choice == "5":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
