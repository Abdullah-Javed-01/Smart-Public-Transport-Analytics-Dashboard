import pandas as pd
import os

# Load cleaned dataset
df = pd.read_csv("output/cleaned_dataset.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Date features
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()
df["Month_Number"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Weekday"] = df["Date"].dt.day_name()

# Revenue category
df["Revenue_Category"] = pd.cut(
    df["Ticket_Revenue_PKR"],
    bins=[0, 10000, 25000, 50000, 100000],
    labels=["Low", "Medium", "High", "Very High"]
)

# Delay category
df["Delay_Category"] = pd.cut(
    df["Delay_Minutes"],
    bins=[-1, 5, 15, 30, 60, 120],
    labels=["On Time", "Minor", "Moderate", "High", "Critical"]
)

# Occupancy category
df["Occupancy_Category"] = pd.cut(
    df["Occupancy_Rate (%)"],
    bins=[0, 40, 60, 80, 100],
    labels=["Low", "Medium", "High", "Full"]
)

os.makedirs("output/dashboard", exist_ok=True)

df.to_csv(
    "output/dashboard/dashboard_dataset.csv",
    index=False
)

print("Dashboard dataset exported successfully.")