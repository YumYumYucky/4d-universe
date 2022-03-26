# dirived from https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/

import math
import threading
import time
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

global x_p, y_p, z_p, w_p, theta_old, l, x, y, z, w, pointing, r, theta, psi, omega

x_p = [1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 0]
y_p = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0]
z_p = [-1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 0]
w_p = [1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 2]
pointing = [0, 1, 0, 0]
x = 1
y = 1
z = 1
w = 1

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

        x0w = ((x_p[0]) / (l - w_p[0])) + x
        x1w = ((x_p[1]) / (l - w_p[1])) + x
        x2w = ((x_p[2]) / (l - w_p[2])) + x
        x3w = ((x_p[3]) / (l - w_p[3])) + x
        x4w = ((x_p[4]) / (l - w_p[4])) + x
        x5w = ((x_p[5]) / (l - w_p[5])) + x
        x6w = ((x_p[6]) / (l - w_p[6])) + x
        x7w = ((x_p[7]) / (l - w_p[7])) + x
        x8w = ((x_p[8]) / (l - w_p[8])) + x
        x9w = ((x_p[9]) / (l - w_p[9])) + x
        x10w = ((x_p[10]) / (l - w_p[10])) + x
        x11w = ((x_p[11]) / (l - w_p[11])) + x
        x12w = ((x_p[12]) / (l - w_p[12])) + x
        x13w = ((x_p[13]) / (l - w_p[13])) + x
        x14w = ((x_p[14]) / (l - w_p[14])) + x
        x15w = ((x_p[15]) / (l - w_p[15])) + x
        x16w = ((x_p[16]) / (l - w_p[16])) + x

        y0w = ((y_p[0]) / (l - w_p[0])) + y
        y1w = ((y_p[1]) / (l - w_p[1])) + y
        y2w = ((y_p[2]) / (l - w_p[2])) + y
        y3w = ((y_p[3]) / (l - w_p[3])) + y
        y4w = ((y_p[4]) / (l - w_p[4])) + y
        y5w = ((y_p[5]) / (l - w_p[5])) + y
        y6w = ((y_p[6]) / (l - w_p[6])) + y
        y7w = ((y_p[7]) / (l - w_p[7])) + y
        y8w = ((y_p[8]) / (l - w_p[8])) + y
        y9w = ((y_p[9]) / (l - w_p[9])) + y
        y10w = ((y_p[10]) / (l - w_p[10])) + y
        y11w = ((y_p[11]) / (l - w_p[11])) + y
        y12w = ((y_p[12]) / (l - w_p[12])) + y
        y13w = ((y_p[13]) / (l - w_p[13])) + y
        y14w = ((y_p[14]) / (l - w_p[14])) + y
        y15w = ((y_p[15]) / (l - w_p[15])) + y
        y16w = ((y_p[16]) / (l - w_p[16])) + y

        z0w = ((z_p[0]) / (l - w_p[0])) + z
        z1w = ((z_p[1]) / (l - w_p[1])) + z
        z2w = ((z_p[2]) / (l - w_p[2])) + z
        z3w = ((z_p[3]) / (l - w_p[3])) + z
        z4w = ((z_p[4]) / (l - w_p[4])) + z
        z5w = ((z_p[5]) / (l - w_p[5])) + z
        z6w = ((z_p[6]) / (l - w_p[6])) + z
        z7w = ((z_p[7]) / (l - w_p[7])) + z
        z8w = ((z_p[8]) / (l - w_p[8])) + z
        z9w = ((z_p[9]) / (l - w_p[9])) + z
        z10w = ((z_p[10]) / (l - w_p[10])) + z
        z11w = ((z_p[11]) / (l - w_p[11])) + z
        z12w = ((z_p[12]) / (l - w_p[12])) + z
        z13w = ((z_p[13]) / (l - w_p[13])) + z
        z14w = ((z_p[14]) / (l - w_p[14])) + z
        z15w = ((z_p[15]) / (l - w_p[15])) + z
        z16w = ((z_p[16]) / (l - w_p[16])) + z

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

        w0x = ((w_p[0]) / (l - x_p[0])) + w + 2
        w1x = ((w_p[1]) / (l - x_p[1])) + w + 2
        w2x = ((w_p[2]) / (l - x_p[2])) + w + 2
        w3x = ((w_p[3]) / (l - x_p[3])) + w + 2
        w4x = ((w_p[4]) / (l - x_p[4])) + w + 2
        w5x = ((w_p[5]) / (l - x_p[5])) + w + 2
        w6x = ((w_p[6]) / (l - x_p[6])) + w + 2
        w7x = ((w_p[7]) / (l - x_p[7])) + w + 2
        w8x = ((w_p[8]) / (l - x_p[8])) + w + 2
        w9x = ((w_p[9]) / (l - x_p[9])) + w + 2
        w10x = ((w_p[10]) / (l - x_p[10])) + w + 2
        w11x = ((w_p[11]) / (l - x_p[11])) + w + 2
        w12x = ((w_p[12]) / (l - x_p[12])) + w + 2
        w13x = ((w_p[13]) / (l - x_p[13])) + w + 2
        w14x = ((w_p[14]) / (l - x_p[14])) + w + 2
        w15x = ((w_p[15]) / (l - x_p[15])) + w + 2
        w16x = ((w_p[16]) / (l - x_p[16])) + w + 2

        y0x = ((y_p[0]) / (l - x_p[0])) + y
        y1x = ((y_p[1]) / (l - x_p[1])) + y
        y2x = ((y_p[2]) / (l - x_p[2])) + y
        y3x = ((y_p[3]) / (l - x_p[3])) + y
        y4x = ((y_p[4]) / (l - x_p[4])) + y
        y5x = ((y_p[5]) / (l - x_p[5])) + y
        y6x = ((y_p[6]) / (l - x_p[6])) + y
        y7x = ((y_p[7]) / (l - x_p[7])) + y
        y8x = ((y_p[8]) / (l - x_p[8])) + y
        y9x = ((y_p[9]) / (l - x_p[9])) + y
        y10x = ((y_p[10]) / (l - x_p[10])) + y
        y11x = ((y_p[11]) / (l - x_p[11])) + y
        y12x = ((y_p[12]) / (l - x_p[12])) + y
        y13x = ((y_p[13]) / (l - x_p[13])) + y
        y14x = ((y_p[14]) / (l - x_p[14])) + y
        y15x = ((y_p[15]) / (l - x_p[15])) + y
        y16x = ((y_p[16]) / (l - x_p[16])) + y

        z0x = ((z_p[0]) / (l - x_p[0])) + z
        z1x = ((z_p[1]) / (l - x_p[1])) + z
        z2x = ((z_p[2]) / (l - x_p[2])) + z
        z3x = ((z_p[3]) / (l - x_p[3])) + z
        z4x = ((z_p[4]) / (l - x_p[4])) + z
        z5x = ((z_p[5]) / (l - x_p[5])) + z
        z6x = ((z_p[6]) / (l - x_p[6])) + z
        z7x = ((z_p[7]) / (l - x_p[7])) + z
        z8x = ((z_p[8]) / (l - x_p[8])) + z
        z9x = ((z_p[9]) / (l - x_p[9])) + z
        z10x = ((z_p[10]) / (l - x_p[10])) + z
        z11x = ((z_p[11]) / (l - x_p[11])) + z
        z12x = ((z_p[12]) / (l - x_p[12])) + z
        z13x = ((z_p[13]) / (l - x_p[13])) + z
        z14x = ((z_p[14]) / (l - x_p[14])) + z
        z15x = ((z_p[15]) / (l - x_p[15])) + z
        z16x = ((z_p[16]) / (l - x_p[16])) + z

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

        w0y = ((w_p[0]) / (l - y_p[0])) + w
        w1y = ((w_p[1]) / (l - y_p[1])) + w
        w2y = ((w_p[2]) / (l - y_p[2])) + w
        w3y = ((w_p[3]) / (l - y_p[3])) + w
        w4y = ((w_p[4]) / (l - y_p[4])) + w
        w5y = ((w_p[5]) / (l - y_p[5])) + w
        w6y = ((w_p[6]) / (l - y_p[6])) + w
        w7y = ((w_p[7]) / (l - y_p[7])) + w
        w8y = ((w_p[8]) / (l - y_p[8])) + w
        w9y = ((w_p[9]) / (l - y_p[9])) + w
        w10y = ((w_p[10]) / (l - y_p[10])) + w
        w11y = ((w_p[11]) / (l - y_p[11])) + w
        w12y = ((w_p[12]) / (l - y_p[12])) + w
        w13y = ((w_p[13]) / (l - y_p[13])) + w
        w14y = ((w_p[14]) / (l - y_p[14])) + w
        w15y = ((w_p[15]) / (l - y_p[15])) + w
        w16y = ((w_p[16]) / (l - y_p[16])) + w

        x0y = ((x_p[0]) / (l - y_p[0])) + x
        x1y = ((x_p[1]) / (l - y_p[1])) + x
        x2y = ((x_p[2]) / (l - y_p[2])) + x
        x3y = ((x_p[3]) / (l - y_p[3])) + x
        x4y = ((x_p[4]) / (l - y_p[4])) + x
        x5y = ((x_p[5]) / (l - y_p[5])) + x
        x6y = ((x_p[6]) / (l - y_p[6])) + x
        x7y = ((x_p[7]) / (l - y_p[7])) + x
        x8y = ((x_p[8]) / (l - y_p[8])) + x
        x9y = ((x_p[9]) / (l - y_p[9])) + x
        x10y = ((x_p[10]) / (l - y_p[10])) + x
        x11y = ((x_p[11]) / (l - y_p[11])) + x
        x12y = ((x_p[12]) / (l - y_p[12])) + x
        x13y = ((x_p[13]) / (l - y_p[13])) + x
        x14y = ((x_p[14]) / (l - y_p[14])) + x
        x15y = ((x_p[15]) / (l - y_p[15])) + x
        x16y = ((x_p[16]) / (l - y_p[16])) + x

        z0y = ((z_p[0]) / (l - y_p[0])) + z
        z1y = ((z_p[1]) / (l - y_p[1])) + z
        z2y = ((z_p[2]) / (l - y_p[2])) + z
        z3y = ((z_p[3]) / (l - y_p[3])) + z
        z4y = ((z_p[4]) / (l - y_p[4])) + z
        z5y = ((z_p[5]) / (l - y_p[5])) + z
        z6y = ((z_p[6]) / (l - y_p[6])) + z
        z7y = ((z_p[7]) / (l - y_p[7])) + z
        z8y = ((z_p[8]) / (l - y_p[8])) + z
        z9y = ((z_p[9]) / (l - y_p[9])) + z
        z10y = ((z_p[10]) / (l - y_p[10])) + z
        z11y = ((z_p[11]) / (l - y_p[11])) + z
        z12y = ((z_p[12]) / (l - y_p[12])) + z
        z13y = ((z_p[13]) / (l - y_p[13])) + z
        z14y = ((z_p[14]) / (l - y_p[14])) + z
        z15y = ((z_p[15]) / (l - y_p[15])) + z
        z16y = ((z_p[16]) / (l - y_p[16])) + z

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

        w0z = ((w_p[0]) / (l - z_p[0])) + w
        w1z = ((w_p[1]) / (l - z_p[1])) + w
        w2z = ((w_p[2]) / (l - z_p[2])) + w
        w3z = ((w_p[3]) / (l - z_p[3])) + w
        w4z = ((w_p[4]) / (l - z_p[4])) + w
        w5z = ((w_p[5]) / (l - z_p[5])) + w
        w6z = ((w_p[6]) / (l - z_p[6])) + w
        w7z = ((w_p[7]) / (l - z_p[7])) + w
        w8z = ((w_p[8]) / (l - z_p[8])) + w
        w9z = ((w_p[9]) / (l - z_p[9])) + w
        w10z = ((w_p[10]) / (l - z_p[10])) + w
        w11z = ((w_p[11]) / (l - z_p[11])) + w
        w12z = ((w_p[12]) / (l - z_p[12])) + w
        w13z = ((w_p[13]) / (l - z_p[13])) + w
        w14z = ((w_p[14]) / (l - z_p[14])) + w
        w15z = ((w_p[15]) / (l - z_p[15])) + w
        w16z = ((w_p[16]) / (l - z_p[16])) + w

        x0z = ((x_p[0]) / (l - z_p[0])) + x
        x1z = ((x_p[1]) / (l - z_p[1])) + x
        x2z = ((x_p[2]) / (l - z_p[2])) + x
        x3z = ((x_p[3]) / (l - z_p[3])) + x
        x4z = ((x_p[4]) / (l - z_p[4])) + x
        x5z = ((x_p[5]) / (l - z_p[5])) + x
        x6z = ((x_p[6]) / (l - z_p[6])) + x
        x7z = ((x_p[7]) / (l - z_p[7])) + x
        x8z = ((x_p[8]) / (l - z_p[8])) + x
        x9z = ((x_p[9]) / (l - z_p[9])) + x
        x10z = ((x_p[10]) / (l - z_p[10])) + x
        x11z = ((x_p[11]) / (l - z_p[11])) + x
        x12z = ((x_p[12]) / (l - z_p[12])) + x
        x13z = ((x_p[13]) / (l - z_p[13])) + x
        x14z = ((x_p[14]) / (l - z_p[14])) + x
        x15z = ((x_p[15]) / (l - z_p[15])) + x
        x16z = ((x_p[16]) / (l - z_p[16])) + x

        y0z = ((y_p[0]) / (l - z_p[0])) + y
        y1z = ((y_p[1]) / (l - z_p[1])) + y
        y2z = ((y_p[2]) / (l - z_p[2])) + y
        y3z = ((y_p[3]) / (l - z_p[3])) + y
        y4z = ((y_p[4]) / (l - z_p[4])) + y
        y5z = ((y_p[5]) / (l - z_p[5])) + y
        y6z = ((y_p[6]) / (l - z_p[6])) + y
        y7z = ((y_p[7]) / (l - z_p[7])) + y
        y8z = ((y_p[8]) / (l - z_p[8])) + y
        y9z = ((y_p[9]) / (l - z_p[9])) + y
        y10z = ((y_p[10]) / (l - z_p[10])) + y
        y11z = ((y_p[11]) / (l - z_p[11])) + y
        y12z = ((y_p[12]) / (l - z_p[12])) + y
        y13z = ((y_p[13]) / (l - z_p[13])) + y
        y14z = ((y_p[14]) / (l - z_p[14])) + y
        y15z = ((y_p[15]) / (l - z_p[15])) + y
        y16z = ((y_p[16]) / (l - z_p[16])) + y

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

    def positions():
        x0 = ((x_p[0]) / (l - w_p[0]))
        print(f'\northographic cords of x0={x_p[0]}')
        print(f'steriographic cords of x0={x0}')
        print(f'orthographic cords of x16={x_p[16]}')
        print(f'{pointing}')

    # def gravity():
    #    global x, y, z, w

    #    g_r = math.sqrt(x ** 2 + y ** 2 + z ** 2 + w ** 2)
    #    g_force = 1 / r ** 3
    #    g_theta = math.acos(w / r)
    #    g_psi = math.acos(z / math.sqrt(x ** 2 + y ** 2 + z ** 2))
    #    print(y)
    #    g_omega = math.atan(x / y)

    #    x = x + g_force * math.sin(theta + math.pi) * math.sin(psi) * math.sin(omega)

    #    y = y + g_force * math.sin(theta + math.pi) * math.sin(psi) * math.cos(omega)

    #    z = z + g_force * math.sin(theta + math.pi) * math.cos(psi)

    #    w = w + g_force * math.cos(theta + math.pi)

    def c_p(d):
        global r, theta, psi, omega

        r = math.sqrt(d[0] ** 2 + d[1] ** 2 + d[2] ** 2 + d[3] ** 2)
        theta = math.acos(d[3] / r)
        psi = math.acos(d[2] / (math.sqrt(d[0] ** 2 + d[1] ** 2 + d[2] ** 2)))
        omega = math.atan(d[0] / d[1])

        print(f'magnatude= {r}')
        print(f'theta= {theta}')
        print(f'psi= {psi}')
        print(f'omega= {omega}')

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

            x = x + ((.1) * math.sin(theta) * math.sin(psi) * math.sin(omega))
            y = y + ((.1) * math.sin(theta) * math.sin(psi) * math.cos(omega))
            z = z + ((.1) * math.sin(theta) * math.cos(psi))
            w = w + ((.1) * math.cos(theta))

        # DOWN
        if key[pygame.K_a]:
            x = x + ((.1) * math.sin(theta + math.pi) * math.sin(psi) * math.sin(omega))
            y = y + ((.1) * math.sin(theta + math.pi) * math.sin(psi) * math.cos(omega))
            z = z + ((.1) * math.sin(theta + math.pi) * math.cos(psi))
            w = w + ((.1) * math.cos(theta + math.pi))

        # W-
        if key[pygame.K_w]:
            x = x + ((.1) * math.sin(theta + (math.pi) / 2) * math.sin(psi) * math.sin(omega))
            y = y + ((.1) * math.sin(theta + (math.pi) / 2) * math.sin(psi) * math.cos(omega))
            z = z + ((.1) * math.sin(theta + (math.pi) / 2) * math.cos(psi))
            w = w + ((.1) * math.cos(theta + (math.pi) / 2))

        # W+
        if key[pygame.K_s]:
            x = x + ((.1) * math.sin(theta - (math.pi) / 2) * math.sin(psi) * math.sin(omega))
            y = y + ((.1) * math.sin(theta - (math.pi) / 2) * math.sin(psi) * math.cos(omega))
            z = z + ((.1) * math.sin(theta - (math.pi) / 2) * math.cos(psi))
            w = w + ((.1) * math.cos(theta - (math.pi) / 2))

        # BACK
        if key[pygame.K_UP]:
            x = x + ((.1) * math.sin(theta) * math.sin(psi + (math.pi) / 2) * math.sin(omega))
            y = y + ((.1) * math.sin(theta) * math.sin(psi + (math.pi) / 2) * math.cos(omega))
            z = z + ((.1) * math.sin(theta) * math.cos(psi + (math.pi) / 2))
            w = w + ((.1) * math.cos(theta))

        # FORWARD
        if key[pygame.K_DOWN]:
            x = x + ((.1) * math.sin(theta) * math.sin(psi - (math.pi) / 2) * math.sin(omega))
            y = y + ((.1) * math.sin(theta) * math.sin(psi - (math.pi) / 2) * math.cos(omega))
            z = z + ((.1) * math.sin(theta) * math.cos(psi - (math.pi) / 2))
            w = w + ((.1) * math.cos(theta))

        # RIGHT
        if key[pygame.K_RIGHT]:
            x = x + ((.1) * math.sin(theta) * math.sin(psi) * math.sin(omega + (math.pi) / 2))
            y = y + ((.1) * math.sin(theta) * math.sin(psi) * math.cos(omega + (math.pi) / 2))
            z = z + ((.1) * math.sin(theta) * math.cos(psi))
            w = w + ((.1) * math.cos(theta))

        # LEFT
        if key[pygame.K_LEFT]:
            x = x + ((.1) * math.sin(theta) * math.sin(psi) * math.sin(omega - (math.pi) / 2))
            y = y + ((.1) * math.sin(theta) * math.sin(psi) * math.cos(omega - (math.pi) / 2))
            z = z + ((.1) * math.sin(theta) * math.cos(psi))
            w = w + ((.1) * math.cos(theta))


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

    print(f'{w_p[1]}')

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


# def Cubex():
#    glBegin(GL_LINES)
##    for edge in edgesx:
#        for vertex in edge:
#            glVertex3fv(verticiesx[vertex])
#    glEnd()
# TUPLE INDEX OUT OF RANGE


def main():
    global pointing
    pygame.init()

    glClearColor(0.2, 0.3, 0.3, 1.0);

    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(40, (display[0] / display[1]), 0.1, 25.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        t1 = threading.Thread(target=move.press())
        # t2 = threading.Thread(target=move.stereographic())
        t4 = threading.Thread(target=move.positions())
        t5 = threading.Thread(target=move.c_p(pointing))
        # t6 = threading.Thread(target=move.gravity())

        t7 = threading.Thread(target=move.steriographic_w())
        t8 = threading.Thread(target=move.steriographic_x())
        t9 = threading.Thread(target=move.steriographic_y())
        t10 = threading.Thread(target=move.steriographic_z())

        t1.start()

        # steriograhic projection
        # t2.start()

        t7.start()
        t8.start()
        t9.start()
        t10.start()

        # orthographic projection
        # t3.start()

        t5.start()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        # Cubex()
        pygame.display.flip()
        pygame.time.wait(10)


main()
