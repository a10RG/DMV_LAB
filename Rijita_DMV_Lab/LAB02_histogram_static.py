import matplotlib.pyplot as plt
data = [
    45, 47, 48, 49, 50, 51, 52, 53, 54, 55,
    56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
    66, 67, 68, 69, 70, 71, 72, 73, 74, 75
]
plt.hist(
    data,
    bins=6,
    edgecolor="white", 
    linewidth=1       
)

plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.title("Histogram")

plt.show()
