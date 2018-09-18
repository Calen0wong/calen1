import numpy as np
import matplotlib.pyplot as plt


# 创建一个8*6大小的figure，并设置每英寸80个像素点，dpi是像素点
plt.figure(figsize=(8, 6), dpi=80)

# 在1*1的位置之上创建一个subplot
plt.subplot(111)

# 从np中获取需要的数据，通常是获取横轴的数据。
# linspace(-np.pi, np.pi, 10, endpoint=True)从-π到π中均匀的选取10个点
x1 = np.linspace(-np.pi, np.pi, 144, endpoint=True)
x2 = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x1), np.sin(2*x2)  # c是cos()函数，s是sin()函数。
# 而通过的np的cos和sin计算公式可以得到相应的y值
plt.plot(x1, c, color='blue', linewidth=2.5, linestyle="-")  # 绘制c曲线
plt.plot(x2, s, color="red",  linewidth=2.5, linestyle="-")  # 绘制s曲线
# plt.xlim(-2, 2)
# plt.ylim(-1, 1)
plt.xlim(x1.min()*0.5, x1.max()*0.5)  # x轴下标范围，但是不用显示
plt.ylim(c.min()*0.5, c.max()*0.5)  # y轴下标范围，不用显示
plt.xticks(np.linspace(-4, 4, 10, endpoint=True))
plt.yticks(np.linspace(-1, 1, 10, endpoint=True))
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# plt.yticks([-1, 0, +1])
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r"$-\pi$", r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$"])
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])
plt.show()




