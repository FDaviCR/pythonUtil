import matplotlib.pyplot as plt
'''
plt.plot([1,2,3,4],[1,4,9,16])
plt.plot([1,3,4,5],[0,4,10,22])
plt.ylabel('QUADRADOS')
plt.xlabel('VALORES')
plt.show()
'''
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from random import randint

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

points = []
last = 0
bound = 100
for i in range(0, 100):
  last += randint(-bound, bound)
  points.append(last)
  
ax.plot(points)
fig.savefig('graph.png')
