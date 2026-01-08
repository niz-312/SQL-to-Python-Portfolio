# 📊 SQL to Python: Logistics & Delivery Analytics

## 🎯 Project Goal
To analyze delivery performance gaps for a logistics platform (similar to Uber/Careem) by comparing **Predicted vs. Actual** delivery times. The goal is to identify monthly trends in "Extreme Delays" (>20 mins) which impact customer retention (NPS).

## 🛠️ Skills Demonstrated
* **Python (Pandas)**: Date manipulation (`.dt` accessor), Boolean Indexing.
* **Logic translation**: Converting SQL `CASE WHEN` to Python `np.where`.
* **Aggregation**: Grouping time-series data to calculate KPI percentages.

## 📈 Key Logic
The analysis defines "Extremely Late" as any order arriving **20+ minutes** after the predicted ETA.
```python
# Vectorized logic for high-performance flagging
df['is_extremely_late'] = np.where(df['diff_act_pred_min'] > 20, 1, 0)
