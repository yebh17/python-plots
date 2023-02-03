import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Generate data
data = np.random.normal(0, 1, 1000)

# Plot histogram
sns.distplot(data, kde=False, bins=30, color='blue', hist_kws={'edgecolor': 'black'})

# Show plot
plt.show()