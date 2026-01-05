def calculate_average(marks):
    return sum(marks) / len(marks)


def get_result(avg):
    if avg >= 75:
        return "Distinction"
    elif avg >= 60:
        return "First Class"
    elif avg >= 50:
        return "Second Class"
    else:
        return "Fail"


def analyze_student(student):
    marks = student["marks"]
    avg = calculate_average(marks)

    print("\nStudent Name:", student["name"])
    print("Marks:", marks)
    print("Average:", round(avg, 2))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
    print("Result:", get_result(avg))


# Sample student data
student_data = {
    "name": "Sandhya",
    "marks": [78, 65, 82, 70, 60]
}

analyze_student(student_data)
