import numpy as np
import matplotlib.pyplot as plt
import math

class GradientDescent:
    Dm = 0
    Dc = 0
    lr = 0.0005
    n = 10
    i = 0
    x = np.linspace(1, 10, n)
    m = -1
    c = 0
    y = m * x + c
    epochs = 1000
    x_coordinates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_coordinates = [2, 3, 7, 8, 12, 13, 12, 18, 18, 21]
    #x_coordinates = [i / 10 for i in range(n)]
    #y_coordinates = [i / 10 for i in range(n)]

    def loss_function (self, x_coordinates, y_coordinates, y, i, n):
        output = 0
        for i in range(n):
            output += (y_coordinates[i] - y[i]) ** 2
        output = output / n
        return output

    def slope_update (self, m, x_coordinates, y_coordinates, y,  lr, n, Dm):
        for i in range(n):
            Dm += x_coordinates[i] * (y_coordinates[i] - y[i])
        Dm = -2 * Dm / n
        m = m - lr * (Dm)
        return m

    def y_intercept_update (self, c, y_coordinates, y, lr, n, Dc) :
        for i in range(n):
            Dc += y_coordinates[i] - y[i]
        Dc = -2 * Dc / n
        c = c - lr * (Dc)
        return c

if __name__ == '__main__':
    obj = GradientDescent()
    for j in range(obj.epochs):
        obj.m = obj.slope_update(obj.m, obj.x_coordinates, obj.y_coordinates, obj.y, obj.lr, obj.n, obj.Dm)
        obj.c = obj.y_intercept_update(obj.c, obj.y_coordinates, obj.y, obj.lr, obj.n, obj.Dc)
        obj.y = obj.x * obj.m + obj.c
    print(obj.m)
    print(obj.c)
    plt.scatter(obj.x_coordinates, obj.y_coordinates)
    plt.scatter(obj.x, obj.y)
    plt.show()
