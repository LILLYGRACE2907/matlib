#annotations
import matplotlib.pyplot as plt 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
plt.annotate('Highest Sales', xy=(6, 4000), xytext=(4, 4500), arrowprops={"arrowstyle": "->", "color": "red"})
plt.show()