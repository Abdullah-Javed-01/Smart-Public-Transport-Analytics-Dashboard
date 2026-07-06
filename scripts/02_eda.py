import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Create output folder
# -----------------------------
os.makedirs("output/figures", exist_ok=True)

# -----------------------------
# Load Clean Dataset
# -----------------------------
df = pd.read_csv("output/cleaned_dataset.csv")

print("=" * 60)
print("Exploratory Data Analysis")
print("=" * 60)

# -----------------------------
# Statistical Summary
# -----------------------------
print("\nStatistical Summary")
print(df.describe())

# -----------------------------
# Total Passengers by Route
# -----------------------------
route_passengers = (
    df.groupby("Route_Name")["Passenger_Count"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(12,6))
route_passengers.plot(kind="bar")
plt.title("Total Passengers by Route")
plt.xlabel("Route")
plt.ylabel("Passengers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/figures/passengers_by_route.png")
plt.close()

# -----------------------------
# Revenue by Route
# -----------------------------
route_revenue = (
    df.groupby("Route_Name")["Ticket_Revenue_PKR"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(12,6))
route_revenue.plot(kind="bar")
plt.title("Revenue by Route")
plt.xlabel("Route")
plt.ylabel("Revenue (PKR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/figures/revenue_by_route.png")
plt.close()

# -----------------------------
# Trip Status Distribution
# -----------------------------
trip_status = df["Trip_Status"].value_counts()

plt.figure(figsize=(6,6))
trip_status.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Trip Status Distribution")
plt.tight_layout()
plt.savefig("output/figures/trip_status.png")
plt.close()

# -----------------------------
# Weather Condition
# -----------------------------
weather = df["Weather_Condition"].value_counts()

plt.figure(figsize=(8,5))
weather.plot(kind="bar")
plt.title("Trips by Weather Condition")
plt.xlabel("Weather")
plt.ylabel("Trips")
plt.tight_layout()
plt.savefig("output/figures/weather.png")
plt.close()

# -----------------------------
# Delay Distribution
# -----------------------------
plt.figure(figsize=(10,5))
plt.hist(df["Delay_Minutes"], bins=20)
plt.title("Delay Distribution")
plt.xlabel("Delay (Minutes)")
plt.ylabel("Number of Trips")
plt.tight_layout()
plt.savefig("output/figures/delay_distribution.png")
plt.close()

# -----------------------------
# Passenger Distribution
# -----------------------------
plt.figure(figsize=(10,5))
plt.hist(df["Passenger_Count"], bins=20)
plt.title("Passenger Distribution")
plt.xlabel("Passengers")
plt.ylabel("Trips")
plt.tight_layout()
plt.savefig("output/figures/passenger_distribution.png")
plt.close()

# -----------------------------
# Fuel Consumption by Bus Type
# -----------------------------
fuel = (
    df.groupby("Bus_Type")["Fuel_Consumption_Liters"]
      .mean()
)

plt.figure(figsize=(8,5))
fuel.plot(kind="bar")
plt.title("Average Fuel Consumption by Bus Type")
plt.xlabel("Bus Type")
plt.ylabel("Fuel (Liters)")
plt.tight_layout()
plt.savefig("output/figures/fuel_bus_type.png")
plt.close()

# -----------------------------
# Average Delay by Traffic
# -----------------------------
traffic_delay = (
    df.groupby("Traffic_Level")["Delay_Minutes"]
      .mean()
)

plt.figure(figsize=(6,5))
traffic_delay.plot(kind="bar")
plt.title("Average Delay by Traffic Level")
plt.xlabel("Traffic Level")
plt.ylabel("Delay (Minutes)")
plt.tight_layout()
plt.savefig("output/figures/traffic_delay.png")
plt.close()

# -----------------------------
# Correlation Matrix
# -----------------------------
numeric = df.select_dtypes(include=["int64", "float64"])

corr = numeric.corr()

plt.figure(figsize=(10,8))
plt.imshow(corr)
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("output/figures/correlation_matrix.png")
plt.close()

# -----------------------------
# Business Insights
# -----------------------------
print("\nBusiness Insights")
print("-" * 40)

print("Highest Revenue Route:")
print(route_revenue.idxmax())

print("\nMost Crowded Route:")
print(route_passengers.idxmax())

print("\nAverage Delay:")
print(round(df["Delay_Minutes"].mean(),2),"minutes")

print("\nTotal Revenue:")
print(f"PKR {df['Ticket_Revenue_PKR'].sum():,.0f}")

print("\nTotal Passengers:")
print(df["Passenger_Count"].sum())

print("\nTrip Completion Rate:")
completed = (
    (df["Trip_Status"]=="Completed").sum()/len(df)
)*100

print(f"{completed:.2f}%")

print("\nEDA Completed Successfully!")