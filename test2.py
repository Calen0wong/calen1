from matplotlib import pyplot as plt

# 创建x轴和y轴
x = [0, 10]
y = [0, 20]
# 创建绘图对象
plt.figure()
# 绘制图像
plt.plot(x, y)
# 给两条轴添加说明
plt.xlabel("time(s)")
plt.ylabel("distance(m)")
# 保存图片
plt.savefig("easy_plot.png")