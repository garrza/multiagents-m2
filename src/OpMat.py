import numpy as np


class OpMat:
    def __init__(self):
        self.A = np.identity(4)

    def translate(self, tx, ty, tz):
        T = np.identity(4)
        T[0][3] = tx
        T[1][3] = ty
        T[2][3] = tz
        self.A = T @ self.A

    def rotate(self, theta, x, y, z):
        radians = np.radians(theta)
        axis = np.array([x, y, z])
        axis = axis / np.linalg.norm(axis)

        ux, uy, uz = axis
        cos_t = np.cos(radians)
        sin_t = np.sin(radians)

        # Rotation matrix components
        R = np.array(
            [
                [
                    cos_t + ux**2 * (1 - cos_t),
                    ux * uy * (1 - cos_t) - uz * sin_t,
                    ux * uz * (1 - cos_t) + uy * sin_t,
                    0,
                ],
                [
                    uy * ux * (1 - cos_t) + uz * sin_t,
                    cos_t + uy**2 * (1 - cos_t),
                    uy * uz * (1 - cos_t) - ux * sin_t,
                    0,
                ],
                [
                    uz * ux * (1 - cos_t) - uy * sin_t,
                    uz * uy * (1 - cos_t) + ux * sin_t,
                    cos_t + uz**2 * (1 - cos_t),
                    0,
                ],
                [0, 0, 0, 1],
            ]
        )
        self.A = R @ self.A

    def mult_Points(self, points):
        pointsR = (self.A @ points.T).T
        return pointsR
