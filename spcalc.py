import numpy as np

k = 8.9


class Point():
    def __init__(self, q, r):
        self.q = q
        self.r = r

    def field_made(self, radius_vector):
        ro = np.linalg.norm(radius_vector)  # module of distance
        F = (k*self.q/ro**3) * radius_vector
        return F
