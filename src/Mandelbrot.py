import numpy as np
import matplotlib.pyplot as plt


print("Veuillez attendre plusieur minute pour que le set Mandelbrot calcule")

def mandelbrot(c, maxiter):
    z = 0
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z **3+ c
    return maxiter
        
        
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, width)
    mset = np.zeros((width, height))
    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i,j] = mandelbrot(c, maxiter)
    return mset

xmin , xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
maxiter = 100

img = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter)

plt.imshow(img, cmap='hot', extent=[xmin, xmax, ymin, ymax])
plt.colorbar()

plt.show()