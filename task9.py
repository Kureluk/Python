import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

data = pd.concat([train_data, test_data], sort=False)

data['Age'].fillna(data['Age'].median(), inplace=True)
data['Fare'].fillna(data['Fare'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

label_encoders = {}
for col in ['Sex', 'Embarked']:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = data[features]

X_train = X[:len(train_data)]
y_train = train_data['Survived']
X_test = X[len(train_data):]

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = Sequential([
    Dense(32, input_dim=X_train_scaled.shape[1], activation='relu'),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid') 
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train_scaled, y_train, epochs=100, batch_size=16, verbose=1, validation_split=0.2)


predictions = model.predict(X_test_scaled)
predicted_classes = (predictions > 0.5).astype(int).flatten()


submission = pd.DataFrame({
    "PassengerId": test_data["PassengerId"],
    "Survived": predicted_classes
})
submission.to_csv("submission.csv", index=False)
