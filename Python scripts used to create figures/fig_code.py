import matplotlib.pyplot as plt
from pathlib import Path


proposed_model_code = 46 
data_preprocessing = 32
baseline_models = 12
hyperparameter_tuning_code = 8

values = [proposed_model_code, baseline_models, data_preprocessing, hyperparameter_tuning_code]
categories = ['Proposed model', 'Baseline models', 'Data Preprocessing' , 'Hyperparameter tuning']

# Sort data by values descending
sorted_data = sorted(zip(values, categories), reverse=True)
sorted_values, sorted_categories = zip(*sorted_data)

# Plot

fig, ax = plt.subplots(figsize=(6, 2))
bars = ax.barh(categories, values, color = "#1f77b4")

# Flip the y-axis so largest value is at the top
ax.invert_yaxis()
# Add values inside bars
for bar in bars:
    width = bar.get_width()
    ax.text(width / 2,                       # x = middle of the bar
            bar.get_y() + bar.get_height()/2,  # y = middle of the bar
            str(width),                      # label text
            ha='center', va='center',        # horizontal and vertical align center
            color='white')       # adjust font size/color as needed

# Labels and styling
ax.set_xlim(0, max(sorted_values) + 10)
path = Path("Python scripts used to create figures")
path.mkdir(parents=True, exist_ok=True)
plt.tight_layout()
plt.savefig("code.pdf")
plt.show()