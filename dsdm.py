import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Logic: Lorenz Curve to visualize the "90/12 Rule" of Service Inequality
df_enroll = pd.read_csv('aadhaar_enrolment_fully_cleaned.csv')
pincode_vol = df_enroll.groupby('pincode')['total_enrolments'].sum().sort_values(ascending=False).values
cum_activity = np.cumsum(pincode_vol) / np.sum(pincode_vol) * 100
cum_geo = np.linspace(0, 100, len(pincode_vol))
plt.figure(figsize=(10, 5))
plt.plot(cum_geo, cum_activity, color='#8e44ad', lw=3, label='Actual Concentration')
plt.plot([0, 100], [0, 100], '--', color='grey', label='Perfect Equality')
plt.fill_between(cum_geo, cum_activity, alpha=0.1, color='#8e44ad')
plt.title('DSDM & Skewness: Service Monopoly Diagnostic', fontsize=14, fontweight='bold')
plt.legend()
plt.show()