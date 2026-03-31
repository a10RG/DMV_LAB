import numpy as np
import matplotlib.pyplot as plt

# Create Cluster 1 (positive correlation)
x1 = np.random.normal(5, 1, 50)
y1 = 2 * x1 + np.random.normal(0, 1, 50)

# Create Cluster 2
x2 = np.random.normal(12, 1, 40)
y2 = 2 * x2 + np.random.normal(0, 1, 40)

# Combine clusters
x = np.concatenate((x1, x2))
y = np.concatenate((y1, y2))

# Add outliers
x_outlier = np.array([2, 18])
y_outlier = np.array([30, 5])

x = np.concatenate((x, x_outlier))
y = np.concatenate((y, y_outlier))

# Scatter plot
plt.scatter(x, y)

plt.title("Scatter Plot with Clusters, Outliers and Positive Correlation")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()
