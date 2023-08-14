Magnitudes, Occurrences = countMagnitudes (earthquakeMagnitudes)
barWidth = 0.4
plt.bar(Magnitudes, Occurrences, barWidth)
plt.title("Histogram of Magnitude Occurrences")
plt.xlabel("Magnitude")
plt.ylabel("Number of Occurrences")