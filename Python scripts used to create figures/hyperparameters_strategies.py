import matplotlib.pyplot as plt
from pathlib import Path


Optuna_library = 1
Bayesian_optimization = 1
Grid_search = 8
Not_reported = 36

values = [Optuna_library, Bayesian_optimization,  Grid_search, Not_reported]
categories = ['Optuna library', 'Bayesian optimization', 'Grid search', 'Not reported']

# Sort data by values descending

sorted_values, sorted_categories = values, categories

# Plot
fig, ax = plt.subplots(figsize=(6, 2))
bars = ax.barh(sorted_categories, sorted_values, color=["#1f77b4", "#1f77b4", "#1f77b4", '#c62828'])

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
plt.xlabel("Number of papers")
path = Path("Python scripts used to create figures")
path.mkdir(parents=True, exist_ok=True)
plt.tight_layout()
plt.savefig("hyperparameter_strategies.pdf")
plt.show()