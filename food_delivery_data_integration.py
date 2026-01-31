"""
Food Delivery Data Integration Project
This script loads, merges, and analyzes data from three different sources:
- orders.csv (Transactional Data)
- users.json (User Master Data)
- restaurants.sql (Restaurant Master Data)
"""

import pandas as pd
import json
import re
import sqlite3
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

class FoodDeliveryDataIntegration:
    def __init__(self, orders_path, users_path, restaurants_path):
        """Initialize the data integration pipeline"""
        self.orders_path = orders_path
        self.users_path = users_path
        self.restaurants_path = restaurants_path
        self.orders_df = None
        self.users_df = None
        self.restaurants_df = None
        self.final_df = None
    
    def load_csv_data(self):
        """Step 1: Load CSV Data (Orders)"""
        print("=" * 70)
        print("STEP 1: Loading CSV Data (orders.csv)")
        print("=" * 70)
        
        self.orders_df = pd.read_csv(self.orders_path)
        
        # Convert date to datetime format
        self.orders_df['order_date'] = pd.to_datetime(self.orders_df['order_date'], format='%d-%m-%Y')
        
        print(f"✓ Loaded {len(self.orders_df)} orders")
        print(f"✓ Date range: {self.orders_df['order_date'].min()} to {self.orders_df['order_date'].max()}")
        print(f"\nColumns: {list(self.orders_df.columns)}")
        print(f"\nFirst 5 rows:")
        print(self.orders_df.head())
        print(f"\nData types:")
        print(self.orders_df.dtypes)
        print()
        
        return self.orders_df
    
    def load_json_data(self):
        """Step 2: Load JSON Data (Users)"""
        print("=" * 70)
        print("STEP 2: Loading JSON Data (users.json)")
        print("=" * 70)
        
        with open(self.users_path, 'r') as f:
            users_data = json.load(f)
        
        self.users_df = pd.DataFrame(users_data)
        
        print(f"✓ Loaded {len(self.users_df)} users")
        print(f"\nColumns: {list(self.users_df.columns)}")
        print(f"\nFirst 5 rows:")
        print(self.users_df.head())
        print(f"\nMembership distribution:")
        print(self.users_df['membership'].value_counts())
        print(f"\nCity distribution:")
        print(self.users_df['city'].value_counts())
        print()
        
        return self.users_df
    
    def load_sql_data(self):
        """Step 3: Load SQL Data (Restaurants)"""
        print("=" * 70)
        print("STEP 3: Loading SQL Data (restaurants.sql)")
        print("=" * 70)
        
        # Read the SQL file
        with open(self.restaurants_path, 'r') as f:
            sql_content = f.read()
        
        # Create an in-memory SQLite database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        # Execute the SQL statements
        cursor.executescript(sql_content)
        
        # Read the data into a DataFrame
        self.restaurants_df = pd.read_sql_query("SELECT * FROM restaurants", conn)
        
        conn.close()
        
        print(f"✓ Loaded {len(self.restaurants_df)} restaurants")
        print(f"\nColumns: {list(self.restaurants_df.columns)}")
        print(f"\nFirst 5 rows:")
        print(self.restaurants_df.head())
        print(f"\nCuisine distribution:")
        print(self.restaurants_df['cuisine'].value_counts())
        print(f"\nRating statistics:")
        print(self.restaurants_df['rating'].describe())
        print()
        
        return self.restaurants_df
    
    def merge_datasets(self):
        """Step 4: Merge the Data using LEFT JOIN"""
        print("=" * 70)
        print("STEP 4: Merging Datasets")
        print("=" * 70)
        
        # First merge: orders + users (on user_id)
        print("Merging orders with users on user_id...")
        merged_df = pd.merge(
            self.orders_df,
            self.users_df,
            on='user_id',
            how='left'
        )
        print(f"✓ After merging with users: {len(merged_df)} rows")
        
        # Second merge: (orders + users) + restaurants (on restaurant_id)
        print("Merging with restaurants on restaurant_id...")
        self.final_df = pd.merge(
            merged_df,
            self.restaurants_df,
            on='restaurant_id',
            how='left',
            suffixes=('_order', '_restaurant')
        )
        print(f"✓ Final dataset: {len(self.final_df)} rows")
        
        # Clean up column names (remove duplicate restaurant_name from orders)
        if 'restaurant_name_order' in self.final_df.columns:
            self.final_df = self.final_df.drop('restaurant_name_order', axis=1)
            self.final_df = self.final_df.rename(columns={'restaurant_name_restaurant': 'restaurant_name'})
        
        print(f"\nFinal columns: {list(self.final_df.columns)}")
        print(f"\nNull values check:")
        print(self.final_df.isnull().sum())
        print()
        
        return self.final_df
    
    def create_final_dataset(self, output_path):
        """Step 5: Create Final Dataset with additional features"""
        print("=" * 70)
        print("STEP 5: Creating Final Dataset with Enriched Features")
        print("=" * 70)
        
        # Add time-based features
        self.final_df['year'] = self.final_df['order_date'].dt.year
        self.final_df['month'] = self.final_df['order_date'].dt.month
        self.final_df['month_name'] = self.final_df['order_date'].dt.strftime('%B')
        self.final_df['day_of_week'] = self.final_df['order_date'].dt.day_name()
        self.final_df['quarter'] = self.final_df['order_date'].dt.quarter
        
        # Reorder columns for better readability
        column_order = [
            'order_id', 'order_date', 'year', 'month', 'month_name', 
            'day_of_week', 'quarter',
            'user_id', 'name', 'city', 'membership',
            'restaurant_id', 'restaurant_name', 'cuisine', 'rating',
            'total_amount'
        ]
        
        self.final_df = self.final_df[column_order]
        
        # Save to CSV
        self.final_df.to_csv(output_path, index=False)
        
        print(f"✓ Final dataset saved to: {output_path}")
        print(f"✓ Total rows: {len(self.final_df)}")
        print(f"✓ Total columns: {len(self.final_df.columns)}")
        print(f"\nDataset Summary:")
        print(f"  - Date range: {self.final_df['order_date'].min().date()} to {self.final_df['order_date'].max().date()}")
        print(f"  - Unique users: {self.final_df['user_id'].nunique()}")
        print(f"  - Unique restaurants: {self.final_df['restaurant_id'].nunique()}")
        print(f"  - Total revenue: ${self.final_df['total_amount'].sum():,.2f}")
        print(f"  - Average order value: ${self.final_df['total_amount'].mean():.2f}")
        print(f"\nFirst 10 rows of final dataset:")
        print(self.final_df.head(10))
        print()
        
        return self.final_df
    
    def generate_analysis_report(self):
        """Generate comprehensive analysis of the final dataset"""
        print("=" * 70)
        print("COMPREHENSIVE DATA ANALYSIS REPORT")
        print("=" * 70)
        print()
        
        # 1. Order Trends Over Time
        print("📊 1. ORDER TRENDS OVER TIME")
        print("-" * 70)
        monthly_orders = self.final_df.groupby(['year', 'month_name']).agg({
            'order_id': 'count',
            'total_amount': 'sum'
        }).round(2)
        monthly_orders.columns = ['Total Orders', 'Total Revenue']
        print(monthly_orders)
        print()
        
        # 2. User Behavior Patterns
        print("👥 2. USER BEHAVIOR PATTERNS")
        print("-" * 70)
        user_stats = self.final_df.groupby('user_id').agg({
            'order_id': 'count',
            'total_amount': ['sum', 'mean']
        }).round(2)
        user_stats.columns = ['Order Count', 'Total Spent', 'Avg Order Value']
        user_stats = user_stats.sort_values('Total Spent', ascending=False)
        print("Top 10 Users by Total Spending:")
        print(user_stats.head(10))
        print()
        
        # 3. City-wise Performance
        print("🏙️ 3. CITY-WISE PERFORMANCE")
        print("-" * 70)
        city_stats = self.final_df.groupby('city').agg({
            'order_id': 'count',
            'total_amount': ['sum', 'mean'],
            'user_id': 'nunique'
        }).round(2)
        city_stats.columns = ['Total Orders', 'Total Revenue', 'Avg Order Value', 'Unique Users']
        city_stats = city_stats.sort_values('Total Revenue', ascending=False)
        print(city_stats)
        print()
        
        # 4. Cuisine-wise Performance
        print("🍽️ 4. CUISINE-WISE PERFORMANCE")
        print("-" * 70)
        cuisine_stats = self.final_df.groupby('cuisine').agg({
            'order_id': 'count',
            'total_amount': ['sum', 'mean'],
            'rating': 'mean'
        }).round(2)
        cuisine_stats.columns = ['Total Orders', 'Total Revenue', 'Avg Order Value', 'Avg Rating']
        cuisine_stats = cuisine_stats.sort_values('Total Revenue', ascending=False)
        print(cuisine_stats)
        print()
        
        # 5. Membership Impact
        print("💳 5. MEMBERSHIP IMPACT (Gold vs Regular)")
        print("-" * 70)
        membership_stats = self.final_df.groupby('membership').agg({
            'order_id': 'count',
            'total_amount': ['sum', 'mean'],
            'user_id': 'nunique'
        }).round(2)
        membership_stats.columns = ['Total Orders', 'Total Revenue', 'Avg Order Value', 'Unique Users']
        print(membership_stats)
        print()
        
        # 6. Revenue Distribution
        print("💰 6. REVENUE DISTRIBUTION")
        print("-" * 70)
        print(f"Total Revenue: ${self.final_df['total_amount'].sum():,.2f}")
        print(f"Average Order Value: ${self.final_df['total_amount'].mean():.2f}")
        print(f"Median Order Value: ${self.final_df['total_amount'].median():.2f}")
        print(f"Standard Deviation: ${self.final_df['total_amount'].std():.2f}")
        print(f"Min Order Value: ${self.final_df['total_amount'].min():.2f}")
        print(f"Max Order Value: ${self.final_df['total_amount'].max():.2f}")
        print()
        
        # 7. Seasonality Analysis
        print("📅 7. SEASONALITY ANALYSIS")
        print("-" * 70)
        quarter_stats = self.final_df.groupby('quarter').agg({
            'order_id': 'count',
            'total_amount': 'sum'
        }).round(2)
        quarter_stats.columns = ['Total Orders', 'Total Revenue']
        print(quarter_stats)
        print()
        
        # 8. Day of Week Analysis
        print("📆 8. DAY OF WEEK ANALYSIS")
        print("-" * 70)
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        dow_stats = self.final_df.groupby('day_of_week').agg({
            'order_id': 'count',
            'total_amount': ['sum', 'mean']
        }).round(2)
        dow_stats.columns = ['Total Orders', 'Total Revenue', 'Avg Order Value']
        dow_stats = dow_stats.reindex(day_order)
        print(dow_stats)
        print()
        
        # 9. Top Performing Restaurants
        print("🏆 9. TOP PERFORMING RESTAURANTS")
        print("-" * 70)
        restaurant_stats = self.final_df.groupby(['restaurant_id', 'restaurant_name', 'cuisine']).agg({
            'order_id': 'count',
            'total_amount': 'sum',
            'rating': 'first'
        }).round(2)
        restaurant_stats.columns = ['Total Orders', 'Total Revenue', 'Rating']
        restaurant_stats = restaurant_stats.sort_values('Total Revenue', ascending=False)
        print("Top 15 Restaurants by Revenue:")
        print(restaurant_stats.head(15))
        print()
        
        # 10. Rating Analysis
        print("⭐ 10. RATING ANALYSIS")
        print("-" * 70)
        rating_bins = [0, 3.0, 3.5, 4.0, 4.5, 5.0]
        rating_labels = ['Poor (0-3.0)', 'Fair (3.0-3.5)', 'Good (3.5-4.0)', 'Great (4.0-4.5)', 'Excellent (4.5-5.0)']
        self.final_df['rating_category'] = pd.cut(self.final_df['rating'], bins=rating_bins, labels=rating_labels)
        rating_analysis = self.final_df.groupby('rating_category').agg({
            'order_id': 'count',
            'total_amount': 'mean'
        }).round(2)
        rating_analysis.columns = ['Order Count', 'Avg Order Value']
        print(rating_analysis)
        print()
        
        print("=" * 70)
        print("ANALYSIS COMPLETE")
        print("=" * 70)


def main():
    """Main execution function"""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 10 + "FOOD DELIVERY DATA INTEGRATION PROJECT" + " " * 19 + "║")
    print("╚" + "═" * 68 + "╝")
    print()
    
    # File paths
    orders_path = '/mnt/user-data/uploads/orders.csv'
    users_path = '/mnt/user-data/uploads/users.json'
    restaurants_path = '/mnt/user-data/uploads/restaurants.sql'
    output_path = '/home/claude/final_food_delivery_dataset.csv'
    
    # Initialize the integration pipeline
    integration = FoodDeliveryDataIntegration(orders_path, users_path, restaurants_path)
    
    # Execute the data integration pipeline
    try:
        # Step 1: Load CSV
        integration.load_csv_data()
        
        # Step 2: Load JSON
        integration.load_json_data()
        
        # Step 3: Load SQL
        integration.load_sql_data()
        
        # Step 4: Merge datasets
        integration.merge_datasets()
        
        # Step 5: Create final dataset
        integration.create_final_dataset(output_path)
        
        # Generate comprehensive analysis
        integration.generate_analysis_report()
        
        print("\n✅ SUCCESS! All steps completed successfully!")
        print(f"📁 Final dataset saved at: {output_path}")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
