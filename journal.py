
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
