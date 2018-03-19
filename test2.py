import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [5,2,6,4,2]

x2 = [1,3,5,7,9]
y2 = [7,4,1,6,3]

plt.bar(x,y, label = '1', color = 'r')
plt.bar(x2,y2, label = '2', color = 'b')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Bar charts')
plt.legend()
plt.show()

plt.hist(y2,x2,histtype = 'bar', rwidth=0.8)
plt.show()
