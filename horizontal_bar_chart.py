import matplotlib.pyplot as plt

students = ["Aneeqa", "Sara", "Ali", "Zoya", "Ahmed"]
marks = [95, 88, 91, 72, 65]

plt.barh(students, marks)
for index, mark in enumerate(marks):
    plt.text(mark + 1, index, str(mark), va="center")

plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Student Marks Comparison")

plt.xlim(0,100)
plt.grid(axis="x")
plt.savefig("student_marks_horizontal_bar_chart.png")
plt.show()
