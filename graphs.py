import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv(r"/Users/Alex/Downloads/bigdata.csv", header=None, index_col=0)

sns.set(style="darkgrid")
fig, axs = plt.subplots(2, 2, figsize=(7, 7))

sns.histplot(data.loc['Ed Sheeran'], bins = 11, binwidth = 1, binrange = (-0.5, 10.5), kde = True, ax=axs[0, 0])
sns.histplot(data.loc['Queen'], bins = 11, binwidth = 1, binrange = (-0.5, 10.5), kde = True, ax=axs[0, 1])
sns.histplot(data.loc['SZA'], bins = 11, binwidth = 1, binrange = (-0.5, 10.5), kde = True, ax=axs[1, 0])
sns.histplot(data.loc['The Beatles'], bins = 11, binwidth = 1, binrange = (-0.5, 10.5), kde = True, ax=axs[1, 1])

plt.show()
