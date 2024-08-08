import matplotlib.pyplot as plt
import pandas as  pd
import numpy as  np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

header = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names = header)

array = data.values
X = array[:, 0:8]
Y = array[:, 8]
print(X.shape, Y.shape)
scaler = binarizer(threshold=0.5)
rescled_X = scaler.fit_transform(X)
print(rescled_X)


# scaler = StandardScaler()
# rescaled_X = scaler.fit_transform(X)
# print(rescaled_X)

# scaler = MinMaxScaler(feature_range=(0,1))
# rescaled_X = scaler.transform(X)
# print(rescaled_X)


# plt.clf()
# pd.plotting.scatter_matrix(data)
# plt.savefig("./results/scatter.png")

# data.hist(figsize=(12,10), bins=5)
# plt.tight_layout()
# plt.savefig("./results/histogram.png")

# data.plot(kind="box", subplots=True, figsize=(12,10), layout=(3,3), sharex = False, sharey = False)
# plt.savefig("./results/boxplot.png")

# 밀도 계산
# data.plot(kind='density', figsize =(12,10), subplots = True, layout=(3,3), sharex = False)
# plt.savefig("./results/density_plot.png")

