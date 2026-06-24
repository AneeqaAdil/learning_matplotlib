import matplotlib.pyplot as plt

students = ["Aneeqa", "Sara", "Ali", "Zoya", "Ahmed"]
marks = [95, 88, 91, 72, 65]

plt.bar(students, marks, color="skyblue")
for index, mark in enumerate(marks):
    plt.text(index, mark + 1, str(mark), ha="center")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")
plt.grid(axis="y")
plt.savefig("student_marks_bar_chart.png")
plt.ylim(0, 100)
plt.show()
