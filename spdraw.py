import numpy as np
from matplotlib import pyplot as plt


def draw(field, output_file, norm=False):
    if not field.normalised and norm is True:
        field.normalise()

    X_minus, Y_minus = [], []
    X_plus, Y_plus = [], []
    for particle in field.particles:
        for line in field.lines[particle]:
            X = []
            Y = []
            for point in line:
                X.append(point[0])
                Y.append(point[1])
            plt.plot(X, Y, color="grey")

        x, y = particle.r
        if np.sign(particle.q) == 1:
            X_plus.append(x)
            Y_plus.append(y)
        else:
            X_minus.append(x)
            Y_minus.append(y)
    plt.scatter(X_plus, Y_plus, color="r")
    plt.scatter(X_minus, Y_minus, color="b")
    plt.savefig(output_file)
