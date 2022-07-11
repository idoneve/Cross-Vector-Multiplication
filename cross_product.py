import numpy as np
import matplotlib.pyplot as plt

def cross_mult(v1, v2):
    v3 = [0, 0, 0]
    v3[0] = (v1[1] * v2[2]) - (v1[2] * v2[1])
    v3[1] = (v1[2] * v2[0]) - (v1[0] * v2[2])
    v3[2] = (v1[0] * v2[1]) - (v1[1] * v2[0])
    return v3

ax = plt.axes(projection="3d")

v1 = [3, -1, 4]
v2 = [2, 5, 1]
v3 = cross_mult(v1, v2)

print(f'{v1}, {v2}, {v3}')

ax.plot3D([0, v1[0]], [0, v1[1]], [0, v1[2]])
ax.plot3D([0, v2[0]], [0, v2[1]], [0, v2[2]])
ax.plot3D([0, v3[0]], [0, v3[1]], [0, v3[2]])

plt.xlim([-10, 10])
plt.ylim([-10, 10])
ax.set_zlim([-10, 10])

plt.grid()
plt.show()
