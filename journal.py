
records = [
    ["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
    ["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
    ["Jana", 94], ["Ziad", 75]
]


class_journal = {}
for name, grade in records:
    if name not in class_journal:
        class_journal[name] = []
    class_journal[name].append(grade)

for student, grades in class_journal.items():
    average = round(sum(grades) / len(grades), 2)
    print(f"{student}: Grades: {grades} | Average: {average}")


highest_avg = None
most_consistent = None
below_70 = []
total_grades = 0
all_grades = []

min_range = float('inf')
max_avg = -1
student_high_avg = ""
student_consistent = ""

for student, grades in class_journal.items():
    avg = sum(grades) / len(grades)
    grade_range = max(grades) - min(grades)
    total_grades += len(grades)
    all_grades.extend(grades)

    if avg > max_avg:
        max_avg = avg
        student_high_avg = student

    if grade_range < min_range:
        min_range = grade_range
        student_consistent = student

    if any(g < 70 for g in grades):
        below_70.append(student)

overall_avg = round(sum(all_grades) / len(all_grades), 2)

report = f"""
Highest average: {student_high_avg} ({round(max_avg, 2)})
Most consistent: {student_consistent} (range {min_range})
Students with at least one grade < 70: {', '.join(below_70)}
Total grades entered: {total_grades}
Overall class average: {overall_avg}
"""

print(report)


with open("class_report.txt", "w") as f:
    f.write(report)

new_grades = [["Jana", 99], ["Ziad", 78], ["Layla", 84]]

for name, grade in new_grades:
    if name not in class_journal:
        class_journal[name] = []
    class_journal[name].append(grade)
