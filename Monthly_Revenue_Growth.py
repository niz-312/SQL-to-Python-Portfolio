import pandas as pd

# PROJECT: Monthly Revenue Growth Analysis
# GOAL: Calculate month-over-month percentage growth in revenue.
# COMPARISON: Replicates SQL 'LAG()' function using Python's '.shift()'.

# 1. Load Data
# Assuming data is loaded into variable 'sf_transactions'
df = sf_transactions

# 2. Pre-processing: Sort by Date
# Critical Step: Unlike SQL, Python needs explicit sorting for time-series logic to work.
df = df.sort_values('created_at')

# 3. Extract Month (YYYY-MM)
df['yr_mo'] = df['created_at'].dt.strftime('%Y-%m')

# 4. Aggregation: Total Revenue per Month
monthly_df = df.groupby('yr_mo')['value'].sum().reset_index()

# 5. Logic: Calculate Previous Month's Revenue
# Python Method: .shift(1) moves the column down by 1 row (Equivalent to SQL LAG)
monthly_df['prev_rev'] = monthly_df['value'].shift(1)

# 6. Metric Calculation: Growth Percentage
# Formula: ((Current - Previous) / Previous) * 100
monthly_df['percent_change'] = (
    (monthly_df['value'] - monthly_df['prev_rev']) / monthly_df['prev_rev'] * 100
).round(2)

# 7. Output Result
print(monthly_df[['yr_mo', 'percent_change']])
