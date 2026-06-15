#  Sales Analysis Dashboard

A modern and interactive Sales Analysis Dashboard built using **Python, Streamlit, Pandas, and Plotly**. This dashboard provides valuable insights into sales performance, profitability, customer segments, and product trends through dynamic visualizations and filters.

---

##  Features

###  Key Performance Indicators (KPIs)
- Total Sales
- Total Profit
- Total Orders
- Average Order Value (AOV)
- Profit Margin (%)

###  Interactive Visualizations
- Monthly Sales Trend (Line Chart)
- Category-wise Sales Analysis (Bar Chart)
- Region-wise Sales Analysis (Bar Chart)
- Top 10 Products Analysis
- Salesperson Performance
- Customer Segmentation (Pie Chart)
- Profit Analysis (Scatter Plot)

###  Interactive Filters
Users can filter data based on:
- Year
- Month
- Region
- Category
- Product

---

##  Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **OpenPyXL**

---
## Installing requirement:

  pip install -r requirements.txt
## How to run
  streamlit run app.py
  
After execution, the dashboard will open in your browser at:

  http://localhost:8501
---

## 📋 Dataset Columns

The dataset should contain the following columns:

| Column Name | Description |
|--------------|------------|
| Order ID | Unique order identifier |
| Date | Transaction date |
| Region | Sales region |
| Category | Product category |
| Product | Product name |
| Salesperson | Name of salesperson |
| Customer Segment | Customer type |
| Quantity | Quantity sold |
| Sales | Revenue generated |
| Profit | Profit earned |

---
### Dashboard Components

###KPI Cards

Displays:
  -Total Sales
  -Total Profit
  -Orders
  -Average Order Value
  -Profit Margin
### Monthly Sales Trend

-Shows monthly sales performance using a line chart.

### Category-wise Sales

-Compares revenue across different product categories.

### Region-wise Sales

-Analyzes sales performance by region.

### Top 10 Products

-Identifies the highest revenue-generating products.

### Salesperson Performance

-Evaluates individual sales contributions.

### Customer Segmentation

-Shows revenue distribution among customer segments.

### Profit Analysis

-Visualizes the relationship between sales and profit.

### Future Enhancements:
  
  -Export Dashboard to PDF
  
  -Download Reports to Excel
  
  -Sales Forecasting using Machine Learning
  
  -User Authentication System
  
  -Real-time Database Integration
  
  -AI-powered Sales Prediction
