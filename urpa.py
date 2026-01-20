import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Logic: Density Distribution (KDE) to compare Proactive vs Reactive behavior
df_enroll = pd.read_csv('aadhaar_enrolment_fully_cleaned.csv')
urban_list = ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune']
df_enroll['category'] = df_enroll['district'].apply(lambda x: 'Urban (Proactive)' if any(u in str(x) for u in urban_list) else 'Rural (Reactive)')

velocity = df_enroll.groupby(['category', 'district', 'date'])['total_enrolments'].sum().reset_index()
velocity_avg = velocity.groupby(['category', 'district'])['total_enrolments'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.kdeplot(data=velocity_avg, x='total_enrolments', hue='category', fill=True, palette='viridis', common_norm=False)
plt.xlim(0, 1000)
plt.title('URPA: Behavioral Divergence (Update Velocity)', fontsize=14, fontweight='bold')
plt.show()