import numpy as np
import spcalc


def read_input(input_file):
    points = []
    with open(input_file) as f:
        for line in f:
            if len(line.strip()) == 0 or line[0] == '#':
                continue
            else:
                data = parse(line)
                point = spcalc.Point(data)
                points.append(point)


def parse(line):
    line = line.split()
    q = float(line[0])
    r = np.array([
        float(line[1]),
        float(line[2])
    ])
    return spcalc.Point(q, r)


if __name__ == "__main__":
    print("This module is not for direct call!")
