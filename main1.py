import numpy as np
import matplotlib.pyplot as plt
import math

class GradientDescentParabola:
    da = 0
    db = 0
    dc = 0
    lr = 0.00005
    a = -69
    b = 420
    c = 17
    n = 10
    i = 0
    x = np.linspace(1, 10, n)
    y = (a * (x ** 2)) + b * x + c
    epochs = 500000
    x_coordinates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_coordinates = [6, 1, -2, -3, -2, 1, 6, 13, 22, 33]

    def a_update (self, x_coordinates, y_coordinates, y, lr, n, da, a):
        for i in range(n):
            da += (y_coordinates[i] - y[i]) * x_coordinates[i] * x_coordinates[i]
        da = -2 * da / n
        a -= lr * da
        return a

    def b_update (self, x_coordinates, y_coordinates, y, lr, n, db, b):
        for i in range(n):
            db += (y_coordinates[i] - y[i]) * x_coordinates[i]
        db = -2 * db / n
        b -= lr * db
        return b

    def c_update (self, y_coordinate, y, lr, n, dc, c):
        for i in range(n):
            dc += y_coordinate[i] - y[i]
        dc = -2 * dc / n
        c -= lr * dc
        return c

if __name__ == '__main__':
    obj1 = GradientDescentParabola()
    for j in range(obj1.epochs):
        #print(obj1.a)
        #print(obj1.b)
        #print(obj1.c)
        if(j % 1000 == 0):
            progress = (j + 1000) * 100 / obj1.epochs
            print('Progress:', progress, '%')
        obj1.a = obj1.a_update(obj1.x_coordinates, obj1.y_coordinates, obj1.y, obj1.lr, obj1.n, obj1.da, obj1.a)
        obj1.b = obj1.b_update(obj1.x_coordinates, obj1.y_coordinates, obj1.y, obj1.lr, obj1.n, obj1.db, obj1.b)
        obj1.c = obj1.c_update(obj1.y_coordinates, obj1.y, obj1.lr, obj1.n, obj1.dc, obj1.c)
        obj1.y = obj1.a * obj1.x * obj1.x + obj1.b * obj1.x + obj1.c
    print(obj1.a)
    print(obj1.b)
    print(obj1.c)
    plt.scatter(obj1.x_coordinates, obj1.y_coordinates)
    plt.scatter(obj1.x, obj1.y)
    plt.show()