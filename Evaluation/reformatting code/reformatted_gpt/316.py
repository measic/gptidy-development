import matplotlib.pyplot as plt
import pandas as pd

top = df.groupby('breed').filter(lambda x: len(x) >= 20)
top['breed'].value_counts().plot(kind='bar')
plt.title('The Most Rated Breeds')