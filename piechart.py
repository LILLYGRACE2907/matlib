#pie chart
import matplotlib.pyplot as pyplot
courses=["Python","Java","C++","JavaScript"]
students=[30,25,20,25]
pyplot.pie(students, labels=courses, autopct='%1.1f%%')
pyplot.title("Student Distribution by Course")
pyplot.show()

#explode a slice
pyplot.pie(students, labels=courses, autopct='%1.1f%%', explode=(0.1,0,0,0))
pyplot.title("Student Distribution by Course (Exploded Slice)")
pyplot.show()