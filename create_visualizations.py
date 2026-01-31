"""
Food Delivery Data Visualization Script
Generates comprehensive visualizations for the integrated dataset
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Load the final dataset
df = pd.read_csv('/home/claude/final_food_delivery_dataset.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

print("Creating visualizations...")
print("=" * 70)

# Create figure directory
import os
os.makedirs('/home/claude/visualizations', exist_ok=True)

# 1. Revenue Trend Over Time
plt.figure(figsize=(14, 6))
monthly_revenue = df.groupby(df['order_date'].dt.to_period('M'))['total_amount'].sum()
plt.plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker='o', linewidth=2, markersize=8)
plt.title('Monthly Revenue Trend - 2023', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/home/claude/visualizations/1_revenue_trend.png', dpi=300, bbox_inches='tight')
print("✓ Created: 1_revenue_trend.png")
plt.close()

# 2. Order Volume by City
plt.figure(figsize=(10, 6))
city_orders = df['city'].value_counts()
colors = sns.color_palette("viridis", len(city_orders))
bars = plt.bar(city_orders.index, city_orders.values, color=colors)
plt.title('Total Orders by City', fontsize=16, fontweight='bold')
plt.xlabel('City', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.xticks(rotation=0)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('/home/claude/visualizations/2_orders_by_city.png', dpi=300, bbox_inches='tight')
print("✓ Created: 2_orders_by_city.png")
plt.close()

# 3. Revenue by Cuisine
plt.figure(figsize=(10, 6))
cuisine_revenue = df.groupby('cuisine')['total_amount'].sum().sort_values(ascending=True)
colors = sns.color_palette("rocket", len(cuisine_revenue))
plt.barh(cuisine_revenue.index, cuisine_revenue.values, color=colors)
plt.title('Total Revenue by Cuisine Type', fontsize=16, fontweight='bold')
plt.xlabel('Revenue ($)', fontsize=12)
plt.ylabel('Cuisine', fontsize=12)
for i, v in enumerate(cuisine_revenue.values):
    plt.text(v, i, f' ${v:,.0f}', va='center', fontsize=10)
plt.tight_layout()
plt.savefig('/home/claude/visualizations/3_revenue_by_cuisine.png', dpi=300, bbox_inches='tight')
print("✓ Created: 3_revenue_by_cuisine.png")
plt.close()

# 4. Membership Comparison
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
membership_orders = df['membership'].value_counts()
colors = ['#FF6B6B', '#4ECDC4']
plt.pie(membership_orders.values, labels=membership_orders.index, autopct='%1.1f%%',
        startangle=90, colors=colors, textprops={'fontsize': 12})
plt.title('Order Distribution by Membership', fontsize=14, fontweight='bold')

plt.subplot(1, 2, 2)
membership_revenue = df.groupby('membership')['total_amount'].sum()
bars = plt.bar(membership_revenue.index, membership_revenue.values, color=colors)
plt.title('Revenue by Membership Type', fontsize=14, fontweight='bold')
plt.ylabel('Revenue ($)', fontsize=12)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'${height:,.0f}',
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('/home/claude/visualizations/4_membership_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Created: 4_membership_analysis.png")
plt.close()

# 5. Day of Week Analysis
plt.figure(figsize=(12, 6))
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_stats = df.groupby('day_of_week').agg({
    'order_id': 'count',
    'total_amount': 'sum'
})
dow_stats = dow_stats.reindex(day_order)

x = np.arange(len(day_order))
width = 0.35

fig, ax1 = plt.subplots(figsize=(12, 6))

color1 = '#3498db'
ax1.set_xlabel('Day of Week', fontsize=12)
ax1.set_ylabel('Number of Orders', color=color1, fontsize=12)
bars1 = ax1.bar(x - width/2, dow_stats['order_id'], width, label='Orders', color=color1, alpha=0.8)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_xticks(x)
ax1.set_xticklabels(day_order, rotation=45, ha='right')

ax2 = ax1.twinx()
color2 = '#e74c3c'
ax2.set_ylabel('Revenue ($)', color=color2, fontsize=12)
bars2 = ax2.bar(x + width/2, dow_stats['total_amount'], width, label='Revenue', color=color2, alpha=0.8)
ax2.tick_params(axis='y', labelcolor=color2)

plt.title('Orders and Revenue by Day of Week', fontsize=16, fontweight='bold')
fig.tight_layout()
plt.savefig('/home/claude/visualizations/5_day_of_week_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Created: 5_day_of_week_analysis.png")
plt.close()

# 6. Rating Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['rating'], bins=20, color='#9b59b6', edgecolor='black', alpha=0.7)
plt.axvline(df['rating'].mean(), color='red', linestyle='dashed', linewidth=2, label=f'Mean: {df["rating"].mean():.2f}')
plt.axvline(df['rating'].median(), color='green', linestyle='dashed', linewidth=2, label=f'Median: {df["rating"].median():.2f}')
plt.title('Distribution of Restaurant Ratings', fontsize=16, fontweight='bold')
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/home/claude/visualizations/6_rating_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Created: 6_rating_distribution.png")
plt.close()

# 7. Order Amount Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['total_amount'], bins=30, color='#16a085', edgecolor='black', alpha=0.7)
plt.axvline(df['total_amount'].mean(), color='red', linestyle='dashed', linewidth=2, 
           label=f'Mean: ${df["total_amount"].mean():.2f}')
plt.axvline(df['total_amount'].median(), color='green', linestyle='dashed', linewidth=2,
           label=f'Median: ${df["total_amount"].median():.2f}')
plt.title('Distribution of Order Amounts', fontsize=16, fontweight='bold')
plt.xlabel('Order Amount ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/home/claude/visualizations/7_order_amount_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Created: 7_order_amount_distribution.png")
plt.close()

# 8. Top 10 Restaurants by Revenue
plt.figure(figsize=(12, 7))
top_restaurants = df.groupby('restaurant_name')['total_amount'].sum().sort_values(ascending=True).tail(10)
colors = sns.color_palette("coolwarm", len(top_restaurants))
plt.barh(range(len(top_restaurants)), top_restaurants.values, color=colors)
plt.yticks(range(len(top_restaurants)), top_restaurants.index, fontsize=10)
plt.xlabel('Total Revenue ($)', fontsize=12)
plt.title('Top 10 Restaurants by Revenue', fontsize=16, fontweight='bold')
for i, v in enumerate(top_restaurants.values):
    plt.text(v, i, f' ${v:,.0f}', va='center', fontsize=9)
plt.tight_layout()
plt.savefig('/home/claude/visualizations/8_top_restaurants.png', dpi=300, bbox_inches='tight')
print("✓ Created: 8_top_restaurants.png")
plt.close()

# 9. Heatmap: City vs Cuisine Revenue
plt.figure(figsize=(10, 6))
pivot_data = df.pivot_table(values='total_amount', index='city', columns='cuisine', aggfunc='sum')
sns.heatmap(pivot_data, annot=True, fmt='.0f', cmap='YlOrRd', cbar_kws={'label': 'Revenue ($)'})
plt.title('Revenue Heatmap: City vs Cuisine', fontsize=16, fontweight='bold')
plt.xlabel('Cuisine', fontsize=12)
plt.ylabel('City', fontsize=12)
plt.tight_layout()
plt.savefig('/home/claude/visualizations/9_city_cuisine_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Created: 9_city_cuisine_heatmap.png")
plt.close()

# 10. Quarterly Performance
plt.figure(figsize=(10, 6))
quarterly_data = df.groupby('quarter').agg({
    'order_id': 'count',
    'total_amount': 'sum'
})

fig, ax1 = plt.subplots(figsize=(10, 6))

x = quarterly_data.index
width = 0.35

color1 = '#2ecc71'
ax1.set_xlabel('Quarter', fontsize=12)
ax1.set_ylabel('Number of Orders', color=color1, fontsize=12)
bars1 = ax1.bar(x - width/2, quarterly_data['order_id'], width, label='Orders', color=color1, alpha=0.8)
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()
color2 = '#e67e22'
ax2.set_ylabel('Revenue ($)', color=color2, fontsize=12)
bars2 = ax2.bar(x + width/2, quarterly_data['total_amount'], width, label='Revenue', color=color2, alpha=0.8)
ax2.tick_params(axis='y', labelcolor=color2)

plt.title('Quarterly Performance - Orders and Revenue', fontsize=16, fontweight='bold')
fig.tight_layout()
plt.savefig('/home/claude/visualizations/10_quarterly_performance.png', dpi=300, bbox_inches='tight')
print("✓ Created: 10_quarterly_performance.png")
plt.close()

print()
print("=" * 70)
print("✅ All visualizations created successfully!")
print("📁 Location: /home/claude/visualizations/")
print("=" * 70)
