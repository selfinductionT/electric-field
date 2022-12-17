# import numpy as np
from matplotlib import pyplot as plt
# import spcalc


def draw(field):
    if not field.normalised:
        field.normalise()
    for particle in field.particles:
        for line in field.lines[particle]:
            X = []
            Y = []
            for point in line:
                X.append(int(point[0]))
                Y.append(int(point[1]))
            plt.plot(X, Y, color="r")
    plt.show()
