import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
# Page Configuration
st.set_page_config(
    page_title="Sales Analysis Dashboard",
    layout="wide"
)

st.title("Sales Analysis Dashboard")

# Load Data
df = pd.read_csv("sales_data_1.csv")

# Convert date
df['Date'] = df['Date'].apply(lambda x: datetime.datetime.strptime(x, '%d-%m-%Y'))


# Create Year and Month columns
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.strftime('%b')

# Sidebar Filters
st.sidebar.header("Filters")

year = st.sidebar.multiselect(
    "Select Year",
    options=df['Year'].unique(),
    default=df['Year'].unique()
)

month = st.sidebar.multiselect(
    "Select Month",
    options=df['Month'].unique(),
    default=df['Month'].unique()
)

region = st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

product = st.sidebar.multiselect(
    "Select Product",
    options=df['Product'].unique(),
    default=df['Product'].unique()
)

# Filter Data
filtered_df = df[
    (df['Year'].isin(year)) &
    (df['Month'].isin(month)) &
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Product'].isin(product))
]

# KPI Metrics
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_orders = filtered_df['Order ID'].nunique()
avg_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Sales", f"₹{total_sales:,.0f}")
col2.metric("Total Profit", f"₹{total_profit:,.0f}")
col3.metric("Orders", total_orders)
col4.metric("Avg Order Value", f"₹{avg_order_value:,.0f}")
col5.metric("Profit Margin", f"{profit_margin:.2f}%")

st.divider()

# Monthly Sales Trend
monthly_sales = filtered_df.groupby(
    filtered_df['Date'].dt.strftime('%b')
)['Sales'].sum().reset_index()

fig1 = px.line(
    monthly_sales,
    x='Date',
    y='Sales',
    title='Monthly Sales Trend',
    markers=True
)

st.plotly_chart(fig1, use_container_width=True)

# Category-wise Sales
col1, col2 = st.columns(2)

category_sales = filtered_df.groupby(
    'Category'
)['Sales'].sum().reset_index()

fig2 = px.bar(
    category_sales,
    x='Category',
    y='Sales',
    title='Category-wise Sales'
)

col1.plotly_chart(fig2, use_container_width=True)

# Region-wise Sales
region_sales = filtered_df.groupby(
    'Region'
)['Sales'].sum().reset_index()

fig3 = px.bar(
    region_sales,
    x='Region',
    y='Sales',
    title='Region-wise Sales'
)

col2.plotly_chart(fig3, use_container_width=True)

# Top 10 Products
top_products = filtered_df.groupby(
    'Product'
)['Sales'].sum().reset_index()

top_products = top_products.sort_values(
    by='Sales',
    ascending=False
).head(10)

fig4 = px.bar(
    top_products,
    x='Sales',
    y='Product',
    orientation='h',
    title='Top 10 Products'
)

st.plotly_chart(fig4, use_container_width=True)

# Salesperson Performance
col1, col2 = st.columns(2)

salesperson = filtered_df.groupby(
    'Salesperson'
)['Sales'].sum().reset_index()

fig5 = px.bar(
    salesperson,
    x='Salesperson',
    y='Sales',
    title='Salesperson Performance'
)

col1.plotly_chart(fig5, use_container_width=True)

# Customer Segmentation
segment = filtered_df.groupby(
    'Customer Segment'
)['Sales'].sum().reset_index()

fig6 = px.pie(
    segment,
    names='Customer Segment',
    values='Sales',
    title='Customer Segmentation'
)

col2.plotly_chart(fig6, use_container_width=True)

# Profit Analysis
fig7 = px.scatter(
    filtered_df,
    x='Sales',
    y='Profit',
    color='Category',
    size='Quantity',
    hover_data=['Product'],
    title='Profit Analysis'
)

st.plotly_chart(fig7, use_container_width=True)
