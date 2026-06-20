import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
study_hours = [2, 3, 4, 3, 5]
sleep_hours = [8, 7, 7, 8, 6]
exercise_hours = [1, 1, 0.5, 1, 1.5]

plt.figure(figsize=(10, 8))
plt.plot(days, study_hours, marker="o", color="red", label="Study Hours")
plt.plot(days, sleep_hours, marker="s", color="blue", label="Sleep Hours")
plt.plot(days, exercise_hours, marker="^", color="green", label="Exercise Hours")

plt.xlabel("Days")
plt.ylabel("Hours")
plt.title("Study vs Sleep vs Exercise Hours")
plt.grid()
plt.legend()

plt.show()
