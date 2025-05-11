import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y = x**2 * np.sin(x)

plt.plot(x, y)
plt.title("Графік функції: x^2 * sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()


data = np.random.normal(loc=5, scale=2, size=1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title("Гістограма нормального розподілу (μ=5, σ=2)")
plt.xlabel("Значення")
plt.ylabel("Частота")
plt.grid(True)
plt.show()



hobbies = ['Читання', 'Програмування', 'Спорт', 'Музика', 'Подорожі']
shares = [20, 30, 15, 25, 10]

plt.pie(shares, labels=hobbies, autopct='%1.1f%%', startangle=140)
plt.title("Розподіл часу між хобі")
plt.axis('equal')
plt.show()



fruit_names = ['Яблука', 'Банани', 'Апельсини', 'Груші']
fruit_data = [np.random.normal(loc=150, scale=10, size=100),
              np.random.normal(loc=120, scale=15, size=100),
              np.random.normal(loc=160, scale=12, size=100),
              np.random.normal(loc=140, scale=8, size=100)]

plt.boxplot(fruit_data, labels=fruit_names)
plt.title("Box-Plot маси фруктів (грам)")
plt.ylabel("Маса (г)")
plt.grid(True)
plt.show()




x = np.random.uniform(0, 1, 100)
y = np.random.uniform(0, 1, 100)

plt.scatter(x, y, color='green', alpha=0.6)
plt.title("Точкова діаграма")
plt.xlabel("X координата")
plt.ylabel("Y координата")
plt.grid(True)
plt.show()




x = np.linspace(0, 10, 500)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='orange')
plt.plot(x, y3, label='sin(x) * cos(x)', color='green')

plt.title("Графіки трьох функцій")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
