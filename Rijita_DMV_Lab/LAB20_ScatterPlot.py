import numpy as np
import matplotlib.pyplot as plt
# Create clusters
np.random.seed(10)
# Cluster 1
x1 = np.random.normal(100, 10, 40)
y1 = x1 * 0.3 + np.random.normal(0, 5, 40)
# Cluster 2
x2 = np.random.normal(300, 15, 40)
y2 = x2 * 0.3 + np.random.normal(0, 5, 40)
# Cluster 3
x3 = np.random.normal(600, 20, 40)
y3 = x3 * 0.3 + np.random.normal(0, 5, 40)
# Outliers
x_out = [900, 950]
y_out = [50, 250]
plt.figure(figsize=(8,6))
plt.scatter(x1, y1, color='blue', label="Cluster 1")
plt.scatter(x2, y2, color='green', label="Cluster 2")
plt.scatter(x3, y3, color='orange', label="Cluster 3")
plt.scatter(x_out, y_out, color='red', label="Outliers", s=120)
plt.title("Scatter Plot with Clusters, Outliers and Positive Correlation")
plt.xlabel("Revenue")
plt.ylabel("Net Profit")
plt.legend()
plt.grid(True)
plt.show()
