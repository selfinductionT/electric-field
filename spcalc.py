# вместо why должен быть for в calc()
# неплохо бы обработать то, что две линии рядом могут быть одной
# + сделать регулирование размера окна, output file

import numpy as np

k = 8.988e9


class Particle():
    def __init__(self, q, r):
        self.q = q
        self.r = r

    def field_made(self, radius_vector):
        """This finction calculates field at the point"""
        delta_r = radius_vector - self.r
        ro = np.linalg.norm(delta_r)  # module of distance
        F = (k*self.q/ro**3) * delta_r
        return F


class Field():
    def __init__(self, particles):
        self.size = Field.construct_size(particles)
        self.particles = particles
        self.normalised = False
        self.lines = {}
        # we will calculate 4 lines for each particle
        # lines would start from 4 points on the distance delta from a particle
        for particle in particles:
            delta = self.size.min() / 1e3
            # 4 lines for each particle
            self.lines[particle] = [
                [particle.r + np.array([delta, 0])],
                [particle.r + np.array([-delta, 0])],
                [particle.r + np.array([0, delta])],
                [particle.r + np.array([0, -delta])],
            ]

    def construct_size(particles):
        xs = []
        ys = []
        for particle in particles:
            xs.append(particle.r[0])
            ys.append(particle.r[1])
        return np.array([max(xs), max(ys)])

    def at_point(self, r_point):
        F = np.zeros(2)
        for particle in self.particles:
            F += particle.field_made(r_point)
        return F

    def calc(self):
        # надо вайл вместо фор
        for i in range(2000):
            self.step_calc()

    def step_calc(self):
        for particle in self.particles:
            for line in self.lines[particle]:
                point = line[-1]
                E = self.at_point(point)
                E /= np.linalg.norm(E)
                E *= np.max(self.size) * 1e-3
                if np.sign(particle.q) == 1:
                    new_point = point + E
                else:
                    new_point = point - E
                line.append(new_point)

    def normalise(self):
        size = np.array([255, 255])
        k = size / self.size
        for particle in self.particles:
            particle.r *= k
            for line in self.lines[particle]:
                for point in line:
                    point *= k
        self.normilised = True


if __name__ == "__main__":
    print("This module is not for direct call!")
