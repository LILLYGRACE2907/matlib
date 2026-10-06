#area chart
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500]
plt.fill_between(months, sales, color="skyblue", alpha=0.5)
plt.plot(months, sales, color="Slateblue", alpha=0.6, linewidth=2)
plt.title("Monthly Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()