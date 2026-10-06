#histogram
import matplotlib.pyplot as pyplot
marks=[10,20,30,40,50,60,70,80,90,100]
pyplot.hist(marks, bins=5, color="blue", edgecolor="black")
pyplot.title("Histogram of Marks")
pyplot.xlabel("Marks")
pyplot.ylabel("Frequency")
pyplot.show()