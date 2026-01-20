import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATA
df_enroll = pd.read_csv('/content/aadhaar_enrolment_fully_cleaned.csv')
df_demo = pd.read_csv('/content/aadhar_demographic_cleaned.csv')

# 2. CONVERT DATE (Bulletproof Method)
# errors='coerce' turns bad data into empty values instead of crashing
df_enroll['date'] = pd.to_datetime(df_enroll['date'], dayfirst=True, errors='coerce')
df_demo['date'] = pd.to_datetime(df_demo['date'], dayfirst=True, errors='coerce')

# Drop rows where the date couldn't be parsed
df_enroll = df_enroll.dropna(subset=['date'])
df_demo = df_demo.dropna(subset=['date'])

# 3. AGGREGATE BY DATE
daily_enroll = df_enroll.groupby('date')['total_enrolments'].sum().reset_index()
daily_demo = df_demo.groupby('date')['total_enrolments'].sum().reset_index()

# 4. PLOT LINE CHART 
plt.figure(figsize=(15, 6))
sns.set_style("whitegrid")

plt.plot(daily_enroll['date'], daily_enroll['total_enrolments'], 
         label='New Enrolments (Growth)', color='#28a745', linewidth=2.5)
plt.plot(daily_demo['date'], daily_demo['total_enrolments'], 
         label='Demographic Updates (Maintenance)', color='#003366', linewidth=2.5)

# Formatting
plt.title('CHART A: PFTP - Temporal Volatility Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Total Daily Transactions', fontsize=12)
plt.legend(frameon=True, loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()