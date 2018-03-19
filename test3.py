import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,2,6,4,2,6,3,9,5,1]
y2 = [9,3,4,7,1,3,5,7,4,2]
plt.scatter(x,y,label = 'scatter', marker = '*', color = 'r')
plt.scatter(x,y2,label = 'scatter', marker = '*', color = 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plots')
plt.legend()
plt.show()
plt.close()
