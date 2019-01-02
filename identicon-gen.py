'''
identicon generator using python which creates a 5x5 identicon
Naveena
'''

import hashlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
test= 'hello world'
print test
a = hashlib.md5(test.encode()).hexdigest()
bg_cc ='#'+ a[:6]
cc = '#' + a[6:12]
block = a[7:32]
b = []
c = []

for i in range(0, 25):
    c.append(int(block[i], 16) )
    if( c[i] > 7):
        b.append(1)
    else:
        b.append(0)

b = np.reshape(b, (5, 5))


cmap = colors.ListedColormap([bg_cc, cc])
fig, ax = plt.subplots()
ax.imshow(b, cmap=cmap)
ax.grid(which='major', axis='both', linestyle='-', linewidth=2)
ax.axis('off')

plt.show()

