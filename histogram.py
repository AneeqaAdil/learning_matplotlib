import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 70, 75, 85, 90, 95, 78, 82, 67, 58, 73]

plt.hist(marks, bins=5, edgecolor="pink")

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")
plt.grid(axis="y")
plt.savefig("student_marks_histogram.png")

plt.show()
