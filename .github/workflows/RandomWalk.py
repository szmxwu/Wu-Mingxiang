from random import choice
import matplotlib.pyplot as plt
% matplotlib inline
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
class RandomWalk():
    '''一个生成随机漫步数据的类'''
    def __init__(self,num_points=5000):
        '''初始化随机漫步的属性'''
        self.num_points = num_points

        #所有的随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        '''计算随机漫步的所有点'''

        # 不断漫步，直到列表到达指定长度
        while len(self.x_values)<self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction*x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的x和y值
            next_x = self.x_values[-1]+x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
#创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk(50000)
rw.fill_walk()
#print(rw.x_values)
point_numbers=list(range(rw.num_points))

plt.figure(dpi=128,figsize=(10,6))
plt.scatter(rw.x_values,rw.y_values,s=5,c=point_numbers,cmap=plt.cm.RdBu,edgecolors='none')
