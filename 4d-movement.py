# derived from https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/

import math
import threading
import time
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

global x_p, y_p, z_p, w_p, theta_old, l, velocity, position, pointing, r, theta, psi, omega

x_p = [1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 0]
y_p = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0]
z_p = [-1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 0]
w_p = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 2]
pointing = [0, 1, 0, 0]
velocity = [.55, .2, 0, 0]
position = [2, 3, 2, 2]

# rotation increments
theta_old = 1 / 100

# projection distance
l = 2.1


#
#
# HAVE A LIST OF ALL THE POINTS then rotate it with a function and then have those locations without one of the axis and then create a cube out of that
# Only use 3 of the axis to describe it.
#
#


class move:

    def steriographic_w():

        global verticies_w, edges_w

        x0w = ((x_p[0]) / (l - w_p[0])) + position[0]
        x1w = ((x_p[1]) / (l - w_p[1])) + position[0]
        x2w = ((x_p[2]) / (l - w_p[2])) + position[0]
        x3w = ((x_p[3]) / (l - w_p[3])) + position[0]
        x4w = ((x_p[4]) / (l - w_p[4])) + position[0]
        x5w = ((x_p[5]) / (l - w_p[5])) + position[0]
        x6w = ((x_p[6]) / (l - w_p[6])) + position[0]
        x7w = ((x_p[7]) / (l - w_p[7])) + position[0]
        x8w = ((x_p[8]) / (l - w_p[8])) + position[0]
        x9w = ((x_p[9]) / (l - w_p[9])) + position[0]
        x10w = ((x_p[10]) / (l - w_p[10])) + position[0]
        x11w = ((x_p[11]) / (l - w_p[11])) + position[0]
        x12w = ((x_p[12]) / (l - w_p[12])) + position[0]
        x13w = ((x_p[13]) / (l - w_p[13])) + position[0]
        x14w = ((x_p[14]) / (l - w_p[14])) + position[0]
        x15w = ((x_p[15]) / (l - w_p[15])) + position[0]
        x16w = ((x_p[16]) / (l - w_p[16])) + position[0]

        y0w = ((y_p[0]) / (l - w_p[0])) + position[1]
        y1w = ((y_p[1]) / (l - w_p[1])) + position[1]
        y2w = ((y_p[2]) / (l - w_p[2])) + position[1]
        y3w = ((y_p[3]) / (l - w_p[3])) + position[1]
        y4w = ((y_p[4]) / (l - w_p[4])) + position[1]
        y5w = ((y_p[5]) / (l - w_p[5])) + position[1]
        y6w = ((y_p[6]) / (l - w_p[6])) + position[1]
        y7w = ((y_p[7]) / (l - w_p[7])) + position[1]
        y8w = ((y_p[8]) / (l - w_p[8])) + position[1]
        y9w = ((y_p[9]) / (l - w_p[9])) + position[1]
        y10w = ((y_p[10]) / (l - w_p[10])) + position[1]
        y11w = ((y_p[11]) / (l - w_p[11])) + position[1]
        y12w = ((y_p[12]) / (l - w_p[12])) + position[1]
        y13w = ((y_p[13]) / (l - w_p[13])) + position[1]
        y14w = ((y_p[14]) / (l - w_p[14])) + position[1]
        y15w = ((y_p[15]) / (l - w_p[15])) + position[1]
        y16w = ((y_p[16]) / (l - w_p[16])) + position[1]

        z0w = ((z_p[0]) / (l - w_p[0])) + position[2]
        z1w = ((z_p[1]) / (l - w_p[1])) + position[2]
        z2w = ((z_p[2]) / (l - w_p[2])) + position[2]
        z3w = ((z_p[3]) / (l - w_p[3])) + position[2]
        z4w = ((z_p[4]) / (l - w_p[4])) + position[2]
        z5w = ((z_p[5]) / (l - w_p[5])) + position[2]
        z6w = ((z_p[6]) / (l - w_p[6])) + position[2]
        z7w = ((z_p[7]) / (l - w_p[7])) + position[2]
        z8w = ((z_p[8]) / (l - w_p[8])) + position[2]
        z9w = ((z_p[9]) / (l - w_p[9])) + position[2]
        z10w = ((z_p[10]) / (l - w_p[10])) + position[2]
        z11w = ((z_p[11]) / (l - w_p[11])) + position[2]
        z12w = ((z_p[12]) / (l - w_p[12])) + position[2]
        z13w = ((z_p[13]) / (l - w_p[13])) + position[2]
        z14w = ((z_p[14]) / (l - w_p[14])) + position[2]
        z15w = ((z_p[15]) / (l - w_p[15])) + position[2]
        z16w = ((z_p[16]) / (l - w_p[16])) + position[2]

        verticies_w = (

            (x0w, y0w, z0w),
            (x1w, y1w, z1w),
            (x2w, y2w, z2w),
            (x3w, y3w, z3w),
            (x4w, y4w, z4w),
            (x5w, y5w, z5w),
            (x6w, y6w, z6w),
            (x7w, y7w, z7w),
            (x8w, y8w, z8w),
            (x9w, y9w, z9w),
            (x10w, y10w, z10w),
            (x11w, y11w, z11w),
            (x12w, y12w, z12w),
            (x13w, y13w, z13w),
            (x14w, y14w, z14w),
            (x15w, y15w, z15w),
            (x16w, y16w, z16w)
        )

        edges_w = (
            (0, 1),
            (0, 2),
            (0, 4),
            (3, 1),
            (3, 2),
            (3, 7),
            (6, 2),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7),
            (8, 9),
            (8, 10),
            (8, 12),
            (11, 9),
            (11, 10),
            (11, 15),
            (14, 10),
            (14, 12),
            (14, 15),
            (13, 9),
            (13, 12),
            (13, 15),
            (0, 8),
            (1, 9),
            (2, 10),
            (3, 11),
            (4, 12),
            (5, 13),
            (6, 14),
            (7, 15),

            (0, 16),
            (1, 16),
            (2, 16),
            (3, 16),
            (4, 16),
            (5, 16),
            (6, 16),
            (7, 16)

        )

    def steriographic_x():
        global verticies_x, edges_x

        w0x = ((w_p[0]) / (l - x_p[0])) + position[3]
        w1x = ((w_p[1]) / (l - x_p[1])) + position[3]
        w2x = ((w_p[2]) / (l - x_p[2])) + position[3]
        w3x = ((w_p[3]) / (l - x_p[3])) + position[3]
        w4x = ((w_p[4]) / (l - x_p[4])) + position[3]
        w5x = ((w_p[5]) / (l - x_p[5])) + position[3]
        w6x = ((w_p[6]) / (l - x_p[6])) + position[3]
        w7x = ((w_p[7]) / (l - x_p[7])) + position[3]
        w8x = ((w_p[8]) / (l - x_p[8])) + position[3]
        w9x = ((w_p[9]) / (l - x_p[9])) + position[3]
        w10x = ((w_p[10]) / (l - x_p[10])) + position[3]
        w11x = ((w_p[11]) / (l - x_p[11])) + position[3]
        w12x = ((w_p[12]) / (l - x_p[12])) + position[3]
        w13x = ((w_p[13]) / (l - x_p[13])) + position[3]
        w14x = ((w_p[14]) / (l - x_p[14])) + position[3]
        w15x = ((w_p[15]) / (l - x_p[15])) + position[3]
        w16x = ((w_p[16]) / (l - x_p[16])) + position[3]

        y0x = ((y_p[0]) / (l - x_p[0])) + position[1]
        y1x = ((y_p[1]) / (l - x_p[1])) + position[1]
        y2x = ((y_p[2]) / (l - x_p[2])) + position[1]
        y3x = ((y_p[3]) / (l - x_p[3])) + position[1]
        y4x = ((y_p[4]) / (l - x_p[4])) + position[1]
        y5x = ((y_p[5]) / (l - x_p[5])) + position[1]
        y6x = ((y_p[6]) / (l - x_p[6])) + position[1]
        y7x = ((y_p[7]) / (l - x_p[7])) + position[1]
        y8x = ((y_p[8]) / (l - x_p[8])) + position[1]
        y9x = ((y_p[9]) / (l - x_p[9])) + position[1]
        y10x = ((y_p[10]) / (l - x_p[10])) + position[1]
        y11x = ((y_p[11]) / (l - x_p[11])) + position[1]
        y12x = ((y_p[12]) / (l - x_p[12])) + position[1]
        y13x = ((y_p[13]) / (l - x_p[13])) + position[1]
        y14x = ((y_p[14]) / (l - x_p[14])) + position[1]
        y15x = ((y_p[15]) / (l - x_p[15])) + position[1]
        y16x = ((y_p[16]) / (l - x_p[16])) + position[1]

        z0x = ((z_p[0]) / (l - x_p[0])) + position[2]
        z1x = ((z_p[1]) / (l - x_p[1])) + position[2]
        z2x = ((z_p[2]) / (l - x_p[2])) + position[2]
        z3x = ((z_p[3]) / (l - x_p[3])) + position[2]
        z4x = ((z_p[4]) / (l - x_p[4])) + position[2]
        z5x = ((z_p[5]) / (l - x_p[5])) + position[2]
        z6x = ((z_p[6]) / (l - x_p[6])) + position[2]
        z7x = ((z_p[7]) / (l - x_p[7])) + position[2]
        z8x = ((z_p[8]) / (l - x_p[8])) + position[2]
        z9x = ((z_p[9]) / (l - x_p[9])) + position[2]
        z10x = ((z_p[10]) / (l - x_p[10])) + position[2]
        z11x = ((z_p[11]) / (l - x_p[11])) + position[2]
        z12x = ((z_p[12]) / (l - x_p[12])) + position[2]
        z13x = ((z_p[13]) / (l - x_p[13])) + position[2]
        z14x = ((z_p[14]) / (l - x_p[14])) + position[2]
        z15x = ((z_p[15]) / (l - x_p[15])) + position[2]
        z16x = ((z_p[16]) / (l - x_p[16])) + position[2]

        verticies_x = (

            (w0x, y0x, z0x),
            (w1x, y1x, z1x),
            (w2x, y2x, z2x),
            (w3x, y3x, z3x),
            (w4x, y4x, z4x),
            (w5x, y5x, z5x),
            (w6x, y6x, z6x),
            (w7x, y7x, z7x),
            (w8x, y8x, z8x),
            (w9x, y9x, z9x),
            (w10x, y10x, z10x),
            (w11x, y11x, z11x),
            (w12x, y12x, z12x),
            (w13x, y13x, z13x),
            (w14x, y14x, z14x),
            (w15x, y15x, z15x),
            (w16x, y16x, z16x)
        )

        edges_x = (
            (0, 1),
            (0, 2),
            (0, 4),
            (3, 1),
            (3, 2),
            (3, 7),
            (6, 2),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7),
            (8, 9),
            (8, 10),
            (8, 12),
            (11, 9),
            (11, 10),
            (11, 15),
            (14, 10),
            (14, 12),
            (14, 15),
            (13, 9),
            (13, 12),
            (13, 15),
            (0, 8),
            (1, 9),
            (2, 10),
            (3, 11),
            (4, 12),
            (5, 13),
            (6, 14),
            (7, 15),

            (0, 16),
            (1, 16),
            (2, 16),
            (3, 16),
            (4, 16),
            (5, 16),
            (6, 16),
            (7, 16)

        )

    def steriographic_y():
        global verticies_y, edges_y

        w0y = ((w_p[0]) / (l - y_p[0])) + position[3]
        w1y = ((w_p[1]) / (l - y_p[1])) + position[3]
        w2y = ((w_p[2]) / (l - y_p[2])) + position[3]
        w3y = ((w_p[3]) / (l - y_p[3])) + position[3]
        w4y = ((w_p[4]) / (l - y_p[4])) + position[3]
        w5y = ((w_p[5]) / (l - y_p[5])) + position[3]
        w6y = ((w_p[6]) / (l - y_p[6])) + position[3]
        w7y = ((w_p[7]) / (l - y_p[7])) + position[3]
        w8y = ((w_p[8]) / (l - y_p[8])) + position[3]
        w9y = ((w_p[9]) / (l - y_p[9])) + position[3]
        w10y = ((w_p[10]) / (l - y_p[10])) + position[3]
        w11y = ((w_p[11]) / (l - y_p[11])) + position[3]
        w12y = ((w_p[12]) / (l - y_p[12])) + position[3]
        w13y = ((w_p[13]) / (l - y_p[13])) + position[3]
        w14y = ((w_p[14]) / (l - y_p[14])) + position[3]
        w15y = ((w_p[15]) / (l - y_p[15])) + position[3]
        w16y = ((w_p[16]) / (l - y_p[16])) + position[3]

        x0y = ((x_p[0]) / (l - y_p[0])) + position[0]
        x1y = ((x_p[1]) / (l - y_p[1])) + position[0]
        x2y = ((x_p[2]) / (l - y_p[2])) + position[0]
        x3y = ((x_p[3]) / (l - y_p[3])) + position[0]
        x4y = ((x_p[4]) / (l - y_p[4])) + position[0]
        x5y = ((x_p[5]) / (l - y_p[5])) + position[0]
        x6y = ((x_p[6]) / (l - y_p[6])) + position[0]
        x7y = ((x_p[7]) / (l - y_p[7])) + position[0]
        x8y = ((x_p[8]) / (l - y_p[8])) + position[0]
        x9y = ((x_p[9]) / (l - y_p[9])) + position[0]
        x10y = ((x_p[10]) / (l - y_p[10])) + position[0]
        x11y = ((x_p[11]) / (l - y_p[11])) + position[0]
        x12y = ((x_p[12]) / (l - y_p[12])) + position[0]
        x13y = ((x_p[13]) / (l - y_p[13])) + position[0]
        x14y = ((x_p[14]) / (l - y_p[14])) + position[0]
        x15y = ((x_p[15]) / (l - y_p[15])) + position[0]
        x16y = ((x_p[16]) / (l - y_p[16])) + position[0]

        z0y = ((z_p[0]) / (l - y_p[0])) + position[2]
        z1y = ((z_p[1]) / (l - y_p[1])) + position[2]
        z2y = ((z_p[2]) / (l - y_p[2])) + position[2]
        z3y = ((z_p[3]) / (l - y_p[3])) + position[2]
        z4y = ((z_p[4]) / (l - y_p[4])) + position[2]
        z5y = ((z_p[5]) / (l - y_p[5])) + position[2]
        z6y = ((z_p[6]) / (l - y_p[6])) + position[2]
        z7y = ((z_p[7]) / (l - y_p[7])) + position[2]
        z8y = ((z_p[8]) / (l - y_p[8])) + position[2]
        z9y = ((z_p[9]) / (l - y_p[9])) + position[2]
        z10y = ((z_p[10]) / (l - y_p[10])) + position[2]
        z11y = ((z_p[11]) / (l - y_p[11])) + position[2]
        z12y = ((z_p[12]) / (l - y_p[12])) + position[2]
        z13y = ((z_p[13]) / (l - y_p[13])) + position[2]
        z14y = ((z_p[14]) / (l - y_p[14])) + position[2]
        z15y = ((z_p[15]) / (l - y_p[15])) + position[2]
        z16y = ((z_p[16]) / (l - y_p[16])) + position[2]

        verticies_y = (

            (w0y, x0y, z0y),
            (w1y, x1y, z1y),
            (w2y, x2y, z2y),
            (w3y, x3y, z3y),
            (w4y, x4y, z4y),
            (w5y, x5y, z5y),
            (w6y, x6y, z6y),
            (w7y, x7y, z7y),
            (w8y, x8y, z8y),
            (w9y, x9y, z9y),
            (w10y, x10y, z10y),
            (w11y, x11y, z11y),
            (w12y, x12y, z12y),
            (w13y, x13y, z13y),
            (w14y, x14y, z14y),
            (w15y, x15y, z15y),
            (w16y, x16y, z16y)
        )

        edges_y = (
            (0, 1),
            (0, 2),
            (0, 4),
            (3, 1),
            (3, 2),
            (3, 7),
            (6, 2),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7),
            (8, 9),
            (8, 10),
            (8, 12),
            (11, 9),
            (11, 10),
            (11, 15),
            (14, 10),
            (14, 12),
            (14, 15),
            (13, 9),
            (13, 12),
            (13, 15),
            (0, 8),
            (1, 9),
            (2, 10),
            (3, 11),
            (4, 12),
            (5, 13),
            (6, 14),
            (7, 15),

            (0, 16),
            (1, 16),
            (2, 16),
            (3, 16),
            (4, 16),
            (5, 16),
            (6, 16),
            (7, 16)

        )

    def steriographic_z():
        global verticies_z, edges_z

        w0z = ((w_p[0]) / (l - z_p[0])) + position[3]
        w1z = ((w_p[1]) / (l - z_p[1])) + position[3]
        w2z = ((w_p[2]) / (l - z_p[2])) + position[3]
        w3z = ((w_p[3]) / (l - z_p[3])) + position[3]
        w4z = ((w_p[4]) / (l - z_p[4])) + position[3]
        w5z = ((w_p[5]) / (l - z_p[5])) + position[3]
        w6z = ((w_p[6]) / (l - z_p[6])) + position[3]
        w7z = ((w_p[7]) / (l - z_p[7])) + position[3]
        w8z = ((w_p[8]) / (l - z_p[8])) + position[3]
        w9z = ((w_p[9]) / (l - z_p[9])) + position[3]
        w10z = ((w_p[10]) / (l - z_p[10])) + position[3]
        w11z = ((w_p[11]) / (l - z_p[11])) + position[3]
        w12z = ((w_p[12]) / (l - z_p[12])) + position[3]
        w13z = ((w_p[13]) / (l - z_p[13])) + position[3]
        w14z = ((w_p[14]) / (l - z_p[14])) + position[3]
        w15z = ((w_p[15]) / (l - z_p[15])) + position[3]
        w16z = ((w_p[16]) / (l - z_p[16])) + position[3]

        x0z = ((x_p[0]) / (l - z_p[0])) + position[0]
        x1z = ((x_p[1]) / (l - z_p[1])) + position[0]
        x2z = ((x_p[2]) / (l - z_p[2])) + position[0]
        x3z = ((x_p[3]) / (l - z_p[3])) + position[0]
        x4z = ((x_p[4]) / (l - z_p[4])) + position[0]
        x5z = ((x_p[5]) / (l - z_p[5])) + position[0]
        x6z = ((x_p[6]) / (l - z_p[6])) + position[0]
        x7z = ((x_p[7]) / (l - z_p[7])) + position[0]
        x8z = ((x_p[8]) / (l - z_p[8])) + position[0]
        x9z = ((x_p[9]) / (l - z_p[9])) + position[0]
        x10z = ((x_p[10]) / (l - z_p[10])) + position[0]
        x11z = ((x_p[11]) / (l - z_p[11])) + position[0]
        x12z = ((x_p[12]) / (l - z_p[12])) + position[0]
        x13z = ((x_p[13]) / (l - z_p[13])) + position[0]
        x14z = ((x_p[14]) / (l - z_p[14])) + position[0]
        x15z = ((x_p[15]) / (l - z_p[15])) + position[0]
        x16z = ((x_p[16]) / (l - z_p[16])) + position[0]

        y0z = ((y_p[0]) / (l - z_p[0])) + position[1]
        y1z = ((y_p[1]) / (l - z_p[1])) + position[1]
        y2z = ((y_p[2]) / (l - z_p[2])) + position[1]
        y3z = ((y_p[3]) / (l - z_p[3])) + position[1]
        y4z = ((y_p[4]) / (l - z_p[4])) + position[1]
        y5z = ((y_p[5]) / (l - z_p[5])) + position[1]
        y6z = ((y_p[6]) / (l - z_p[6])) + position[1]
        y7z = ((y_p[7]) / (l - z_p[7])) + position[1]
        y8z = ((y_p[8]) / (l - z_p[8])) + position[1]
        y9z = ((y_p[9]) / (l - z_p[9])) + position[1]
        y10z = ((y_p[10]) / (l - z_p[10])) + position[1]
        y11z = ((y_p[11]) / (l - z_p[11])) + position[1]
        y12z = ((y_p[12]) / (l - z_p[12])) + position[1]
        y13z = ((y_p[13]) / (l - z_p[13])) + position[1]
        y14z = ((y_p[14]) / (l - z_p[14])) + position[1]
        y15z = ((y_p[15]) / (l - z_p[15])) + position[1]
        y16z = ((y_p[16]) / (l - z_p[16])) + position[1]

        verticies_z = (

            (w0z, x0z, y0z),
            (w1z, x1z, y1z),
            (w2z, x2z, y2z),
            (w3z, x3z, y3z),
            (w4z, x4z, y4z),
            (w5z, x5z, y5z),
            (w6z, x6z, y6z),
            (w7z, x7z, y7z),
            (w8z, x8z, y8z),
            (w9z, x9z, y9z),
            (w10z, x10z, y10z),
            (w11z, x11z, y11z),
            (w12z, x12z, y12z),
            (w13z, x13z, y13z),
            (w14z, x14z, y14z),
            (w15z, x15z, y15z),
            (w16z, x16z, y16z)
        )

        edges_z = (
            (0, 1),
            (0, 2),
            (0, 4),
            (3, 1),
            (3, 2),
            (3, 7),
            (6, 2),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7),
            (8, 9),
            (8, 10),
            (8, 12),
            (11, 9),
            (11, 10),
            (11, 15),
            (14, 10),
            (14, 12),
            (14, 15),
            (13, 9),
            (13, 12),
            (13, 15),
            (0, 8),
            (1, 9),
            (2, 10),
            (3, 11),
            (4, 12),
            (5, 13),
            (6, 14),
            (7, 15),

            (0, 16),
            (1, 16),
            (2, 16),
            (3, 16),
            (4, 16),
            (5, 16),
            (6, 16),
            (7, 16)

        )

    # def positions():
    #   x0 = ((x_p[0]) / (l - w_p[0]))
    #    print(f'\northographic cords of x0={x_p[0]}')
    #    print(f'steriographic cords of x0={x0}')
    #    print(f'orthographic cords of x16={x_p[16]}')

    def gravity():
        global x, y, z, w

        g_r = math.sqrt(position[0] ** 2 + position[1] ** 2 + position[2] ** 2 + position[3] ** 2)
        g_theta = math.atan(
            -position[3] / math.sqrt(position[0] ** 2 + position[1] ** 2 + position[2] ** 2)) + math.pi / 2
        g_psi = math.atan(-position[2] / math.sqrt(position[0] ** 2 + position[1] ** 2)) + math.pi / 2
        g_omega = math.atan(position[0] / position[1])

        if g_r > .99:
            g_force = 1 / g_r ** 3
        elif g_r < -.99:
            g_force = 1 / math.abs(g_r ** 3)
        else:
            g_force = 0

        g_x = math.sin(g_theta) * math.sin(g_psi) * math.sin(g_omega)
        g_y = math.sin(g_theta) * math.sin(g_psi) * math.cos(g_omega)
        g_z = math.sin(g_theta) * math.cos(g_psi)
        g_w = math.cos(g_theta)

        print(f'g_x={g_x}')
        print(f'g_y={g_y}')
        print(f'g_z={g_z}')
        print(f'g_w={g_w}')

        velocity[0] = velocity[0] - (g_force * position[0])

        velocity[1] = velocity[1] - (g_force * position[1])

        velocity[2] = velocity[2] - (g_force * position[2])

        velocity[3] = velocity[3] - (g_force * position[3])

        print(f'x_velocity={velocity[0]}')
        print(f'y_velocity={velocity[1]}')
        print(f'z_velocity={velocity[2]}')
        print(f'w_velocity={velocity[3]}')

    def velocity():
        position[0] = position[0] + velocity[0]
        position[1] = position[1] + velocity[1]
        position[2] = position[2] + velocity[2]
        position[3] = position[3] + velocity[3]

    def c_p(d):
        global r, theta, psi, omega

        r = math.sqrt(d[0] ** 2 + d[1] ** 2 + d[2] ** 2 + d[3] ** 2)
        theta = math.acos(d[3] / r)
        psi = math.acos(d[2] / (math.sqrt(d[0] ** 2 + d[1] ** 2 + d[2] ** 2)))
        omega = math.atan(d[0] / d[1])

    def press():
        global x, y, z, w
        rotate = 'rotate'
        counter_rotate = 'counter_rotate'

        plane = [0, 1]

        key = pygame.key.get_pressed()
        if key[pygame.K_j]:
            plane = [0, 1]
            rotate_plane(x_p, y_p, plane)
            rotate_direction(plane, rotate)

        if key[pygame.K_l]:
            plane = [0, 1]
            rotate_plane(y_p, x_p, plane)
            rotate_direction(plane, counter_rotate)

        if key[pygame.K_i]:
            plane = [0, 2]
            rotate_plane(x_p, z_p, plane)
            rotate_direction(plane, rotate)

        if key[pygame.K_k]:
            plane = [0, 2]
            rotate_plane(z_p, x_p, plane)
            rotate_direction(plane, counter_rotate)

        if key[pygame.K_t]:
            plane = [0, 3]
            rotate_plane(x_p, w_p, plane)
            rotate_direction(plane, rotate)

        if key[pygame.K_u]:
            plane = [0, 3]
            rotate_plane(w_p, x_p, plane)
            rotate_direction(plane, counter_rotate)

        if key[pygame.K_y]:
            plane = [1, 2]
            rotate_plane(y_p, z_p, plane)
            rotate_direction(plane, rotate)

        if key[pygame.K_h]:
            plane = [1, 2]
            rotate_plane(z_p, y_p, plane)
            rotate_direction(plane, counter_rotate)

        if key[pygame.K_f]:
            plane = [1, 3]
            rotate_plane(y_p, w_p, plane)
            rotate_direction(plane, rotate)

        if key[pygame.K_v]:
            plane = [1, 3]
            rotate_plane(w_p, y_p, plane)
            rotate_direction(plane, counter_rotate)

        if key[pygame.K_c]:
            plane = [2, 3]
            rotate_plane(z_p, w_p, plane)
            rotate_direction(plane, rotate)

        if key[pygame.K_b]:
            plane = [2, 3]
            rotate_plane(w_p, z_p, plane)
            rotate_direction(plane, counter_rotate)

        # movement

        # UP
        if key[pygame.K_d]:
            # Might need to switch where + and - pi/2 goes because might not be the right direction

            velocity[0] = velocity[0] + (.01 * math.sin(theta) * math.sin(psi) * math.sin(omega))
            velocity[1] = velocity[1] + (.01 * math.sin(theta) * math.sin(psi) * math.cos(omega))
            velocity[2] = velocity[2] + (.01 * math.sin(theta) * math.cos(psi))
            velocity[3] = velocity[3] + (.01 * math.cos(theta))

        # DOWN
        if key[pygame.K_a]:
            velocity[0] = velocity[0] + (.01 * math.sin(theta + math.pi) * math.sin(psi) * math.sin(omega))
            velocity[1] = velocity[1] + (.01 * math.sin(theta + math.pi) * math.sin(psi) * math.cos(omega))
            velocity[2] = velocity[2] + (.01 * math.sin(theta + math.pi) * math.cos(psi))
            velocity[3] = velocity[3] + (.01 * math.cos(theta + math.pi))

        # W-
        if key[pygame.K_w]:
            velocity[0] = velocity[0] + (.01 * math.sin(theta + math.pi / 2) * math.sin(psi) * math.sin(omega))
            velocity[1] = velocity[1] + (.01 * math.sin(theta + math.pi / 2) * math.sin(psi) * math.cos(omega))
            velocity[2] = velocity[2] + (.01 * math.sin(theta + math.pi / 2) * math.cos(psi))
            velocity[3] = velocity[3] + (.01 * math.cos(theta + math.pi / 2))

        # W+
        if key[pygame.K_s]:
            velocity[0] = velocity[0] + (.01 * math.sin(theta - math.pi / 2) * math.sin(psi) * math.sin(omega))
            velocity[1] = velocity[1] + (.01 * math.sin(theta - math.pi / 2) * math.sin(psi) * math.cos(omega))
            velocity[2] = velocity[2] + (.01 * math.sin(theta - math.pi / 2) * math.cos(psi))
            velocity[3] = velocity[3] + (.01 * math.cos(theta - math.pi / 2))

        # BACK
        if key[pygame.K_UP]:
            velocity[0] = velocity[0] + (.01 * math.sin(theta) * math.sin(psi + math.pi / 2) * math.sin(omega))
            velocity[1] = velocity[1] + (.01 * math.sin(theta) * math.sin(psi + math.pi / 2) * math.cos(omega))
            velocity[2] = velocity[2] + (.01 * math.sin(theta) * math.cos(psi + math.pi / 2))
            velocity[3] = velocity[3] + (.01 * math.cos(theta))

        # FORWARD
        if key[pygame.K_DOWN]:
            velocity[0] = velocity[0] + (.01 * math.sin(theta) * math.sin(psi - math.pi / 2) * math.sin(omega))
            velocity[1] = velocity[1] + (.01 * math.sin(theta) * math.sin(psi - math.pi / 2) * math.cos(omega))
            velocity[2] = velocity[2] + (.01 * math.sin(theta) * math.cos(psi - math.pi / 2))
            velocity[3] = velocity[3] + (.01 * math.cos(theta))

        # RIGHT
        if key[pygame.K_RIGHT]:
            velocity[0] = velocity[0] + (.01 * math.sin(theta) * math.sin(psi) * math.sin(omega + math.pi / 2))
            velocity[1] = velocity[1] + (.01 * math.sin(theta) * math.sin(psi) * math.cos(omega + math.pi / 2))
            velocity[2] = velocity[2] + (.01 * math.sin(theta) * math.cos(psi))
            velocity[3] = velocity[3] + (.01 * math.cos(theta))

        # LEFT
        if key[pygame.K_LEFT]:
            velocity[0] = velocity[0] + (.01 * math.sin(theta) * math.sin(psi) * math.sin(omega - math.pi / 2))
            velocity[1] = velocity[1] + (.01 * math.sin(theta) * math.sin(psi) * math.cos(omega - math.pi / 2))
            velocity[2] = velocity[2] + (.01 * math.sin(theta) * math.cos(psi))
            velocity[3] = velocity[3] + (.01 * math.cos(theta))


def rotate_plane(first_axis, second_axis, plane):
    global x_p, y_p, z_p, w_p, theta_old

    location = []
    s_location = []

    for a in range(len(first_axis)):
        f0 = (first_axis[a] * math.cos(theta_old)) - (second_axis[a] * math.sin(theta_old))
        s0 = (first_axis[a] * math.sin(theta_old)) + (second_axis[a] * math.cos(theta_old))

        s_location.append(s0)
        location.append(f0)

    if first_axis == x_p:
        x_p = location

    elif first_axis == y_p:
        y_p = location

    elif first_axis == z_p:
        z_p = location

    elif first_axis == w_p:
        w_p = location

    else:
        print('HELP')

    if second_axis == x_p:
        x_p = s_location

    elif second_axis == y_p:
        y_p = s_location

    elif second_axis == z_p:
        z_p = s_location

    elif second_axis == w_p:
        w_p = s_location

    else:
        print('HELP')


def rotate_direction(plane, rotation):
    global pointing

    if rotation == 'rotate':
        # print(f'plane[0]={plane[0]} and plane[1]={plane[1]}')
        direction0 = (pointing[plane[0]] * math.cos(theta_old)) - (pointing[plane[1]] * math.sin(theta_old))
        direction1 = (pointing[plane[0]] * math.sin(theta_old)) + (pointing[plane[1]] * math.cos(theta_old))

        pointing[plane[0]] = direction0
        pointing[plane[1]] = direction1

    if rotation == 'counter_rotate':
        direction0 = (pointing[plane[0]] * math.cos(theta_old)) + (pointing[plane[1]] * math.sin(theta_old))
        direction1 = -(pointing[plane[0]] * math.sin(theta_old)) + (pointing[plane[1]] * math.cos(theta_old))

        pointing[plane[0]] = direction0
        pointing[plane[1]] = direction1


def positions1():
    x0 = ((x_p[0]) / (l - w_p[0]))
    print(f'\northographic cords of x0={x_p[0]}')
    print(f'steriographic cords of x0={x0}')

    y0 = ((y_p[0]) / (l - w_p[0]))
    print(f'orthographic cords of y0={y_p[0]}')
    print(f'steriographic cords of y0={y0}')


def Cube():
    glBegin(GL_LINES)
    for edge_w in edges_w:
        for vertex in edge_w:
            glVertex3fv(verticies_w[vertex])
    for edge_x in edges_x:
        for vertex_x in edge_x:
            glVertex3fv(verticies_x[vertex_x])

    for edge_y in edges_y:
        for vertex_y in edge_y:
            glVertex3fv(verticies_y[vertex_y])
    for edge_z in edges_z:
        for vertex_z in edge_z:
            glVertex3fv(verticies_z[vertex_z])
    glEnd()


def sphere():
    quad = gluNewQuadric()
    glColor4f(1, 1, .7, 1)
    gluSphere(quad, 1.5, 20, 20)


def Cubex():
    for edge_x in edges_x:
        for vertex_x in edge_x:
            glVertex3fv(verticies_x[vertex_x])
    glEnd()


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


def main():
    global pointing
    pygame.init()

    glClearColor(.2, 0.3, 0.3, 1.0);

    display = (1200, 800)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(120, (display[0] / display[1]), 0.1, 55.0)

    glTranslatef(0.0, 0.0, -15)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        t1 = threading.Thread(target=move.press())
        # t2 = threading.Thread(target=move.stereographic())
        # t4 = threading.Thread(target=move.positions())
        t5 = threading.Thread(target=move.c_p(pointing))
        t6 = threading.Thread(target=move.gravity())

        t7 = threading.Thread(target=move.steriographic_w())
        t8 = threading.Thread(target=move.steriographic_x())
        t9 = threading.Thread(target=move.steriographic_y())
        t10 = threading.Thread(target=move.steriographic_z())
        t11 = threading.Thread(target=move.velocity())

        t1.start()

        # steriograhic projection
        # t2.start()

        t7.start()
        t8.start()
        t9.start()
        t10.start()

        t11.start()
        time.sleep(.01)
        t11.join()

        # orthographic projection
        # t3.start()

        t5.start()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        sphere()
        # Cubex()
        pygame.display.flip()


if __name__ == '__main__':
    main()
