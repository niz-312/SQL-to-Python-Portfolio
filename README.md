# 📊 SQL to Python: Analytics Portfolio

## 📂 Project 1: Logistics & Delivery Analytics
**File:** `Uber_Extremely_Late_Delivery.py`
**Goal:** Analyze delivery performance gaps (Uber/Careem) by identifying "Extreme Delays" (>20 mins).

### 🧠 Key Logic
Converting SQL `CASE WHEN` to Python `np.where` for speed.
```python
# Vectorized logic for high-performance flagging
df['is_extremely_late'] = np.where(df['diff_act_pred_min'] > 20, 1, 0)
