# 🍽️ Zomato Restaurant Data Analysis using Python

## 📌 Project Overview

This project performs **real-time visual data analysis** on Zomato restaurant data using **Python**. It uncovers customer behavior patterns such as online vs. offline orders, preferred price ranges, and the most popular cuisine types based on ratings.

---

## 🛠️ Technologies Used

- Python
- Pandas (for data manipulation)
- Matplotlib & Seaborn (for data visualization)
- CSV (Zomato dataset)

---

## 🧠 Key Highlights

- 📊 **Visual Insights** from raw restaurant data
- 🧹 **Data Cleaning & Preprocessing** before analysis
- 📍 Offline script: runs on **local system**, no internet required
- 🔁 Automated analysis with **exception handling**

---

## 🎯 Features

### ✅ 1. **Online vs Offline Orders**
- Pie chart visualization of how many restaurants provide online order services.
- Helps understand user preferences and digital adoption.

### ✅ 2. **Price Range Preference**
- Analyzes and visualizes which price ranges are most popular based on:
  - Average cost for two people
  - Rating multiplied by number of reviews
- Bar chart with average rating and total score.

### ✅ 3. **Popular Cuisine Types**
- Identifies most favored cuisine categories based on:
  - Number of user ratings received.
- Bar chart showcasing top 15 cuisines.

---

## 🧹 Data Preprocessing

- Dropped null or irrelevant values from critical columns
- Converted numeric columns to appropriate types
- Handled missing or malformed data
- Removed outliers using defined conditions (e.g., cost between ₹0–6000)

---

## 🧾 Input Dataset

**File Name**: `zomato.csv`  
**Source**: Manually downloaded  
**Important Columns**:
- `online_order`
- `avg cost (two people)`
- `rate (out of 5)`
- `num of ratings`
- `cuisines type`

---

## 📊 Sample Visualizations

### 🍽️ Online vs Offline Orders
- Pie chart with % split between restaurants offering online orders or not.

### 💰 Preferred Price Range
- Bar graph showing weighted score of price ranges (based on rating × number of ratings).

### 🍝 Most Popular Cuisine Types
- Colorful bar chart of top 15 cuisines by number of user ratings.

---

## ⚙️ Execution Flow

1. CSV file is loaded and cleaned
2. Each function (`offline_orders`, `analyze_price_range`, `analyze_favorite_cuisines`) is called
3. Plots are displayed for each analysis

---

## ❌ Error Handling

- Implemented a `try-except` block to catch:
  - Missing file
  - Invalid or corrupted data
  - Parsing errors during numeric conversion

---

## 🚀 How to Run

### 🧩 Prerequisites

- Python installed
- Required libraries:  
  `pip install pandas matplotlib seaborn`

### ▶️ Steps

1. Download Zomato dataset (CSV format)
2. Update the file path in the code  
   `df = pd.read_csv(r"Your\Path\To\zomato.csv")`
3. Run the script in any Python environment

---

## 📈 Real-Life Applications

- Food-tech businesses analyzing consumer patterns
- Restaurant managers planning offerings based on trends
- College data science portfolio projects

---

## 👨‍💻 Author

Created by a passionate BCA student exploring **Data Science** and **Data Visualization** using Python.  
🎯 This project bridges the gap between raw data and meaningful insights using real-time visualizations.

