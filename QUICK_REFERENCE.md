# 📊 Quick Reference Guide - Common Analysis Queries

This guide provides ready-to-use code snippets for analyzing the food delivery dataset.

---

## 🚀 Getting Started

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('final_food_delivery_dataset.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

# Quick overview
print(df.head())
print(df.info())
print(df.describe())
```

---

## 💰 Revenue Analysis

### Total Revenue
```python
total_revenue = df['total_amount'].sum()
print(f"Total Revenue: ${total_revenue:,.2f}")
```

### Average Order Value
```python
avg_order = df['total_amount'].mean()
median_order = df['total_amount'].median()
print(f"Average Order Value: ${avg_order:.2f}")
print(f"Median Order Value: ${median_order:.2f}")
```

### Revenue by Month
```python
monthly_revenue = df.groupby('month_name')['total_amount'].sum().sort_values(ascending=False)
print(monthly_revenue)

# Visualization
monthly_revenue.plot(kind='bar', color='skyblue')
plt.title('Monthly Revenue')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Revenue by City
```python
city_revenue = df.groupby('city').agg({
    'order_id': 'count',
    'total_amount': ['sum', 'mean']
}).round(2)
city_revenue.columns = ['Orders', 'Total Revenue', 'Avg Order Value']
print(city_revenue.sort_values('Total Revenue', ascending=False))
```

---

## 👥 Customer Analysis

### Top 10 Customers by Spending
```python
top_customers = df.groupby('user_id').agg({
    'order_id': 'count',
    'total_amount': 'sum'
}).round(2)
top_customers.columns = ['Order Count', 'Total Spent']
top_customers = top_customers.sort_values('Total Spent', ascending=False).head(10)
print(top_customers)
```

### Customer Order Frequency
```python
order_frequency = df.groupby('user_id')['order_id'].count()
print(f"Average orders per customer: {order_frequency.mean():.2f}")
print(f"\nOrder Frequency Distribution:")
print(order_frequency.value_counts().sort_index())

# Visualization
order_frequency.hist(bins=20, color='coral', edgecolor='black')
plt.title('Distribution of Orders per Customer')
plt.xlabel('Number of Orders')
plt.ylabel('Number of Customers')
plt.show()
```

### Membership Analysis
```python
membership_stats = df.groupby('membership').agg({
    'order_id': 'count',
    'total_amount': ['sum', 'mean'],
    'user_id': 'nunique'
}).round(2)
membership_stats.columns = ['Orders', 'Total Revenue', 'Avg Order', 'Unique Users']
print(membership_stats)
```

---

## 🍽️ Restaurant Analysis

### Top Restaurants by Revenue
```python
restaurant_performance = df.groupby(['restaurant_id', 'restaurant_name']).agg({
    'order_id': 'count',
    'total_amount': 'sum',
    'rating': 'first'
}).round(2)
restaurant_performance.columns = ['Orders', 'Revenue', 'Rating']
top_restaurants = restaurant_performance.sort_values('Revenue', ascending=False).head(20)
print(top_restaurants)
```

### Restaurant by Cuisine
```python
cuisine_performance = df.groupby('cuisine').agg({
    'order_id': 'count',
    'total_amount': ['sum', 'mean'],
    'rating': 'mean'
}).round(2)
cuisine_performance.columns = ['Orders', 'Total Revenue', 'Avg Order', 'Avg Rating']
print(cuisine_performance.sort_values('Total Revenue', ascending=False))
```

### Rating Impact on Orders
```python
# Create rating categories
df['rating_category'] = pd.cut(df['rating'], 
                                bins=[0, 3.5, 4.0, 4.5, 5.0],
                                labels=['Low', 'Medium', 'High', 'Excellent'])

rating_impact = df.groupby('rating_category').agg({
    'order_id': 'count',
    'total_amount': 'mean'
}).round(2)
rating_impact.columns = ['Order Count', 'Avg Order Value']
print(rating_impact)
```

---

## 📅 Time-Based Analysis

### Orders by Day of Week
```python
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_analysis = df.groupby('day_of_week').agg({
    'order_id': 'count',
    'total_amount': ['sum', 'mean']
}).round(2)
day_analysis.columns = ['Orders', 'Total Revenue', 'Avg Order']
day_analysis = day_analysis.reindex(day_order)
print(day_analysis)

# Visualization
day_analysis['Orders'].plot(kind='bar', color='teal')
plt.title('Orders by Day of Week')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Weekend vs Weekday
```python
weekend = df[df['day_of_week'].isin(['Saturday', 'Sunday'])]
weekday = df[~df['day_of_week'].isin(['Saturday', 'Sunday'])]

print("Weekend Performance:")
print(f"  Orders: {len(weekend)}")
print(f"  Revenue: ${weekend['total_amount'].sum():,.2f}")
print(f"  Avg Order: ${weekend['total_amount'].mean():.2f}")

print("\nWeekday Performance:")
print(f"  Orders: {len(weekday)}")
print(f"  Revenue: ${weekday['total_amount'].sum():,.2f}")
print(f"  Avg Order: ${weekday['total_amount'].mean():.2f}")
```

### Quarterly Trends
```python
quarterly = df.groupby('quarter').agg({
    'order_id': 'count',
    'total_amount': 'sum'
}).round(2)
quarterly.columns = ['Orders', 'Revenue']
print(quarterly)

# Visualization
quarterly.plot(kind='bar', subplots=True, figsize=(10, 8))
plt.tight_layout()
plt.show()
```

### Monthly Growth Rate
```python
monthly = df.groupby(df['order_date'].dt.to_period('M'))['total_amount'].sum()
monthly_growth = monthly.pct_change() * 100
print("Month-over-Month Growth Rate (%):")
print(monthly_growth.round(2))
```

---

## 🌍 Geographic Analysis

### City Comparison
```python
city_comparison = df.groupby('city').agg({
    'order_id': 'count',
    'total_amount': ['sum', 'mean', 'std'],
    'user_id': 'nunique',
    'restaurant_id': 'nunique'
}).round(2)
city_comparison.columns = ['Orders', 'Revenue', 'Avg Order', 'Std Dev', 'Users', 'Restaurants']
print(city_comparison)
```

### City-Cuisine Matrix
```python
city_cuisine = df.pivot_table(
    values='total_amount',
    index='city',
    columns='cuisine',
    aggfunc='sum'
).round(2)
print(city_cuisine)

# Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(city_cuisine, annot=True, fmt='.0f', cmap='YlOrRd')
plt.title('Revenue Heatmap: City vs Cuisine')
plt.tight_layout()
plt.show()
```

---

## 🎯 Advanced Queries

### Customer Lifetime Value (CLV)
```python
clv = df.groupby('user_id').agg({
    'order_id': 'count',
    'total_amount': 'sum',
    'order_date': ['min', 'max']
})
clv.columns = ['Orders', 'Total Spent', 'First Order', 'Last Order']
clv['Days Active'] = (pd.to_datetime(clv['Last Order']) - 
                      pd.to_datetime(clv['First Order'])).dt.days
clv['CLV'] = clv['Total Spent']
print(clv.sort_values('CLV', ascending=False).head(10))
```

### Cohort Analysis (By Month)
```python
df['cohort_month'] = df['order_date'].dt.to_period('M')
df['order_month'] = df['order_date'].dt.to_period('M')

cohort_data = df.groupby(['user_id', 'cohort_month']).size().reset_index(name='orders')
first_purchase = cohort_data.groupby('user_id')['cohort_month'].min().reset_index()
first_purchase.columns = ['user_id', 'first_month']

print("Cohort retention analysis available")
```

### High-Value vs Low-Value Customers
```python
customer_value = df.groupby('user_id')['total_amount'].sum()
threshold = customer_value.median()

high_value = df[df['user_id'].isin(customer_value[customer_value > threshold].index)]
low_value = df[df['user_id'].isin(customer_value[customer_value <= threshold].index)]

print("High-Value Customers:")
print(f"  Count: {high_value['user_id'].nunique()}")
print(f"  Avg Spend: ${high_value['total_amount'].mean():.2f}")
print(f"  Total Revenue: ${high_value['total_amount'].sum():,.2f}")

print("\nLow-Value Customers:")
print(f"  Count: {low_value['user_id'].nunique()}")
print(f"  Avg Spend: ${low_value['total_amount'].mean():.2f}")
print(f"  Total Revenue: ${low_value['total_amount'].sum():,.2f}")
```

### Restaurant Performance Score
```python
restaurant_score = df.groupby('restaurant_id').agg({
    'order_id': 'count',
    'total_amount': 'sum',
    'rating': 'first'
})
restaurant_score.columns = ['Orders', 'Revenue', 'Rating']

# Normalize and create composite score
restaurant_score['Order_Score'] = (restaurant_score['Orders'] - restaurant_score['Orders'].min()) / (restaurant_score['Orders'].max() - restaurant_score['Orders'].min())
restaurant_score['Revenue_Score'] = (restaurant_score['Revenue'] - restaurant_score['Revenue'].min()) / (restaurant_score['Revenue'].max() - restaurant_score['Revenue'].min())
restaurant_score['Rating_Score'] = (restaurant_score['Rating'] - restaurant_score['Rating'].min()) / (restaurant_score['Rating'].max() - restaurant_score['Rating'].min())

restaurant_score['Performance_Score'] = (
    restaurant_score['Order_Score'] * 0.3 +
    restaurant_score['Revenue_Score'] * 0.5 +
    restaurant_score['Rating_Score'] * 0.2
) * 100

print(restaurant_score.sort_values('Performance_Score', ascending=False).head(10))
```

---

## 📊 Statistical Analysis

### Correlation Analysis
```python
# Numeric correlations
numeric_cols = ['rating', 'total_amount']
correlation = df[numeric_cols].corr()
print(correlation)

# Heatmap
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()
```

### Distribution Analysis
```python
print("Order Amount Distribution:")
print(f"Mean: ${df['total_amount'].mean():.2f}")
print(f"Median: ${df['total_amount'].median():.2f}")
print(f"Std Dev: ${df['total_amount'].std():.2f}")
print(f"Skewness: {df['total_amount'].skew():.2f}")
print(f"Kurtosis: {df['total_amount'].kurtosis():.2f}")

# Percentiles
percentiles = [25, 50, 75, 90, 95, 99]
for p in percentiles:
    value = df['total_amount'].quantile(p/100)
    print(f"{p}th percentile: ${value:.2f}")
```

### Outlier Detection
```python
Q1 = df['total_amount'].quantile(0.25)
Q3 = df['total_amount'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['total_amount'] < lower_bound) | (df['total_amount'] > upper_bound)]
print(f"Number of outliers: {len(outliers)}")
print(f"Percentage of outliers: {len(outliers)/len(df)*100:.2f}%")
```

---

## 💡 Filtering Examples

### High-Value Orders (Top 10%)
```python
threshold_90 = df['total_amount'].quantile(0.90)
high_value_orders = df[df['total_amount'] >= threshold_90]
print(f"Orders above ${threshold_90:.2f}:")
print(high_value_orders[['order_id', 'city', 'cuisine', 'total_amount']].head(10))
```

### Weekend Orders in Bangalore
```python
bangalore_weekend = df[
    (df['city'] == 'Bangalore') & 
    (df['day_of_week'].isin(['Saturday', 'Sunday']))
]
print(f"Weekend orders in Bangalore: {len(bangalore_weekend)}")
print(f"Weekend revenue in Bangalore: ${bangalore_weekend['total_amount'].sum():,.2f}")
```

### Gold Members, High-Rated Restaurants
```python
premium_orders = df[
    (df['membership'] == 'Gold') & 
    (df['rating'] >= 4.5)
]
print(f"Gold member orders at highly-rated restaurants: {len(premium_orders)}")
print(f"Average order value: ${premium_orders['total_amount'].mean():.2f}")
```

---

## 📈 Trend Analysis

### Monthly Trend with Moving Average
```python
monthly_orders = df.groupby(df['order_date'].dt.to_period('M'))['order_id'].count()
monthly_orders_ma = monthly_orders.rolling(window=3).mean()

plt.figure(figsize=(12, 6))
plt.plot(monthly_orders.index.astype(str), monthly_orders.values, label='Actual', marker='o')
plt.plot(monthly_orders.index.astype(str), monthly_orders_ma.values, label='3-Month MA', linestyle='--')
plt.title('Monthly Order Trend with Moving Average')
plt.xlabel('Month')
plt.ylabel('Orders')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 🎨 Quick Visualizations

### Revenue Distribution
```python
plt.figure(figsize=(10, 6))
plt.hist(df['total_amount'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(df['total_amount'].mean(), color='red', linestyle='--', label='Mean')
plt.axvline(df['total_amount'].median(), color='green', linestyle='--', label='Median')
plt.title('Distribution of Order Amounts')
plt.xlabel('Order Amount ($)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
```

### Top 10 Cities or Cuisines
```python
# Quick bar chart
df['cuisine'].value_counts().head(10).plot(kind='barh', color='coral')
plt.title('Top Cuisines by Order Count')
plt.xlabel('Number of Orders')
plt.tight_layout()
plt.show()
```

---

## 🔍 Data Validation

### Check Data Quality
```python
print("Data Quality Report:")
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"\nNull values:")
print(df.isnull().sum())
print(f"\nDuplicate rows: {df.duplicated().sum()}")
print(f"\nDate range: {df['order_date'].min()} to {df['order_date'].max()}")
print(f"Unique users: {df['user_id'].nunique()}")
print(f"Unique restaurants: {df['restaurant_id'].nunique()}")
```

---

**💡 Tip**: Save this file for quick reference when analyzing the dataset!

**📚 For more detailed analysis, refer to `PROJECT_DOCUMENTATION.md`**
