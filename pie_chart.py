import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "German", "College Work"]
hours = [6, 4, 2, 8]
plt.pie(
    hours,
    labels=subjects,
    autopct="%1.1f%%",
    explode=[0, 0, 0, 0.1]
)
plt.title("Weekly Study Time Distribution")
plt.axis("equal")
plt.savefig("weekly_study_time_pie_chart.png")

plt.show()
