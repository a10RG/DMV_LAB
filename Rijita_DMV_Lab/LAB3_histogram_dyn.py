import matplotlib.pyplot as plt
data = list(map(float, input("Enter data values separated by space: ").split()))
bins = int(input("Enter number of bins: "))
plt.hist(
    data,
    bins=bins,
    edgecolor="white",  
    linewidth=1         
)
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.title("Dynamic Histogram")
plt.show()

