import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Load the datasets (Colab paths provided)
df_enroll = pd.read_csv('/content/aadhaar_enrolment_fully_cleaned.csv')

# 2. Data Preparation: Aggregate total enrolments by District and State
# This identifies the total service output per geographic unit
spatial_data = df_enroll.groupby(['state', 'district'])['total_enrolments'].sum().reset_index()

# 3. Define the "Disparity Scale" (Deciles)
# We divide all districts in India into 10 groups (deciles) based on performance
# Decile 1 = Bottom 10% (Service Deserts)
# Decile 10 = Top 10% (Service Hubs)
spatial_data['decile'] = pd.qcut(spatial_data['total_enrolments'], 10, labels=False) + 1

# 4. Create the Heatmap Matrix
# We count how many districts in each state fall into each performance decile
heatmap_matrix = spatial_data.groupby(['state', 'decile']).size().unstack(fill_value=0)

# 5. Normalize the data (Percentage of Districts per State)
# This allows us to compare a large state like UP with a smaller state like Punjab fairly
heatmap_norm = heatmap_matrix.div(heatmap_matrix.sum(axis=1), axis=0) * 100

# 6. Filtering for Clarity: Focus on the top 20 states by volume
top_states = df_enroll.groupby('state')['total_enrolments'].sum().nlargest(20).index
heatmap_final = heatmap_norm.loc[top_states]

# 7. Plotting the "Diagnostic Visual"
plt.figure(figsize=(16, 10))
sns.set_context("talk")

# Using a Diverging color map: Red (Low/Desert) -> Yellow -> Green (High/Hub)
ax = sns.heatmap(
    heatmap_final, 
    annot=True, 
    fmt=".1f", 
    cmap="RdYlGn", 
    linewidths=.5,
    cbar_kws={'label': '% of Districts in State'}
)

# Formatting the Chart
plt.title('Chart B: Spatial Disparity Heatmap (DSDM)\nIdentifying "Service Deserts" (Red) vs "Service Hubs" (Green)', 
          fontsize=20, pad=20, fontweight='bold')
plt.xlabel('Enrolment Performance Decile (1 = Lowest Activity | 10 = Highest Activity)', fontsize=14)
plt.ylabel('State (Top 20 by Volume)', fontsize=14)

# Customizing the X-axis labels to explain the logic
plt.xticks(np.arange(10) + 0.5, [f'D{i+1}' for i in range(10)])
plt.tight_layout()
plt.show()

# Optional: List the Absolute "Service Deserts" for Policy Action
print("\n--- TOP 10 CRITICAL SERVICE DESERTS (Action Required) ---")
deserts = spatial_data[spatial_data['decile'] == 1].sort_values(by='total_enrolments').head(10)
print(deserts[['state', 'district', 'total_enrolments']])