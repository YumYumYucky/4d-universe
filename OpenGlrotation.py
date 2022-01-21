# dirived from https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/

import pygame
import time
import threading
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *



x=1
y=1
z=1
w=1


global x_p, y_p, z_p, w_p, theta, l

x_p=[1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,0]
y_p=[-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,0]
z_p=[-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,0]
w_p=[1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,2]

#rotation increments
theta=(math.pi)/128

#projection distance
l=2.1


#
#
#HAVE A LIST OF ALL THE POINTS then rotate it with a function and then have those locations without one of the axis and then create a cube out of that
#Only use 3 of the axis to describe it.
#
#


class move:

  def steriographic(x_axis,y_axis,z_axis,w_axis):
 
   global verticies1, edges1
   x=x_axis
   y=y_axis
   z=z_axis
   w=w_axis



   #Have to replace all of these

   x0=((x_p[0])/(l-w_p[0]))
   x1=((x_p[1])/(l-w_p[1]))
   x2=((x_p[2])/(l-w_p[2]))
   x3=((x_p[3])/(l-w_p[3]))
   x4=((x_p[4])/(l-w_p[4]))
   x5=((x_p[5])/(l-w_p[5]))
   x6=((x_p[6])/(l-w_p[6]))
   x7=((x_p[7])/(l-w_p[7]))
   x8=((x_p[8])/(l-w_p[8]))
   x9=((x_p[9])/(l-w_p[9]))
   x10=((x_p[10])/(l-w_p[10]))
   x11=((x_p[11])/(l-w_p[11]))
   x12=((x_p[12])/(l-w_p[12]))
   x13=((x_p[13])/(l-w_p[13]))
   x14=((x_p[14])/(l-w_p[14]))
   x15=((x_p[15])/(l-w_p[15]))
   x16=((x_p[16])/(l-w_p[16]))


   y0=((y_p[0])/(l-w_p[0]))
   y1=((y_p[1])/(l-w_p[1]))
   y2=((y_p[2])/(l-w_p[2]))
   y3=((y_p[3])/(l-w_p[3]))
   y4=((y_p[4])/(l-w_p[4]))
   y5=((y_p[5])/(l-w_p[5]))
   y6=((y_p[6])/(l-w_p[6]))
   y7=((y_p[7])/(l-w_p[7]))
   y8=((y_p[8])/(l-w_p[8]))
   y9=((y_p[9])/(l-w_p[9]))
   y10=((y_p[10])/(l-w_p[10]))
   y11=((y_p[11])/(l-w_p[11]))
   y12=((y_p[12])/(l-w_p[12]))
   y13=((y_p[13])/(l-w_p[13]))
   y14=((y_p[14])/(l-w_p[14]))
   y15=((y_p[15])/(l-w_p[15]))
   y16=((y_p[16])/(l-w_p[16]))


   z0=((z_p[0])/(l-w_p[0]))
   z1=((z_p[1])/(l-w_p[1]))
   z2=((z_p[2])/(l-w_p[2]))
   z3=((z_p[3])/(l-w_p[3]))
   z4=((z_p[4])/(l-w_p[4]))
   z5=((z_p[5])/(l-w_p[5]))
   z6=((z_p[6])/(l-w_p[6]))
   z7=((z_p[7])/(l-w_p[7]))
   z8=((z_p[8])/(l-w_p[8]))
   z9=((z_p[9])/(l-w_p[9]))
   z10=((z_p[10])/(l-w_p[10]))
   z11=((z_p[11])/(l-w_p[11]))
   z12=((z_p[12])/(l-w_p[12]))
   z13=((z_p[13])/(l-w_p[13]))
   z14=((z_p[14])/(l-w_p[14]))
   z15=((z_p[15])/(l-w_p[15]))
   z16=((z_p[16])/(l-w_p[16]))




   


   verticies1 = (


    (x0,y0,z0),
    (x1,y1,z1),
    (x2,y2,z2),
    (x3,y3,z3),
    (x4,y4,z4),
    (x5,y5,z5),
    (x6,y6,z6),
    (x7,y7,z7),
    (x8,y8,z8),
    (x9,y9,z9),
    (x10,y10,z10),
    (x11,y11,z11),
    (x12,y12,z12),
    (x13,y13,z13),
    (x14,y14,z14),
    (x15,y15,z15),
    (x16,y16,z16)
    )

   edges1 = (
    (0,1),
    (0,2),
    (0,4),
    (3,1),
    (3,2),
    (3,7),
    (6,2),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    (8,9),
    (8,10),
    (8,12),
    (11,9),
    (11,10),
    (11,15),
    (14,10),
    (14,12),
    (14,15),
    (13,9),
    (13,12),
    (13,15),
    (0,8),
    (1,9),
    (2,10),
    (3,11),
    (4,12),
    (5,13),
    (6,14),
    (7,15),
    (0,16),
    (1,16),
    (2,16),
    (3,16),
    (4,16),
    (5,16),
    (6,16),
    (7,16)


    )


  def positions():
    x0=((x_p[0])/(l-w_p[0]))
    print(f'\northographic cords of x0={x_p[0]}')
    print(f'steriographic cords of x0={x0}')
    print(f'orthographic cords of x16={x_p[16]}')



  def press(x,y,z,w):

   #just have one function that takes the input of the two axis of rotation and then plugs those into the function and have the same axis but fliped for counter rotate
  
   key=pygame.key.get_pressed()
   if key[pygame.K_j]:
    rotate_first_plane(x_p,y_p)
    rotate_second_plane(x_p,y_p)


   if key[pygame.K_l]:
    rotate_first_plane(y_p,x_p)
    rotate_second_plane(y_p,x_p)


   if key[pygame.K_i]:
    rotate_first_plane(x_p,z_p)
    rotate_second_plane(x_p,z_p)


   if key[pygame.K_k]:
    rotate_first_plane(z_p,x_p)
    rotate_second_plane(z_p,x_p)



   if key[pygame.K_d]:
    rotate_first_plane(x_p,w_p)
    rotate_second_plane(x_p,w_p)


   if key[pygame.K_a]:
    rotate_first_plane(w_p,x_p)
    rotate_second_plane(w_p,x_p)



   if key[pygame.K_w]:
    rotate_first_plane(y_p,z_p)
    rotate_second_plane(y_p,z_p)


   if key[pygame.K_s]:
    rotate_first_plane(z_p,y_p)
    rotate_second_plane(z_p,y_p)



   if key[pygame.K_UP]:
    rotate_first_plane(y_p,w_p)
    rotate_second_plane(y_p,w_p)

   if key[pygame.K_DOWN]:
    rotate_first_plane(w_p,y_p)
    rotate_second_plane(w_p,y_p)


   if key[pygame.K_RIGHT]:
    rotate_first_plane(z_p,w_p)
    rotate_second_plane(z_p,w_p)

   if key[pygame.K_LEFT]:
    rotate_first_plane(w_p,z_p)
    rotate_second_plane(w_p,z_p)






#rotates any plane based on the input
def rotate_first_plane(first_axis,second_axis):
 global x_p, y_p, z_p, w_p


 location=[]

 #point0
 f0=(first_axis[0]*math.cos(theta))-(second_axis[0]*math.sin(theta))

 location.append(f0)

 #point1
 f1=(first_axis[1]*math.cos(theta))-(second_axis[1]*math.sin(theta))

 location.append(f1)

 #point2
 f2=(first_axis[2]*math.cos(theta))-(second_axis[2]*math.sin(theta))

 location.append(f2)

 #point3
 f3=(first_axis[3]*math.cos(theta))-(second_axis[3]*math.sin(theta))

 location.append(f3)

 #point4
 f4=(first_axis[4]*math.cos(theta))-(second_axis[4]*math.sin(theta))

 location.append(f4)

 #point5
 f5=(first_axis[5]*math.cos(theta))-(second_axis[5]*math.sin(theta))

 location.append(f5)

 #point6
 f6=(first_axis[6]*math.cos(theta))-(second_axis[6]*math.sin(theta))

 location.append(f6)

 #point7
 f7=(first_axis[7]*math.cos(theta))-(second_axis[7]*math.sin(theta))

 location.append(f7)

 #point8
 f8=(first_axis[8]*math.cos(theta))-(second_axis[8]*math.sin(theta))

 location.append(f8)

 #point9
 f9=(first_axis[9]*math.cos(theta))-(second_axis[9]*math.sin(theta))

 location.append(f9)

 #point10
 f10=(first_axis[10]*math.cos(theta))-(second_axis[10]*math.sin(theta))

 location.append(f10)

 #point11
 f11=(first_axis[11]*math.cos(theta))-(second_axis[11]*math.sin(theta))

 location.append(f11)

 #point12
 f12=(first_axis[12]*math.cos(theta))-(second_axis[12]*math.sin(theta))

 location.append(f12)

 #point13
 f13=(first_axis[13]*math.cos(theta))-(second_axis[13]*math.sin(theta))

 location.append(f13)

 #point14
 f14=(first_axis[14]*math.cos(theta))-(second_axis[14]*math.sin(theta))

 location.append(f14)

 #point15
 f15=(first_axis[15]*math.cos(theta))-(second_axis[15]*math.sin(theta))

 location.append(f15)

 #point16
 f16=(first_axis[16]*math.cos(theta))-(second_axis[16]*math.sin(theta))

 location.append(f16)


 if first_axis == x_p:
  x_p=location

 if first_axis == y_p:
  y_p=location

 if first_axis == z_p:
  z_p=location

 if first_axis == w_p:
  w_p=location






def rotate_second_plane(first_axis,second_axis):
 global x_p, y_p, z_p, w_p


 location=[]

 #point0
 s0=(first_axis[0]*math.sin(theta))+(second_axis[0]*math.cos(theta))

 location.append(s0)

 #point1
 s1=(first_axis[1]*math.sin(theta))+(second_axis[1]*math.cos(theta))

 location.append(s1)

 #point2
 s2=(first_axis[2]*math.sin(theta))+(second_axis[2]*math.cos(theta))

 location.append(s2)

 #point3
 s3=(first_axis[3]*math.sin(theta))+(second_axis[3]*math.cos(theta))

 location.append(s3)

 #point4
 s4=(first_axis[4]*math.sin(theta))+(second_axis[4]*math.cos(theta))

 location.append(s4)

 #point5
 s5=(first_axis[5]*math.sin(theta))+(second_axis[5]*math.cos(theta))

 location.append(s5)

 #point6
 s6=(first_axis[6]*math.sin(theta))+(second_axis[6]*math.cos(theta))

 location.append(s6)

 #point7
 s7=(first_axis[7]*math.sin(theta))+(second_axis[7]*math.cos(theta))

 location.append(s7)

 #point8
 s8=(first_axis[8]*math.sin(theta))+(second_axis[8]*math.cos(theta))

 location.append(s8)

 #point9
 s9=(first_axis[9]*math.sin(theta))+(second_axis[9]*math.cos(theta))

 location.append(s9)

 #point10
 s10=(first_axis[10]*math.sin(theta))+(second_axis[10]*math.cos(theta))

 location.append(s10)

 #point11
 s11=(first_axis[11]*math.sin(theta))+(second_axis[11]*math.cos(theta))

 location.append(s11)

 #point12
 s12=(first_axis[12]*math.sin(theta))+(second_axis[12]*math.cos(theta))

 location.append(s12)

 #point13
 s13=(first_axis[13]*math.sin(theta))+(second_axis[13]*math.cos(theta))

 location.append(s13)

 #point14
 s14=(first_axis[14]*math.sin(theta))+(second_axis[14]*math.cos(theta))

 location.append(s14)

 #point15
 s15=(first_axis[15]*math.sin(theta))+(second_axis[15]*math.cos(theta))

 location.append(s15)

 #point16
 s16=(first_axis[16]*math.sin(theta))+(second_axis[16]*math.cos(theta))

 location.append(s16)

 if second_axis == x_p:
  x_p=location

 if second_axis == y_p:
  y_p=location

 if second_axis == z_p:
  z_p=location

 if second_axis == w_p:
  w_p=location




def positions1():
   x0=((x_p[0])/(l-w_p[0]))
   print(f'\northographic cords of x0={x_p[0]}')
   print(f'steriographic cords of x0={x0}')


   y0=((y_p[0])/(l-w_p[0]))
   print(f'orthographic cords of y0={y_p[0]}')
   print(f'steriographic cords of y0={y0}')








def Cube():
    glBegin(GL_LINES)
    for edge in edges1:
        for vertex in edge:
            glVertex3fv(verticies1[vertex])
    glEnd()




def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    

        t1=threading.Thread(target=move.press(x,y,z,w))
        t2=threading.Thread(target=move.steriographic(x,y,z,w))
        t4=threading.Thread(target=move.positions())



        t1.start()

        #steriograhic projection
        t2.start()


        #orthographic projection
        #t3.start()


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()

