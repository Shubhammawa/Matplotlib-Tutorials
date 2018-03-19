import matplotlib.pyplot as plt

days = [1,2,3,4,5]

slices = [4,2,6,3,5]

activities = ['sleeping', 'eating','playing','studying','bathing']
cols = ['m','r','y','b','c']

plt.pie(slices, labels = activities, colors = cols,startangle = 0, shadow = True, explode =(0,0,0,0.3,0),
        autopct='%1.1f%%')
plt.title('pie chart')
plt.show()
