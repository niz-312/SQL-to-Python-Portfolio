import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load Data
# (Assuming data is loaded into 'delivery_orders')
df = delivery_orders
df = df.dropna(subset=['actual_delivery_time'])

# 2. Data Cleaning & Feature Engineering
df['yr_mo'] = df['order_placed_time'].dt.strftime("%Y-%m")
df['diff_act_pred_min'] = (df['actual_delivery_time'] - df['predicted_delivery_time']).dt.total_seconds()/60

# 3. Business Logic: Flag Extreme Delays (>20 mins)
# Using np.where for vectorized speed (SQL Case When equivalent)
df['is_extremely_late'] = np.where(df['diff_act_pred_min'] > 20, 1, 0)

# 4. Aggregation: Calculate Monthly Late Percentage
result = df.groupby('yr_mo')['is_extremely_late'].mean().reset_index()
result['late_percentage'] = (result['is_extremely_late'] * 100).round(2)

# 5. Output
print(result)

# Note: Visualization code can be added here
