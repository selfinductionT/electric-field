import numpy as np
import spcalc


def read_input(input_file):
    """It takes input file and returns a list of particles"""
    particles = []
    with open(input_file) as f:
        for line in f:
            if len(line.strip()) == 0 or line[0] == '#':
                continue
            else:
                particle = parse(line)
                particles.append(particle)
    return particles


def parse(line):
    """Constucts particle from line in input file"""
    line = line.split()
    q = float(line[0])
    r = np.array([
        float(line[1]),
        float(line[2])
    ])
    return spcalc.Particle(q, r)


if __name__ == "__main__":
    print("This module is not for direct call!")
