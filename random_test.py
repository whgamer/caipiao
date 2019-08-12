import random
import numpy as np
position =0
walk =[position]
steps =1000
for i in range(steps):#xrange python3  合并为range
    step = 1 if random.randint(0,1) else -1
    position +=step
    walk.append(position)
samples =np.random.normal(size =(10,10))
print(samples)