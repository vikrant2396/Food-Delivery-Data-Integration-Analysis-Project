# Food Delivery Data Integration & Analysis Project
## Complete Documentation and Insights Report

---

## 📋 Executive Summary

This project successfully integrates three different data sources (CSV, JSON, and SQL) to create a comprehensive food delivery dataset. The final dataset contains **10,000 orders** from **2,883 unique users** across **500 restaurants** in **4 cities**, generating a total revenue of **$8,011,624.12** throughout 2023.

---

## 🎯 Project Objectives

1. **Data Integration**: Merge three different data formats into a single, unified dataset
2. **Data Enrichment**: Add temporal features and derived metrics
3. **Comprehensive Analysis**: Extract actionable insights for business decision-making
4. **Visualization**: Create clear, informative charts for stakeholders

---

## 📊 Dataset Overview

### Final Dataset Specifications
- **Total Records**: 10,000 orders
- **Date Range**: January 1, 2023 - January 1, 2024
- **Unique Users**: 2,883
- **Unique Restaurants**: 500
- **Cities Covered**: 4 (Bangalore, Chennai, Pune, Hyderabad)
- **Cuisines Available**: 4 (Mexican, Italian, Indian, Chinese)

### Dataset Structure (16 Columns)

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| order_id | Integer | Unique order identifier |
| order_date | DateTime | Date of the order |
| year | Integer | Year extracted from order_date |
| month | Integer | Month number (1-12) |
| month_name | String | Month name (January-December) |
| day_of_week | String | Day name (Monday-Sunday) |
| quarter | Integer | Quarter (1-4) |
| user_id | Integer | Unique user identifier |
| name | String | User name |
| city | String | User's city |
| membership | String | Membership type (Gold/Regular) |
| restaurant_id | Integer | Unique restaurant identifier |
| restaurant_name | String | Restaurant name |
| cuisine | String | Type of cuisine |
| rating | Float | Restaurant rating (3.0-5.0) |
| total_amount | Float | Order total in dollars |

---

## 🔍 Key Insights & Findings

### 1. Revenue Performance

**Total Revenue**: $8,011,624.12
- **Average Order Value**: $801.16
- **Median Order Value**: $806.30
- **Revenue Range**: $100.20 - $1,499.83

**Monthly Performance**:
- **Highest Revenue Month**: March 2023 ($716,738.98)
- **Lowest Revenue Month**: June 2023 ($610,822.93)
- Average monthly revenue: ~$640,000

**Key Insight**: Revenue remains relatively stable throughout the year with slight peak in Q1 and Q4.

---

### 2. Geographic Analysis

#### City Performance Ranking

| Rank | City | Total Orders | Revenue | Avg Order Value | Market Share |
|------|------|--------------|---------|-----------------|--------------|
| 1 | Bangalore | 2,751 | $2,206,946.58 | $802.23 | 27.5% |
| 2 | Chennai | 2,469 | $1,990,513.03 | $806.20 | 24.7% |
| 3 | Pune | 2,430 | $1,924,797.93 | $792.10 | 24.3% |
| 4 | Hyderabad | 2,350 | $1,889,366.58 | $803.99 | 23.5% |

**Key Insights**:
- Bangalore leads in both orders and revenue
- All cities have similar average order values (~$800)
- Market distribution is relatively balanced across cities
- Chennai has the highest average order value

---

### 3. Cuisine Performance

#### Cuisine Ranking by Revenue

| Cuisine | Orders | Revenue | Avg Order Value | Avg Rating |
|---------|--------|---------|-----------------|------------|
| Mexican | 2,581 | $2,085,503.09 | $808.02 | 4.02 |
| Italian | 2,532 | $2,024,203.80 | $799.45 | 4.04 |
| Indian | 2,469 | $1,971,412.58 | $798.47 | 4.02 |
| Chinese | 2,418 | $1,930,504.65 | $798.39 | 4.10 |

**Key Insights**:
- Mexican cuisine leads in revenue despite having similar order volumes
- Chinese cuisine has the highest average rating (4.10)
- All cuisines maintain strong performance with minimal variation
- Average order values are consistent across cuisines (~$800)

---

### 4. Membership Analysis

#### Gold vs Regular Comparison

| Membership Type | Orders | Revenue | Avg Order Value | User Count |
|----------------|--------|---------|-----------------|------------|
| Gold | 4,987 | $3,975,364.89 | $797.15 | 1,430 |
| Regular | 5,013 | $4,036,259.23 | $805.16 | 1,453 |

**Key Insights**:
- Nearly equal split between Gold (49.9%) and Regular (50.1%) members
- Regular members have slightly higher average order value (+$8.01)
- Both segments contribute equally to overall revenue
- Gold members represent 49.3% of total users but generate 49.6% of revenue

**Recommendations**:
- Investigate why Regular members have higher AOV
- Consider loyalty program enhancements to increase Gold member engagement
- Analyze retention rates between membership tiers

---

### 5. Temporal Patterns

#### Day of Week Analysis

| Day | Total Orders | Revenue | Avg Order Value |
|-----|--------------|---------|-----------------|
| Sunday | 1,461 | $1,189,055.72 | $813.86 |
| Saturday | 1,430 | $1,156,335.84 | $808.63 |
| Friday | 1,466 | $1,174,418.88 | $801.10 |
| Monday | 1,418 | $1,137,568.63 | $802.23 |
| Wednesday | 1,404 | $1,126,468.28 | $802.33 |
| Thursday | 1,453 | $1,145,695.14 | $788.50 |
| Tuesday | 1,368 | $1,082,081.63 | $791.00 |

**Key Insights**:
- **Weekend Peak**: Sunday shows highest average order value ($813.86)
- Consistent order volume throughout the week (1,368-1,466 orders)
- Tuesday has lowest performance
- Weekend days (Sat-Sun) have 14.5% of weekly orders

#### Quarterly Performance

| Quarter | Total Orders | Total Revenue |
|---------|--------------|---------------|
| Q1 | 2,519 | $2,010,626.64 |
| Q2 | 2,440 | $1,945,348.72 |
| Q3 | 2,522 | $2,037,385.10 |
| Q4 | 2,519 | $2,018,263.66 |

**Key Insights**:
- Q3 (Jul-Sep) shows highest performance
- Q2 (Apr-Jun) shows slight dip
- Minimal seasonal variation (±3.2%)
- Consistent demand throughout the year

---

### 6. Restaurant Performance

#### Top 10 Restaurants by Revenue

| Rank | Restaurant | Cuisine | Orders | Revenue | Rating |
|------|-----------|---------|--------|---------|--------|
| 1 | Restaurant_287 | Chinese | 35 | $29,460.47 | 4.7 |
| 2 | Restaurant_19 | Indian | 26 | $29,289.52 | 3.6 |
| 3 | Restaurant_484 | Mexican | 28 | $27,051.49 | 4.2 |
| 4 | Restaurant_61 | Italian | 30 | $26,049.71 | 4.4 |
| 5 | Restaurant_134 | Mexican | 30 | $25,791.23 | 4.3 |
| 6 | Restaurant_440 | Mexican | 27 | $25,467.45 | 3.8 |
| 7 | Restaurant_383 | Indian | 36 | $24,955.59 | 3.1 |
| 8 | Restaurant_188 | Chinese | 30 | $24,698.82 | 4.6 |
| 9 | Restaurant_431 | Mexican | 27 | $24,684.31 | 4.6 |
| 10 | Restaurant_153 | Italian | 27 | $24,523.66 | 4.7 |

**Key Insights**:
- Top restaurant generates $29,460.47 with 35 orders
- Interestingly, Restaurant_19 ranks #2 despite low rating (3.6)
- High-performing restaurants maintain 26-36 orders
- Rating doesn't always correlate with revenue

---

### 7. Rating Analysis

#### Rating Distribution

| Rating Category | Orders | Avg Order Value |
|----------------|--------|-----------------|
| Poor (0-3.0) | 331 | $770.45 |
| Fair (3.0-3.5) | 2,348 | $801.43 |
| Good (3.5-4.0) | 2,118 | $810.90 |
| Great (4.0-4.5) | 2,431 | $806.39 |
| Excellent (4.5-5.0) | 2,772 | $792.58 |

**Key Insights**:
- **27.7% of orders** come from Excellent-rated restaurants
- Poor-rated restaurants have lowest average order value ($770.45)
- Surprisingly, Good-rated (3.5-4.0) restaurants have highest AOV
- Only 3.3% of orders from Poor-rated restaurants

**Overall Rating Statistics**:
- **Mean Rating**: 4.04/5.0
- **Median Rating**: 4.10/5.0
- **Rating Range**: 3.0 - 5.0

---

### 8. User Behavior Insights

#### Top 10 Users by Spending

| User ID | Order Count | Total Spent | Avg Order Value |
|---------|-------------|-------------|-----------------|
| 1515 | 12 | $11,556.49 | $963.04 |
| 650 | 10 | $10,747.44 | $1,074.74 |
| 496 | 11 | $9,634.30 | $875.85 |
| 2586 | 10 | $9,486.61 | $948.66 |
| 2615 | 9 | $9,237.32 | $1,026.37 |

**Key Insights**:
- Top user has spent $11,556.49 across 12 orders
- High-value users order 8-13 times per year
- Average order frequency: 3.5 orders per user
- Top 10 users contribute $93,706.50 (1.17% of total revenue)

---

## 💡 Business Recommendations

### 1. **Geographic Expansion**
- Focus on Bangalore - highest performing market
- Investigate Chennai's high AOV for replication in other cities
- Balance marketing efforts across all cities

### 2. **Cuisine Strategy**
- Leverage Mexican cuisine's strong performance
- Promote Chinese restaurants (highest ratings)
- Cross-promote cuisines to increase order diversity

### 3. **Membership Program**
- Investigate why Regular members have higher AOV
- Develop targeted incentives for Gold members
- Consider tiered benefits to increase Gold upgrades

### 4. **Weekend Optimization**
- Capitalize on Sunday's high AOV with premium offerings
- Create weekend-specific promotions
- Ensure adequate restaurant capacity on weekends

### 5. **Restaurant Partnerships**
- Support top-performing restaurants with featured placements
- Help improve low-rated restaurants (3.0-3.5)
- Partner with high-rated restaurants for marketing

### 6. **User Retention**
- Create loyalty programs for high-value users
- Implement retention campaigns for one-time users
- Target users with 1-2 orders for re-engagement

---

## 📈 Technical Implementation

### Data Integration Process

1. **CSV Loading** (orders.csv)
   - Loaded 10,000 transactional records
   - Converted date strings to datetime objects
   - Validated data integrity

2. **JSON Loading** (users.json)
   - Parsed 3,000 user records
   - Extracted nested data structures
   - Mapped user attributes

3. **SQL Loading** (restaurants.sql)
   - Created in-memory SQLite database
   - Executed DDL and INSERT statements
   - Extracted 500 restaurant records

4. **Data Merging**
   - Left join: orders + users (on user_id)
   - Left join: result + restaurants (on restaurant_id)
   - Preserved all order records

5. **Data Enrichment**
   - Added temporal features (year, month, quarter, day_of_week)
   - Created derived metrics
   - Validated completeness (0 null values)

### Quality Assurance

✅ **100% Data Completeness** - No null values in final dataset
✅ **Data Validation** - All joins successful
✅ **Type Consistency** - Proper data types enforced
✅ **Date Integrity** - Valid date range with no anomalies
✅ **Referential Integrity** - All foreign keys matched

---

## 📁 Project Deliverables

### Files Created

1. **final_food_delivery_dataset.csv** - Complete integrated dataset (10,000 rows × 16 columns)
2. **food_delivery_data_integration.py** - Main integration script with analysis
3. **create_visualizations.py** - Visualization generation script
4. **10 Visualization Charts** - Comprehensive visual analysis
5. **This Documentation** - Complete project insights and recommendations

### Visualizations Generated

1. Monthly Revenue Trend
2. Orders by City
3. Revenue by Cuisine
4. Membership Analysis
5. Day of Week Analysis
6. Rating Distribution
7. Order Amount Distribution
8. Top Restaurants
9. City-Cuisine Heatmap
10. Quarterly Performance

---

## 🎓 Learning Outcomes

Students analyzing this dataset should understand:

1. **Data Integration**: Merging heterogeneous data sources
2. **Data Cleaning**: Handling different formats and structures
3. **Feature Engineering**: Creating temporal and derived features
4. **Exploratory Analysis**: Statistical analysis and pattern recognition
5. **Business Intelligence**: Translating data into actionable insights
6. **Visualization**: Communicating insights through charts
7. **SQL Operations**: Working with database exports
8. **JSON Processing**: Handling nested data structures
9. **Time Series Analysis**: Understanding temporal patterns
10. **Customer Segmentation**: Analyzing user behavior

---

## 📊 Summary Statistics

### Overall Metrics
- **Total Revenue**: $8,011,624.12
- **Total Orders**: 10,000
- **Average Order Value**: $801.16
- **Active Users**: 2,883
- **Active Restaurants**: 500
- **Date Range**: 365 days (2023)

### Distribution Metrics
- **Cities**: 4 (balanced distribution)
- **Cuisines**: 4 (balanced distribution)
- **Membership**: ~50/50 Gold/Regular
- **Rating Range**: 3.0 - 5.0 (Mean: 4.04)

---

## 🚀 Next Steps for Analysis

1. **Predictive Modeling**: Forecast future order volumes
2. **Customer Segmentation**: RFM analysis and clustering
3. **Churn Prediction**: Identify at-risk users
4. **Recommendation Engine**: Personalized restaurant suggestions
5. **Price Optimization**: Dynamic pricing strategies
6. **Demand Forecasting**: Inventory and capacity planning
7. **Cohort Analysis**: User lifecycle analysis
8. **A/B Testing Framework**: Experiment design for optimization

---

## 📞 Contact & Support

For questions or additional analysis requests, please refer to:
- Dataset: `final_food_delivery_dataset.csv`
- Scripts: `food_delivery_data_integration.py`
- Visualizations: `/visualizations/` directory

---

**Project Completion Date**: January 31, 2026
**Dataset Version**: 1.0
**Status**: ✅ Complete and Ready for Analysis

---

*This project demonstrates real-world data integration skills essential for data analytics, business intelligence, and data science roles.*
