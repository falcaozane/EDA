# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
data = pd.read_csv("shopping_trends.csv")

# %%
data.head()

# %%
data.info()

# %%
data.describe()

# %%
data.shape

# %%
data.isna().sum()

# %%
data.duplicated()

# %%
data.duplicated().sum()

# %%
data["Age"].plot(kind='hist')
plt.title("Histogram")


# %%
data.columns

# %%
data["Gender"].value_counts().plot(kind="bar")
plt.title("Barplot of Genger")
plt.show()

# %%
data.groupby("Category")["Purchase Amount (USD)"].mean()

# %%
data.groupby("Category")["Purchase Amount (USD)"].mean().sort_values(ascending=False)

# %%
data.groupby("Category")["Purchase Amount (USD)"].mean().sort_values(ascending=False).tail()

# %%
data.sort_values("Review Rating",ascending=False)

# %%
data.sort_values("Review Rating",ascending=False, inplace=True)

# %%
data["Subscription Status"].value_counts().plot(kind="pie")
plt.title("Pie chart of Subscription")
plt.show()

# %%
data["Color"].value_counts()

# %%
data["Color"].value_counts().head().plot(kind="pie")

# %%
data.plot(x="Previous Purchases", y="Review Rating", kind="scatter")
plt.title("Scatter plot - previous purchases review ratings")
plt.show()

# %%
data.head(10).plot(x="Previous Purchases", y="Review Rating", kind="scatter")
plt.title("Scatter plot - previous purchases review ratings")
plt.show()

# %%
data.head(75).plot(x="Previous Purchases", y="Review Rating", kind="scatter")
plt.title("Scatter plot - previous purchases review ratings")
plt.show()

# %%
pd.pivot_table(data, values="Purchase Amount (USD)", index="Location", columns="Item Purchased", aggfunc="mean")

# %%
pd.pivot_table(data, values="Purchase Amount (USD)", index="Location", columns="Item Purchased", aggfunc="mean").head()

# %%
data.groupby("Size")["Purchase Amount (USD)"].mean()

# %%
data.groupby("Payment Method")["Purchase Amount (USD)"].sum()

# %%
data.groupby("Discount Applied")["Review Rating"].mean()

# %%
data.groupby("Color")["Category"].value_counts()

# %%
data.groupby("Frequency of Purchases")["Previous Purchases"].median()

# %%
data.groupby("Season")["Review Rating"].mean()

# %%
data["Season"].value_counts().plot(kind="bar")
plt.xlabel("Season")
plt.ylabel("Count")
plt.title("Count of Purchases in each season")
plt.show()

# %%
data["Category"].value_counts().plot(kind="pie")
plt.title("Distribution of Purchases by Category")
plt.show()

# %%
data.boxplot(column="Review Rating", by="Gender")
plt.xlabel("Gender")
plt.ylabel("Review Rating")
plt.title("Review Rating Distribution By Gender")
plt.show()

# %%
data["Purchase Amount (USD)"].plot(kind="hist",bins=10)
plt.xlabel("USD")
plt.ylabel("Frequency")
plt.title("Histogram of Purchases Amount Distribution")
plt.show()

# %%
data.groupby("Color")["Review Rating"].mean().plot(kind="bar")
plt.xlabel("Color")
plt.ylabel("Mean Review Rating")
plt.title("Mean Review for each Color")
plt.show()

# %%
data.groupby("Payment Method")["Purchase Amount (USD)"].sum().plot(kind="pie")
plt.title("Sum of Purchase Amount by Payment Method")
plt.xlabel("")
plt.ylabel("")
plt.show()

# %%
data.boxplot(column="Purchase Amount (USD)", by="Frequency of Purchases")
plt.xlabel("Frequency of Purchases")
plt.ylabel("Purchase Amount (USD)")
plt.title("Purchase Amount Distribution by frequency of purchases")
plt.show()

# %%
data.groupby("Season")["Purchase Amount (USD)"].median().plot(kind="pie")
plt.xlabel("Season")
plt.ylabel("Sum of Purchases Amount (USD)")
plt.title("Sum of Purchase Amount by Season")
plt.show()

# %%
data.groupby("Season")["Purchase Amount (USD)"].mean().plot(kind="pie")
plt.xlabel("Season")
plt.ylabel("Sum of Purchases Amount (USD)")
plt.title("Sum of Purchase Amount by Season")
plt.show()

# %%
data.groupby("Season")["Purchase Amount (USD)"].max().plot(kind="pie")
plt.xlabel("Season")
plt.ylabel("Sum of Purchases Amount (USD)")
plt.title("Sum of Purchase Amount by Season")
plt.show()

# %%
data.groupby("Season")["Purchase Amount (USD)"].min().plot(kind="pie")
plt.xlabel("Season")
plt.ylabel("Sum of Purchases Amount (USD)")
plt.title("Sum of Purchase Amount by Season")
plt.show()


