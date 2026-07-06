# 🚌 Smart Public Transport Analytics Dashboard

A Business Intelligence project developed using **Python** and **Microsoft Power BI** to analyze public transport operations in Pakistan. The project transforms raw transportation data into actionable business insights through data preprocessing, exploratory analysis, KPI calculation, and an interactive Power BI dashboard.

---

## 📌 Project Overview

The Smart Public Transport Analytics Dashboard helps transport operators monitor operational performance, passenger demand, revenue generation, delays, occupancy, fuel consumption, and route efficiency.

The project follows a complete analytics workflow:

Raw Dataset → Data Cleaning → Exploratory Data Analysis → KPI Analysis → Dashboard Dataset Preparation → Power BI Dashboard → Business Insights

---

## 🎯 Objectives

- Analyze passenger demand across routes
- Monitor ticket revenue and route performance
- Measure operational KPIs
- Analyze delays caused by weather and traffic
- Evaluate bus occupancy and fuel consumption
- Provide interactive dashboards for decision-making

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Data preprocessing and analysis |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Microsoft Power BI | Dashboard development |
| Power Query | Data transformation |
| DAX | KPI calculations |
| Microsoft Excel (CSV) | Dataset storage |

---

# 📂 Project Structure

```text
TASK_3_TC-INT-18991230-740
│
├── dashboard
│   └── Smart_Public_Transport_Dashboard.pbix
│
├── data
│   ├── pakistan_bus_transport_dataset.csv
│   ├── cleaned_dataset.csv
│   └── dashboard_dataset.csv
│
├── output
│   ├── figures
│   └── reports
│
├── reports
│   ├── Smart_Public_Transport_Analytics_Report.docx
│   └── Smart_Public_Transport_Analytics_Report.pdf
│
├── screenshots
│   ├── Page 1.png
│   ├── Page 2.png
│   └── Page 3.png
│
├── scripts
│   ├── 01_data_cleaning.py
│   ├── 02_eda.py
│   ├── 03_kpi_analysis.py
│   └── 04_prepare_dashboard_data.py
│
├── README.md
└── requirements.txt
```

---

# 📊 Dataset

The project uses a synthetic Pakistan public transport dataset containing operational data for multiple cities, operators, routes, and bus types.

### Dataset Features

- Trip Information
- Route Details
- Passenger Count
- Ticket Revenue
- Bus Capacity
- Occupancy Rate
- Delay Duration
- Fuel Consumption
- Weather Condition
- Traffic Level
- Trip Status

---

# ⚙ Python Workflow

## Step 1 – Data Cleaning

Script:

```
scripts/01_data_cleaning.py
```

Tasks performed:

- Checked missing values
- Removed duplicate records
- Corrected data types
- Validated time columns
- Created new features
- Exported cleaned dataset

---

## Step 2 – Exploratory Data Analysis

Script:

```
scripts/02_eda.py
```

Analysis includes:

- Passenger distribution
- Revenue by route
- Delay analysis
- Fuel consumption
- Weather impact
- Correlation analysis

Charts are stored inside:

```
output/figures/
```

---

## Step 3 – KPI Analysis

Script:

```
scripts/03_kpi_analysis.py
```

Calculated KPIs include:

- Total Revenue
- Total Passengers
- Average Delay
- Average Occupancy
- Completion Rate
- Peak Travel Hour
- Highest Revenue Route
- Most Crowded Route
- Average Fuel Consumption

---

## Step 4 – Dashboard Dataset Preparation

Script:

```
scripts/04_prepare_dashboard_data.py
```

Prepares the final dataset for Power BI by creating calculated fields and ensuring compatibility with dashboard visuals.

---

# 📈 Power BI Dashboard

The dashboard consists of three interactive pages.

## 📄 Page 1 – Executive Summary

Features:

- KPI Cards
- Revenue by Route
- Passenger Trend
- Delay by Weather
- Trip Status Distribution
- Interactive Slicers

---

## 📄 Page 2 – Route Performance

Features:

- Route Revenue Analysis
- Passenger Analysis
- Delay by Route
- Fuel Consumption
- Occupancy Analysis
- Operator Performance

---

## 📄 Page 3 – Operations Analysis

Features:

- Peak Travel Hours
- Delay by Traffic Level
- Revenue by Departure City
- Passenger Distribution
- Bus Type Analysis
- Interactive Map Visualization

---

# ✨ Interactive Features

- KPI Cards
- Interactive Slicers
- Drill Down
- Drill Through
- Tooltips
- Cross Filtering
- Map Visual
- Navigation Buttons
- Dynamic Filtering

---

# 📊 Key Business Insights

- Lahore to Karachi generated the highest ticket revenue.
- Rawalpindi to Peshawar carried the highest number of passengers.
- Dust Storm conditions resulted in the highest average delays.
- Peak passenger demand occurred around 7 PM.
- Electric buses demonstrated lower fuel consumption.
- Completion rate remained above 87%, indicating strong operational reliability.

---

# 🚀 Future Improvements

- Real-time GPS integration
- Live dashboard refresh
- SQL database connectivity
- Predictive analytics
- Automated alerts using Power BI Service
- Cloud deployment
- Mobile dashboard support

---

# ▶ How to Run

### Install required libraries

```bash
pip install -r requirements.txt
```

### Run the Python scripts

```bash
python scripts/01_data_cleaning.py
python scripts/02_eda.py
python scripts/03_kpi_analysis.py
python scripts/04_prepare_dashboard_data.py
```

### Open Power BI Dashboard

Open:

```
dashboard/Smart_Public_Transport_Dashboard.pbix
```

using Microsoft Power BI Desktop.

---

# 📄 Project Report

The detailed project documentation is available in the **reports** folder.

---

# 👨‍💻 Author

**Abdullah Javed**

Data Analytics Intern

TEYZIX CORE Internship Program 2026

Reference ID:

**TC-INT-18991230-740**