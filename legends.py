#legends
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], label='Line 1')
plt.plot([3, 2, 1], label='Line 2')
plt.title("Legend Example")
plt.legend()
plt.show()