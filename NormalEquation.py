import numpy as np
import matplotlib.pyplot as plt
import math


class NormalEquation:
    n = 10
    m = 0
    c = 0
    x_coordinates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_coordinates = [2, 3, 7, 8, 12, 13, 12, 18, 18, 21]
    x = np.linspace(1, 10, n)


if __name__ == '__main__':
    obj = NormalEquation()
    X = np.zeros((10, 2))
    Y = np.zeros((10, 1))
    #print(X)
    result_matrix = np.zeros((2, 1))
    x_transpose = np.zeros((2, 10))
    for i in range(10):
        X[i][0] = 1
    for i in range(10):
        X[i][1] = obj.x_coordinates[i]
    for i in range(10):
        Y[i][0] = obj.y_coordinates[i]
    x_transpose = np.transpose(X)
    result_matrix = np.dot(np.dot(np.linalg.inv(np.dot(x_transpose, X)), x_transpose), Y)
    #print(result_matrix)
    obj.c = result_matrix[0][0]
    obj.m = result_matrix[1][0]
    print(obj.m)
    print(obj.c)
    plt.scatter(obj.x_coordinates, obj.y_coordinates)
    y = obj.m * obj.x + obj.c
    plt.plot(obj.x, y)
    plt.show()
