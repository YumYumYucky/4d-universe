# dirived from https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/

import pygame
import time
import threading
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *





global x_p, y_p, z_p, w_p, theta, l, x, y, z, w, direction, r, theta, psi, omega

x_p=[1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,0]
y_p=[-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,0]
z_p=[-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,0]
w_p=[1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,2]
direction=[0,1,0,0]
x=0
y=0
z=0
w=0



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

  def steriographic():
 
   global verticies1, edges1




   #Have to replace all of these

   x0=((x_p[0])/(l-w_p[0]))+x
   x1=((x_p[1])/(l-w_p[1]))+x
   x2=((x_p[2])/(l-w_p[2]))+x
   x3=((x_p[3])/(l-w_p[3]))+x
   x4=((x_p[4])/(l-w_p[4]))+x
   x5=((x_p[5])/(l-w_p[5]))+x
   x6=((x_p[6])/(l-w_p[6]))+x
   x7=((x_p[7])/(l-w_p[7]))+x
   x8=((x_p[8])/(l-w_p[8]))+x
   x9=((x_p[9])/(l-w_p[9]))+x
   x10=((x_p[10])/(l-w_p[10]))+x
   x11=((x_p[11])/(l-w_p[11]))+x
   x12=((x_p[12])/(l-w_p[12]))+x
   x13=((x_p[13])/(l-w_p[13]))+x
   x14=((x_p[14])/(l-w_p[14]))+x
   x15=((x_p[15])/(l-w_p[15]))+x
   x16=((x_p[16])/(l-w_p[16]))+x


   y0=((y_p[0])/(l-w_p[0]))+y
   y1=((y_p[1])/(l-w_p[1]))+y
   y2=((y_p[2])/(l-w_p[2]))+y
   y3=((y_p[3])/(l-w_p[3]))+y
   y4=((y_p[4])/(l-w_p[4]))+y
   y5=((y_p[5])/(l-w_p[5]))+y
   y6=((y_p[6])/(l-w_p[6]))+y
   y7=((y_p[7])/(l-w_p[7]))+y
   y8=((y_p[8])/(l-w_p[8]))+y
   y9=((y_p[9])/(l-w_p[9]))+y
   y10=((y_p[10])/(l-w_p[10]))+y
   y11=((y_p[11])/(l-w_p[11]))+y
   y12=((y_p[12])/(l-w_p[12]))+y
   y13=((y_p[13])/(l-w_p[13]))+y
   y14=((y_p[14])/(l-w_p[14]))+y
   y15=((y_p[15])/(l-w_p[15]))+y
   y16=((y_p[16])/(l-w_p[16]))+y


   z0=((z_p[0])/(l-w_p[0]))+z
   z1=((z_p[1])/(l-w_p[1]))+z
   z2=((z_p[2])/(l-w_p[2]))+z
   z3=((z_p[3])/(l-w_p[3]))+z
   z4=((z_p[4])/(l-w_p[4]))+z
   z5=((z_p[5])/(l-w_p[5]))+z
   z6=((z_p[6])/(l-w_p[6]))+z
   z7=((z_p[7])/(l-w_p[7]))+z
   z8=((z_p[8])/(l-w_p[8]))+z
   z9=((z_p[9])/(l-w_p[9]))+z
   z10=((z_p[10])/(l-w_p[10]))+z
   z11=((z_p[11])/(l-w_p[11]))+z
   z12=((z_p[12])/(l-w_p[12]))+z
   z13=((z_p[13])/(l-w_p[13]))+z
   z14=((z_p[14])/(l-w_p[14]))+z
   z15=((z_p[15])/(l-w_p[15]))+z
   z16=((z_p[16])/(l-w_p[16]))+z




   


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
    print(f'{direction}')


  def c_p(d):
   global r, theta, psi, omega

   r=math.sqrt(d[0]**2+d[1]**2+d[2]**2+d[3]**2)
   theta=math.acos(d[3]/r)+(math.pi)/2
   psi=math.acos(d[2]/(math.sqrt(d[0]**2+d[1]**2+d[2]**2)))+(math.pi)/2
   omega=math.atan(d[0]/d[1])

   print(f'magnatude= {r}')
   print(f'theta= {theta}')
   print(f'psi= {psi}')
   print(f'omega= {omega}')



  def press():
   global x, y, z, w
   rotate='rotate'
   counter_rotate='counter_rotate'

  
   key=pygame.key.get_pressed()
   if key[pygame.K_j]:
    plane=[0,1]
    rotate_plane(x_p,y_p,plane,rotate)


   if key[pygame.K_l]:
    plane=[0,1]
    rotate_plane(y_p,x_p,plane,counter_rotate)


   if key[pygame.K_i]:
    plane=[0,2]
    rotate_plane(x_p,z_p,plane,rotate)


   if key[pygame.K_k]:
    plane=[0,2]
    rotate_plane(z_p,x_p,plane,counter_rotate)



   if key[pygame.K_t]:
    plane=[0,3]
    rotate_plane(x_p,w_p,plane,rotate)


   if key[pygame.K_u]:
    plane=[0,3]
    rotate_plane(w_p,x_p,plane,counter_rotate)


   if key[pygame.K_y]:
    plane=[1,2]
    rotate_plane(y_p,z_p,plane,rotate)


   if key[pygame.K_h]:
    plane=[1,2]
    rotate_plane(z_p,y_p,plane,counter_rotate)



   if key[pygame.K_f]:
    plane=[1,3]
    rotate_plane(y_p,w_p,plane,rotate)


   if key[pygame.K_v]:
    plane=[1,3]
    rotate_plane(w_p,y_p,plane,counter_rotate)


   if key[pygame.K_c]:
    plane=[2,3]
    rotate_plane(z_p,w_p,plane,rotate)

   if key[pygame.K_b]:
    plane=[2,3]
    rotate_plane(w_p,z_p,plane,counter_rotate)



   #movement
   if key[pygame.K_d]:
    x=x+1

   if key[pygame.K_a]:
    x=x-1

   if key[pygame.K_w]:
    y=y+1

   if key[pygame.K_s]:
    y=y-1

   if key[pygame.K_UP]:
    z=z+1

   if key[pygame.K_DOWN]:
    z=z-1

   if key[pygame.K_RIGHT]:
    w=w+1

   if key[pygame.K_LEFT]:
    w=w-1 







def rotate_plane(first_axis,second_axis,plane, rotation):
 global x_p, y_p, z_p, w_p, direction

 location=[]
 s_location=[]



 for a in range(len(first_axis)):
   f0=(first_axis[a]*math.cos(theta))-(second_axis[a]*math.sin(theta))
   s0=(first_axis[a]*math.sin(theta))+(second_axis[a]*math.cos(theta))

   s_location.append(s0)
   location.append(f0)


 if first_axis == x_p:
  x_p=location

 if first_axis == y_p:
  y_p=location

 if first_axis == z_p:
  z_p=location

 if first_axis == w_p:
  w_p=location


 if second_axis == x_p:
  x_p=s_location

 if second_axis == y_p:
  y_p=s_location

 if second_axis == z_p:
  z_p=s_location

 if second_axis == w_p:
  w_p=s_location











def rotate_direction(plane, rotation):
 global direction

 if rotation=='rotate':
  #print(f'plane[0]={plane[0]} and plane[1]={plane[1]}')
  direction[plane[0]]=(direction[plane[0]]*math.cos(theta))-(direction[plane[1]]*math.sin(theta))
  direction[plane[1]]=(direction[plane[0]]*math.sin(theta))+(direction[plane[1]]*math.cos(theta))

 if rotation=='counter_rotate':
  direction[plane[0]]=(direction[plane[0]]*math.cos(theta))+(direction[plane[1]]*math.sin(theta))
  direction[plane[1]]=-(direction[plane[0]]*math.sin(theta))+(direction[plane[1]]*math.cos(theta))









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

    glClearColor(0.2, 0.3, 0.3, 1.0);
  
    display = (800,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)


    gluPerspective(40, (display[0]/display[1]), 0.1, 25.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    

        t1=threading.Thread(target=move.press())
        t2=threading.Thread(target=move.steriographic())
        t4=threading.Thread(target=move.positions())
        t5=threading.Thread(target=move.c_p(direction))


        t1.start()

        #steriograhic projection
        t2.start()

        #orthographic projection
        #t3.start()

        t5.start()


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()




