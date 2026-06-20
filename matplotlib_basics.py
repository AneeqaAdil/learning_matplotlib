import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
study_hours = [2, 3, 4, 3, 5]

plt.plot(
    days,
    study_hours,
    marker="o",
    linestyle="--",
    color="purple",
    label="Study Hours"
)

plt.xlabel("Days")
plt.ylabel("Study Hours")
plt.title("My Study Hours Progress")
plt.grid()
plt.legend()

plt.savefig("study_hours_progress.png")
plt.show()
