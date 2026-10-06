import matplotlib.pyplot as pyplot
x=[2023,2024,2025,2026,2027]
y=[88, 92, 95, 97, 99]
pyplot.plot(x,y,linestyle="--", marker="s", color="green")
pyplot.title("sales performance")
pyplot.xlabel("Year")
pyplot.ylabel("Performance Score")
pyplot.grid("True")
pyplot.show()