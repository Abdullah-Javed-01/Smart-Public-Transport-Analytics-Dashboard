import pandas as pd
import os

# -----------------------------
# Load Dataset
# -----------------------------
file_path = "D:\\Work\\Internship\\TEYZIX\\Task-3_TC-INT-18991230-740\\Smart_Public_Transport_Analytics\\data\\pakistan_bus_transport_dataset.csv"

df = pd.read_csv(file_path)

print("="*50)
print("Dataset Loaded Successfully")
print("="*50)

print("\nShape:", df.shape)

# -----------------------------
# Check Missing Values
# -----------------------------
print("\nMissing Values")
print(df.isnull().sum())

# -----------------------------
# Check Duplicate Records
# -----------------------------
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

if duplicates > 0:
    df = df.drop_duplicates()

# -----------------------------
# Convert Date Column
# -----------------------------
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# -----------------------------
# Convert Time Columns
# -----------------------------
# Convert Departure Time
df["Departure_Hour"] = pd.to_datetime(
    df["Departure_Time"].astype(str),
    format="%H:%M",
    errors="coerce"
).dt.hour

# Replace invalid arrival times like "--:--"
df["Arrival_Time"] = df["Arrival_Time"].replace("--:--", pd.NA)

# Convert Arrival Time
df["Arrival_Hour"] = pd.to_datetime(
    df["Arrival_Time"].astype(str),
    format="%H:%M",
    errors="coerce"
).dt.hour

print("\nInvalid Departure Times:", df["Departure_Time"].isna().sum())
print("Invalid Arrival Times:", df["Arrival_Time"].isna().sum())
print(
    df[df["Arrival_Time"].isna()][
        ["Trip_ID", "Trip_Status", "Arrival_Time"]
    ].head()
)

# -----------------------------
# Correct Numeric Columns
# -----------------------------
numeric_cols = [
    "Scheduled_Duration_Minutes",
    "Actual_Duration_Minutes",
    "Delay_Minutes",
    "Passenger_Count",
    "Bus_Capacity",
    "Occupancy_Rate (%)",
    "Ticket_Fare_PKR",
    "Ticket_Revenue_PKR",
    "Fuel_Consumption_Liters"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# Remove Impossible Values
# -----------------------------
df = df[df["Passenger_Count"] <= df["Bus_Capacity"]]

df = df[df["Delay_Minutes"] >= 0]

# -----------------------------
# Recalculate Occupancy
# -----------------------------
df["Occupancy_Rate (%)"] = (
    df["Passenger_Count"] /
    df["Bus_Capacity"] * 100
).round(2)

# -----------------------------
# Save Clean Dataset
# -----------------------------
os.makedirs("output", exist_ok=True)

df.to_csv("output/cleaned_dataset.csv", index=False)

print("\nClean Dataset Saved!")

print("\nFinal Shape:", df.shape)

print("\nData Types")
print(df.dtypes)