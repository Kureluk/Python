import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

x = np.linspace(-20, 20, 400).reshape(-1, 1)
y_true = np.sin(x) + 0.1 * x**2

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=5)
x_poly = poly.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, y_true)
y_pred = model.predict(x_poly)

mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)

plt.figure(figsize=(10, 6))
plt.plot(x, y_true, label='Реальна функція', color='blue')
plt.plot(x, y_pred, label='Передбачення моделі', color='red', linestyle='--')
plt.title('Порівняння реальної та передбаченої функції')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show(), mae, mse
