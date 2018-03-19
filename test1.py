import matplotlib.pyplot as plt

x1 = [1,2,3]
y1 = [5,7,4]

x2 = [1,2,3]
y2 = [3,4,2]
plt.plot(x1,y1, label = '1')
plt.plot(x2,y2, label = '2')
plt.xlabel('Plot number')
plt.ylabel('Var')
plt.title('Graph')
plt.legend()
plt.show()

