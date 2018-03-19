import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,2,6,4,2,6,3,9,5,1]
y2 = [9,3,4,7,1,3,5,7,4,2]


plt.plot([],[],color='r', label = 'y')
plt.plot([],[],color='b', label = 'y2')
plt.stackplot(x, y,y2, colors = ['r','b'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph')
plt.legend()
plt.show()
plt.close()
