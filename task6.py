from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

minutes = np.arange(0, 24 * 60).reshape(-1, 1)


noise = np.random.normal(0, 2, size=minutes.shape)
trip_duration = 20 + 10 * np.sin((minutes - 420) / 1440 * 2 * np.pi) + noise

poly2 = PolynomialFeatures(degree=4)
minutes_poly = poly2.fit_transform(minutes)
poly_model = LinearRegression()
poly_model.fit(minutes_poly, trip_duration)
trip_pred_poly = poly_model.predict(minutes_poly)


scaler = StandardScaler()
minutes_scaled = scaler.fit_transform(minutes)
mlp = MLPRegressor(hidden_layer_sizes=(20, 10), max_iter=1000, random_state=1)
mlp.fit(minutes_scaled, trip_duration.ravel())
trip_pred_mlp = mlp.predict(minutes_scaled)


mae_poly = mean_absolute_error(trip_duration, trip_pred_poly)
mse_poly = mean_squared_error(trip_duration, trip_pred_poly)
mae_mlp = mean_absolute_error(trip_duration, trip_pred_mlp)
mse_mlp = mean_squared_error(trip_duration, trip_pred_mlp)


def time_to_minutes(h, m):
    return h * 60 + m

test_times = np.array([
    [time_to_minutes(10, 30)],
    [time_to_minutes(0, 0)],
    [time_to_minutes(2, 40)],
])
test_times_poly = poly2.transform(test_times)
test_times_scaled = scaler.transform(test_times)

pred_poly = poly_model.predict(test_times_poly)
pred_mlp = mlp.predict(test_times_scaled)


plt.figure(figsize=(12, 6))
plt.plot(minutes, trip_duration, label='Реальні значення', alpha=0.6)
plt.plot(minutes, trip_pred_poly, label='Поліноміальна регресія', linestyle='--')
plt.plot(minutes, trip_pred_mlp, label='Нейронна модель', linestyle='-.')
plt.title('Передбачення тривалості поїздки в залежності від часу')
plt.xlabel('Хвилини від півночі')
plt.ylabel('Тривалість поїздки (хв)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

(pred_poly, pred_mlp), (mae_poly, mse_poly), (mae_mlp, mse_mlp)
