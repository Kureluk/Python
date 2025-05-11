import numpy as np
import matplotlib.pyplot as plt




# 1
# x = np.linspace(-10, 10, 1000)
# y = x**2 * np.sin(x)

# plt.figure(figsize=(10, 6))
# plt.plot(x, y)
# plt.title('x^2 * sin(x)')
# plt.grid(True)
# plt.axhline(0, color='black', linewidth=0.5)
# plt.axvline(0, color='black', linewidth=0.5)
# plt.show()






# 2
# mean = 5     
# std_dev = 2   
# data = np.random.normal(loc=mean, scale=std_dev, size=1000)

# plt.figure(figsize=(10, 6))
# plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
# plt.grid(True)
# plt.show()





# 3
# y = np.array([50, 20, 25, 5])
# mylabels = ["Auto", "Bicycle", "Public transport", "Foot"]

# plt.pie(y, labels = mylabels)
# plt.show() 





# 4
# d_1 = np.random.normal(70, 10, 100)
# d_2 = np.random.normal(75, 7, 100)
# d_3 = np.random.normal(65, 12, 100)
# d = [d_1, d_2, d_3]

# fig = plt.figure(figsize =(10, 7))
# ax = fig.add_axes([0, 0, 1, 1])
# bp = ax.boxplot(d)

# plt.show()





# 5
# x = np.linspace(-10, 10, 1000)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.sin(x) + np.cos(x)

# plt.figure(figsize=(10, 6))

# plt.plot(x, y1, color='blue')
# plt.plot(x, y2, color='green')
# plt.plot(x, y3, color='red')

# plt.title('sin cos')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.grid(True)
# plt.axhline(0, color='black', linewidth=0.5)
# plt.axvline(0, color='black', linewidth=0.5)
# plt.legend()

# plt.show()





# 6

group_A = np.random.normal(loc=70, scale=10, size=100)
group_B = np.random.normal(loc=80, scale=5, size=100)
group_C = np.random.normal(loc=65, scale=15, size=100)

plt.figure(figsize=(8, 6))
plt.boxplot([group_A, group_B, group_C], labels=['group_A', 'group_B', 'group_C'])

plt.grid(True, axis='y')
plt.show()