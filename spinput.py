import numpy as np
import spcalc


def read_input(input_file):
    with open(input_file) as f:
        output_file = "output.png"
        datafile = "data.txt"

        for line in f:
            if len(line.strip()) == 0 or line[0] == '#':
                continue

            line = line.split()
            if line[0] == 'datafile':
                datafile = line[1]
            elif line[0] == 'output':
                output_file = line[1]

            data = read_data(datafile)
        return (data, output_file)


def read_data(datafile):
    """It takes datafile and returns a list of particles"""
    particles = []
    with open(datafile) as f:
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
