import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random
from math import *  # trigonometry
import numpy as np
import sys
import time
import pyaudio


FORMAT = pyaudio.paInt16 # We use 16bit format per sample
CHANNELS = 1
RATE = 44100
CHUNK = 1024 # 1024bytes of data red from a buffer
RECORD_SECONDS = 0.1
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True)

X = [-1.0, -1.0, -1.0, 0.0, 0.0, 1.0, 1.0, 0.0]
Y = [-1.0, 0.0, 1.0, 1.0, 0.0, 0.0, -1.0, -1.0]


def face_one(i):
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(X[0], Y[0], 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(X[1], Y[1], 0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(X[4], Y[4], 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(X[7], Y[7], 0.0)
    glEnd()
    load_texture_three(i)


def face_two(i):
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(X[1], Y[1], 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(X[2], Y[2], 0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(X[3], Y[3], 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(X[4], Y[4], 0.0)
    glEnd()
    load_texture_one(i)


def face_three(i):
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(X[7], Y[7], 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(X[4], Y[4], 0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(X[5], Y[5], 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(X[6], Y[6], 0.0)
    glEnd()
    load_texture_two(i)


images_array1 = ['1.png', '2.png','3.png','4.png','5.png','6.png', 
                '7.png','8.png','9.png','10.png','11.png', '12.png','13.png',
                '14.png','15.png','16.png', '17.png','18.png','19.png','20.png','21.png', 
                '22.png']
size1 = len(images_array1)
#print(size)
images_array2 = ['output-0.png','output-1.png','output-2.png','output-3.png','output-4.png','output-5.png','output-6.png','output-7.png',
                'output-8.png','output-9.png','output-10.png','output-11.png','output-12.png','output-13.png','output-14.png','output-15.png',
                'output-16.png','output-17.png','output-18.png','output-19.png','output-20.png','output-21.png','output-22.png','output-23.png',
                'output-24.png','output-25.png','output-26.png','output-27.png','output-28.png','output-29.png','output-30.png','output-31.png',
                'output-32.png','output-33.png','output-34.png']

size2 = len(images_array2)

def load_texture_one(i):

    textureSurface = pygame.image.load(images_array1[i%size1])
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

def load_texture_two(i):

    textureSurface = pygame.image.load(images_array1[(i+2)%size1])
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

def load_texture_three(i):

    textureSurface = pygame.image.load(images_array2[(i)%size2])
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
    display = (1366, 768)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | OPENGLBLIT )
    i = 0
   
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)
    vertice = 0
    #face_one(i)
    #face_two(i)
    #face_three()
    
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
                Y[vertice] += 0.07
            if event.key == K_DOWN:
                Y[vertice] -= 0.07
            if event.key == K_LEFT:
                X[vertice] -= 0.07
            if event.key == K_RIGHT:
                X[vertice] += 0.07

            if event.key == K_9:
                pygame.quit()
                quit()
                break

            if event.key == K_0:
                while True:
                    audio_data = np.fromstring(stream.read(CHUNK), np.int16)
                    if max(audio_data) > 3000:
                        i+=1
                        #print(i)
                        


                        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                        face_one(i)
                        face_two(i)
                        face_three(i)
                        pygame.display.flip()




                #pygame.time.wait(250)
            # if event
            # if event.key == K_UP:
        
       
            #print(max(audio_data))
            
            
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        face_one(i)
        face_two(i)
        face_three(i)
        pygame.display.flip()
        pygame.time.wait(40)

    stream.stop_stream()
    stream.close()

    audio.terminate()

main()