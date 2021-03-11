# Gráfico de dispersão 3D / Scartter plot 3D
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
# definindo os eixos: altura, comprimento e profuncidade.
x = [1, 2, 3]
y = [1, 2, 3]
z = [1, 2, 3]
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter3D(x, y, z, color="purple",s=250)
plt.show()