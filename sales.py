import matplotlib.pyplot as pyplot
months=["January","February","March","April","May","June","July"]
sales=["$1000","$1500","$2000","$2500","$3000","$3500","$400"]
pyplot.plot(months, sales, marker="o")
pyplot.xlabel("Months")
pyplot.ylabel("Sales")
pyplot.title("Monthly Sales Performance")
pyplot.legend(["Sales"])
pyplot.show()