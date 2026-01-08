# 📊 SQL to Python: Analytics Portfolio
---

## Project 1: Logistics & Delivery Analytics
**File:** `Uber_Extremely_Late_Delivery.py`  
**Goal:**  Analyze delivery performance gaps (Uber / Careem) by identifying **Extreme Delays**  
(orders delayed by more than **20 minutes**).

### Key Logic
Converting SQL `CASE WHEN` logic into **vectorized Python** using `np.where` for high performance on large datasets.
```python
# Vectorized logic for high-performance flagging
df['is_extremely_late'] = np.where(df['diff_act_pred_min'] > 20,1,0)
```

## Project 2: Monthly Revenue Growth (Financial)
**File**: Monthly_Revenue_Growth.py
**Goal**:Calculate Month-over-Month (MoM) revenue growth.
This replicates the SQL LAG() window function using Python.

**🧠 Key Logic**
Using .shift(1) to create a Previous Month Revenue column for comparison.

# Create 'prev_rev' column (Equivalent to SQL LAG)
monthly_df['prev_rev'] = monthly_df['value'].shift(1)

# Calculate Month-over-Month % Growth
monthly_df['percent_change'] = ((monthly_df['value'] - monthly_df['prev_rev'])/ monthly_df['prev_rev'] * 100).round(2)
