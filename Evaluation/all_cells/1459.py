import pandas as pd
import numpy as np
x = 2
y = 3.5
z = 'Hello'
data = np.array([5,2,3])
df = pd.DataFrame()
# append each data item as a new row
#ignore_index ensures the index remains sequential after each append.
df = df.append({'Data':x}, ignore_index=True)
df = df.append({'Data':y}, ignore_index=True)
df = df.append({'Data':z}, ignore_index=True)
df = df.append({'Data':data}, ignore_index=True)
print(df)
# Save it to file called "some_stuff.csv" in comma delimited (csv) format.
#  index field is set to False so that we don't have row indices saved in the file.
df.to_csv('some_stuff.csv', index=False)