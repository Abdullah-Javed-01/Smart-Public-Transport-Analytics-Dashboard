import os
import pandas as pd

# -----------------------------
# Create Output Folder
# -----------------------------
os.makedirs("output/reports", exist_ok=True)

# -----------------------------
# Load Clean Dataset
# -----------------------------
df = pd.read_csv("output/cleaned_dataset.csv")

# -----------------------------
# Convert Date
# -----------------------------
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# Peak Travel Hour
# -----------------------------
# -----------------------------
# Peak Travel Hour
# -----------------------------
hourly_passengers = (
    df.groupby("Departure_Hour")["Passenger_Count"]
      .sum()
)

print(hourly_passengers)  # Optional: verify values

if hourly_passengers.empty:
    peak_hour = "N/A"
else:
    peak_hour = int(hourly_passengers.idxmax())

# -----------------------------
# KPI Calculations
# -----------------------------
total_passengers = df["Passenger_Count"].sum()

total_revenue = df["Ticket_Revenue_PKR"].sum()

average_daily_passengers = (
    df.groupby("Date")["Passenger_Count"].sum().mean()
)

average_delay = df["Delay_Minutes"].mean()

average_occupancy = df["Occupancy_Rate (%)"].mean()

trip_completion_rate = (
    (df["Trip_Status"] == "Completed").sum()
    / len(df)
) * 100

highest_revenue_route = (
    df.groupby("Route_Name")["Ticket_Revenue_PKR"]
      .sum()
      .idxmax()
)

lowest_revenue_route = (
    df.groupby("Route_Name")["Ticket_Revenue_PKR"]
      .sum()
      .idxmin()
)

peak_hour = (
    df.groupby("Departure_Hour")["Passenger_Count"]
      .sum()
      .idxmax()
)

most_crowded_route = (
    df.groupby("Route_Name")["Passenger_Count"]
      .sum()
      .idxmax()
)

average_fuel = df["Fuel_Consumption_Liters"].mean()

# -----------------------------
# KPI Table
# -----------------------------
kpis = pd.DataFrame({
    "KPI": [
        "Total Passengers",
        "Total Revenue (PKR)",
        "Average Daily Passengers",
        "Average Delay (Minutes)",
        "Average Occupancy (%)",
        "Trip Completion Rate (%)",
        "Highest Revenue Route",
        "Lowest Revenue Route",
        "Peak Travel Hour",
        "Most Crowded Route",
        "Average Fuel Consumption"
    ],
    "Value": [
        total_passengers,
        round(total_revenue, 2),
        round(average_daily_passengers, 2),
        round(average_delay, 2),
        round(average_occupancy, 2),
        round(trip_completion_rate, 2),
        highest_revenue_route,
        lowest_revenue_route,
        f"{peak_hour}:00",
        most_crowded_route,
        round(average_fuel, 2)
    ]
})

# -----------------------------
# Save KPIs
# -----------------------------
kpis.to_csv(
    "output/reports/kpi_summary.csv",
    index=False
)

# -----------------------------
# Print KPIs
# -----------------------------
print("=" * 60)
print("SMART PUBLIC TRANSPORT KPIs")
print("=" * 60)

print(kpis)

print("\nKPI Summary saved successfully!")