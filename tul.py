import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Logic: Bivariate Ratio Analysis using Demographic Dataset
df_demo = pd.read_csv('aadhar_demographic_cleaned.csv')
tul = df_demo.groupby('state').agg({'demo_age_17_': 'sum', 'demo_age_5_17': 'sum'}).reset_index()
tul['TUL_Ratio'] = (tul['demo_age_17_'] + 1) / (tul['demo_age_5_17'] + 1)
plt.figure(figsize=(10, 5))
sns.barplot(data=tul.nlargest(10, 'TUL_Ratio'), x='TUL_Ratio', y='state', palette='magma')
plt.title('TUL: Identity Silence (Adult-to-Teen Lag)', fontsize=14, fontweight='bold')
plt.show()