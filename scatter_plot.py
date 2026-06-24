import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 65, 72, 85, 92]

plt.scatter(study_hours, marks, color="purple", s=100)
plt.plot(study_hours, marks, linestyle="--", color="gray")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Relationship Between Study Hours and Marks")
plt.savefig("study_hours_vs_marks_scatter.png")

plt.grid()
plt.show()
