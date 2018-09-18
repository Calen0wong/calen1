import matplotlib.pyplot as plt

data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}  # 数据是以字典的形式展示
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 6, figsize=(9, 3))  # subplots(1,3)是指生成几个图形
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[5].plot(names, values)
fig.suptitle('Categorical Plotting')
plt.show()