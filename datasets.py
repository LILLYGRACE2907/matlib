import matplotlib.pyplot as plt

class_a=[20,30,40,50,60,70]
class_b=[1,2,3,4,5,6]
plt.hist(class_a, bins=5, alpha=0.5, label="Class A") 
plt.hist(class_b, bins=5, alpha=0.5, label="Class B") 
plt.legend() 
plt.show()