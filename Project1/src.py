import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

kaggle_data = pd.read_csv("tourism_data.csv")

i = 0
count = []
ind = []
while(i<kaggle_data.shape[0]):
    row_count = np.sum(kaggle.iloc[i].isna())
    count.append(row_count)
    if(row_count == 0):
        ind.append(i)
    i += 1

cleaned = kaggle.iloc[ind]
cleaned.reset_index(drop=True) # resetting the index 