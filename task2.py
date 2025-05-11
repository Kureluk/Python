import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("cars_plus.csv")


features = ['brand', 'model', 'year', 'engine_volume', 'mileage', 'horsepower']
target = 'price'
X = df[features]
y = df[target]


X_encoded = pd.get_dummies(X, columns=['brand', 'model'], drop_first=True)


X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mape = mean_absolute_percentage_error(y_test, y_pred) * 100
print(f"\nMAPE (середня абсолютна відносна помилка): {mape:.2f}%")


your_car = pd.DataFrame([{
    'brand': 'Toyota',
    'model': 'Corolla',
    'year': 2019,
    'engine_volume': 1.6,
    'mileage': 70,
    'horsepower': 132
}])


your_car_encoded = pd.get_dummies(your_car, columns=['brand', 'model'])
your_car_encoded = your_car_encoded.reindex(columns=X_encoded.columns, fill_value=0)


predicted_price = model.predict(your_car_encoded)[0]
print(f"\nПрогнозована ціна авто: {predicted_price:,.2f} грн")


plt.figure(figsize=(10,6))
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')
plt.xlabel("Справжня ціна")
plt.ylabel("Прогнозована ціна")
plt.title("Справжня vs Прогнозована ціна")
plt.grid(True)
plt.tight_layout()
plt.show()
