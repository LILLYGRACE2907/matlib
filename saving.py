#saving charts
import matplotlib.pyplot as plt
months=["jan","feb","march","april"]
sales=[23,45,67,45]
plt.plot(months,sales)
plt.savefig("sales_chart.png")
plt.show()