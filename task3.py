import pandas as pd
import matplotlib.pyplot as plt

data = {
    "OrderID": [1, 2, 3, 4, 5, 6],
    "Customer": ["Ivanov", "Petrenko", "Sydorenko", "Ivanov", "Petrenko", "Melnyk"],
    "OrderDate": ["2023-06-04", "2023-06-05", "2023-06-07", "2023-06-09", "2023-06-11", "2023-06-10"],
    "Product": ["Laptop", "Tablet", "Phone", "Monitor", "Tablet", "Laptop"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics"],
    "Quantity": [1, 2, 1, 1, 3, 1],
    "Price": [1000, 300, 800, 200, 300, 1200]
}

df = pd.DataFrame(data)
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

df["TotalAmount"] = df["Quantity"] * df["Price"]

total_income = df["TotalAmount"].sum()

average_total = df["TotalAmount"].mean()

orders_per_customer = df["Customer"].value_counts()

orders_over_500 = df[df["TotalAmount"] > 500]

sorted_df = df.sort_values(by="OrderDate", ascending=False)

filtered_by_date = df[(df["OrderDate"] >= "2023-06-05") & (df["OrderDate"] <= "2023-06-10")]

category_grouped = df.groupby("Category").agg({
    "Quantity": "sum",
    "TotalAmount": "sum"
})

top_customers = df.groupby("Customer")["TotalAmount"].sum().nlargest(3)


orders_by_date = df["OrderDate"].value_counts().sort_index()
orders_by_date.plot(kind="line", marker="o", title="Кількість замовлень по датах")
plt.xlabel("Дата")
plt.ylabel("Кількість замовлень")
plt.grid(True)
plt.show()

category_grouped["TotalAmount"].plot(kind="pie", autopct="%1.1f%%", title="Розподіл доходів по категоріях")
plt.ylabel("")  
plt.show()
