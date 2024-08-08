import matplotlib.pyplot as plt
import pandas as  pd
import numpy as  np

header = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names = header)
# # 행, 열 알아보기
# print(data.shape)
# print(data.describe())

# data.describe().to_csv('./results/pima_describe.csv')

corr = data.corr(method='pearson')

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap = 'coolwarm', vmin = -1, vmax = 1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(header)
ax.set_yticklabels(header)
plt.show()
plt.savefig('./results/corr.png')

