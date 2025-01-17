import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpMat import OpMat
from Piramide import Piramide


def Axis():
    glLineWidth(3.0)
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)  # Eje X en rojo
    glVertex3f(-500.0, 0.0, 0.0)
    glVertex3f(500.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)  # Eje Y en verde
    glVertex3f(0.0, -500.0, 0.0)
    glVertex3f(0.0, 500.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)  # Eje Z en azul
    glVertex3f(0.0, 0.0, -500.0)
    glVertex3f(0.0, 0.0, 500.0)

    glEnd()


def Init():
    pygame.init()
    pygame.display.set_mode((900, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Rotación Libre 3D")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 900 / 600, 0.01, 500.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


def main():
    op3D = OpMat()
    piramide = Piramide(op3D)
    Init()

    # Set initial rotation angles
    angle_x = 0
    angle_y = 0
    angle_z = 0

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Rotación continua
        angle_x += 1  # Increment for X-axis rotation
        angle_y += 0.5  # Increment for Y-axis rotation
        angle_z += 0.2  # Increment for Z-axis rotation

        # Actualizar matriz de transformación con resultados nuevos
        op3D.A = np.identity(4)  # Reset the transformation matrix
        op3D.rotate(angle_x, 1, 0, 0)  # Rotate around X axis
        op3D.rotate(angle_y, 0, 1, 0)  # Rotate around Y axis
        op3D.rotate(angle_z, 0, 0, 1)  # Rotate around Z axis

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Axis()

        piramide.render()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
