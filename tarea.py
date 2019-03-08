import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random
from math import * # trigonometry
import numpy
from PIL import Image
import sys
import time

[
    [-1, -1, 0],
    [-1, 0, 0],
    [-1, 1, 0],
    [0, 1, 0],
    [0, 0,0],
    [1, 0, 0],
    [1, -1, 0],
    [0, -1, 0]
    ]





X = [-1.0, -1.0, -1.0,  0.0,  0.0,  1.0,  1.0 ,  0.0]
Y = [-1.0,  0.0,  1.0,  1.0,  0.0,  0.0, -1.0 , -1.0]


def Cube():
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(X[0], Y[0],  0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(X[1], Y[1],  0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(X[4],  Y[4],  0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(X[7],  Y[7],  0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(X[1], Y[1],  0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(X[2], Y[2],  0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(X[3],  Y[3],  0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(X[4],  Y[4],  0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(X[7], Y[7],  0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(X[4], Y[4],  0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(X[5],  Y[5],  0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(X[6],  Y[6],  0.0)
    glEnd()


imagenes = ['test_0.png','test_1.png','test_2.png','test_3.png']
cantImage = len(imagenes)
#print(cantImage)

def loadTexture():
    aleatorio = random.randint(0,cantImage-1)
    #print(aleatorio)
    textureSurface = pygame.image.load(imagenes[aleatorio])
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def main():
    pygame.init()
    display = (1366,768)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|OPENGLBLIT)

    loadTexture()
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
    vertice = 0
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == KEYDOWN:
            if event.key == K_1:
                vertice = 0
            if event.key == K_2:
                vertice = 1
            if event.key == K_3:
                vertice = 2
            if event.key == K_4:
                vertice = 3
            if event.key == K_5:
                vertice = 4
            if event.key == K_6:
                vertice = 5
            if event.key == K_7:
                vertice = 6
            if event.key == K_8:
                vertice = 7

            if event.key == K_UP:
                Y[vertice] += 0.01
            if event.key == K_DOWN:
                Y[vertice] -= 0.01
            if event.key == K_LEFT:
                X[vertice] -= 0.01 
            if event.key == K_RIGHT:
                X[vertice] += 0.01
                
            if event.key == K_0:
                loadTexture()
                pygame.time.wait(250)
            #if event
            #if event.key == K_UP:
                
            

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()