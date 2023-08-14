print("Total Number of Earthquakes: ", sum(bigOccurences))

plt.figure(figsize = (15,5))

barWidth = 0.4
plt.subplot(1,2,1)
plt.bar(bigMagnitudes, bigOccurences, barWidth)
plt.title("Histogram of Magnitude Occurrences With Varying Mass")
plt.xlabel("Magnitude")
plt.ylabel("Number of Occurrences")

plt.subplot(1,2,2)

plt.semilogy(bigMagnitudes, bigOccurences, "b o", label = "Number of Magnitude Occurences")
plt.semilogy(fitX, fitY, label = "Fitted Function: $P(M) = 99e^{-0.632 M}$")
plt.title("Logarithmic Correlation Between Magnitude and Number of Occurrences")
plt.xlabel("Magnitude")
plt.ylabel("Number of Occurrences")
plt.legend(loc = "best")
plt.show()