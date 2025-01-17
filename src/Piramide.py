import numpy as np
from OpenGL.GL import *


class Piramide:
    def __init__(self, op):
        self.points = np.array(
            [
                [1.0, 0.0, 1.0, 1.0],
                [1.0, 0.0, -1.0, 1.0],
                [-1.0, 0.0, -1.0, 1.0],
                [-1.0, 0.0, 1.0, 1.0],
                [0.0, 3.0, 0.0, 1.0],
            ]
        )
        self.op3D = op

    def update(self):
        pass

    def render(self):
        pointsR = self.op3D.mult_Points(self.points)
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glVertex3f(pointsR[0][0], pointsR[0][1], pointsR[0][2])
        glVertex3f(pointsR[1][0], pointsR[1][1], pointsR[1][2])
        glVertex3f(pointsR[2][0], pointsR[2][1], pointsR[2][2])
        glVertex3f(pointsR[3][0], pointsR[3][1], pointsR[3][2])
        glEnd()

        glBegin(GL_LINES)
        for i in range(4):
            glVertex3f(pointsR[i][0], pointsR[i][1], pointsR[i][2])
            glVertex3f(pointsR[4][0], pointsR[4][1], pointsR[4][2])
        glEnd()
