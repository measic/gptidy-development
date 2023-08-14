import pandas as pd
import numpy as np

#data_streamer = ReutersStreamReader('reuters').iterdocs()
#y = len(list(data_streamer))
#print(y)

data_streamer = ReutersStreamReader('reuters').iterdocs()
data = get_minibatch(data_streamer, None)
print("number of labeled documents in dataset ",data.count()[0])

#type(data)
