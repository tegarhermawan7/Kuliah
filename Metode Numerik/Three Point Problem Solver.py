import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

pointA = "56, 324, 296"
pointB = "286, 386, 176"
pointC = "114, 428, 225"

#Tegar Hermawan Tahir
#22/504673/TK/55211
#Kelas A


def calculate(pointA, pointB, pointC):
    result = ""

    coordsA = list(map(float, pointA.split(',')))
    coordsB = list(map(float, pointB.split(',')))
    coordsC = list(map(float, pointC.split(',')))

    result += "Titik A : {}\n".format(coordsA)
    result += "Titik B : {}\n".format(coordsB)
    result += "Titik C : {}\n\n".format(coordsC)

    N = [
        (coordsB[1] - coordsA[1]) * (coordsC[2] - coordsA[2]) - (coordsB[2] - coordsA[2]) * (coordsC[1] - coordsA[1]),
        (coordsB[2] - coordsA[2]) * (coordsC[0] - coordsA[0]) - (coordsB[0] - coordsA[0]) * (coordsC[2] - coordsA[2]),
        (coordsB[0] - coordsA[0]) * (coordsC[1] - coordsA[1]) - (coordsB[1] - coordsA[1]) * (coordsC[0] - coordsA[0])
    ]
    
    result += "Vektor Normal Bidang (N): {}\n\n".format(N)

    lengthN = (N[0] ** 2 + N[1] ** 2 + N[2] ** 2) ** 0.5
    normalizedN = [N[0] / lengthN, N[1] / lengthN, N[2] / lengthN]
    result += "Normalisasi Vektor N: {}\n\n".format(normalizedN)

    D = - (normalizedN[0] * coordsA[0] + normalizedN[1] * coordsA[1] + normalizedN[2] * coordsA[2])
    result += "D : {:.3f}\n\n".format(D)
    
    result += "Persamaan Bidang: {:.3f}x + {:.3f}y + {:.3f}z + {:.3f} = 0\n\n".format(
        normalizedN[0], normalizedN[1], normalizedN[2], D)

    strike = (180 / math.pi) * math.atan2(normalizedN[1], normalizedN[0])
    result += "Strike (Azimuth): {:.2f} derajat\n\n".format(strike)

    dip = (180 / math.pi) * math.atan2((normalizedN[0] ** 2 + normalizedN[1] ** 2) ** 0.5, normalizedN[2])
    result += "Dip (Kemiringan): {:.2f} derajat\n".format(dip)
    
    return result, D, normalizedN  # Mengembalikan nilai D dan normalizedN


hasil_perhitungan, D, normalizedN = calculate(pointA, pointB, pointC)
print(hasil_perhitungan)

x = np.linspace(-100, 100, 2500)
y = np.linspace(-100, 100, 2500)
X, Y = np.meshgrid(x, y)

Z = (D - normalizedN[0] * X - normalizedN[1] * Y) / normalizedN[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
