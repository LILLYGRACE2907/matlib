import matplotlib.pyplot as pyplot
months=["January","February","March","April","May","June","July"]
sales=["$1000","$1500","$2000","$2500","$3000","$3500","$400"]
pyplot.bar(months, sales, color="blue")
pyplot.xlabel("months")
pyplot.ylabel("Sales")
pyplot.title("Monthly Sales Performance")
pyplot.show()