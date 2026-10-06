#scatter plot
import matplotlib.pyplot as pyplot
hours=[1,2,3,4,5,6,7,8]
scores=[10,20,30,40,50,60,70,80]
pyplot.scatter(hours,scores, color="red")
pyplot.title("Scatter Plot of Hours vs Scores")
pyplot.xlabel("Hours")
pyplot.ylabel("Scores")
pyplot.show()