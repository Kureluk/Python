import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("Energy_Consumption_by_Month.csv")

month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}
df['month_num'] = df['month'].map(month_map)
df = df.dropna()

X = df[['month_num']].values
y = df['consumption_kwh'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = MLPRegressor(hidden_layer_sizes=(10,), max_iter=100000, random_state=42)
model.fit(X_scaled, y)
y_pred = model.predict(X_scaled)

print("MAE:", mean_absolute_error(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))

plt.figure(figsize=(10, 6))
plt.plot(df['month_num'], y, label='Фактичне споживання', marker='o')
plt.plot(df['month_num'], y_pred, label='Прогноз моделі', marker='x')
plt.xticks(ticks=range(1, 13), labels=[k for k, v in sorted(month_map.items(), key=lambda x: x[1])])
plt.title("Передбачення споживання електроенергії за місяцями")
plt.xlabel("Місяць")
plt.ylabel("Споживання (кВт·год)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
