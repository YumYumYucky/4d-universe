# dirived from https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/

import pygame
import time
import threading
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *





global x_p, y_p, z_p, w_p, theta, l, x, y, z, w, direction

x_p=[1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,0]
y_p=[-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,0]
z_p=[-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,0]
w_p=[1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,2]
direction=[1,1,1,1]
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



  def press():
   global x, y, z, w
 

   #just have one function that takes the input of the two axis of rotation and then plugs those into the function and have the same axis but fliped for counter rotate
  
   key=pygame.key.get_pressed()
   if key[pygame.K_j]:
    plane=[0,1]
    rotate_first_plane(x_p,y_p,plane)
    rotate_second_plane(x_p,y_p,plane)


   if key[pygame.K_l]:
    plane=[0,1]
    rotate_first_plane(y_p,x_p,plane)
    rotate_second_plane(y_p,x_p,plane)


   if key[pygame.K_i]:
    plane=[0,2]
    rotate_first_plane(x_p,z_p,plane)
    rotate_second_plane(x_p,z_p,plane)


   if key[pygame.K_k]:
    plane=[0,2]
    rotate_first_plane(z_p,x_p,plane)
    rotate_second_plane(z_p,x_p,plane)



   if key[pygame.K_t]:
    plane=[0,3]
    rotate_first_plane(x_p,w_p,plane)
    rotate_second_plane(x_p,w_p,plane)


   if key[pygame.K_u]:
    plane=[0,3]
    rotate_first_plane(w_p,x_p,plane)
    rotate_second_plane(w_p,x_p,plane)



   if key[pygame.K_y]:
    plane=[1,2]
    rotate_first_plane(y_p,z_p,plane)
    rotate_second_plane(y_p,z_p,plane)


   if key[pygame.K_h]:
    plane=[1,2]
    rotate_first_plane(z_p,y_p,plane)
    rotate_second_plane(z_p,y_p,plane)



   if key[pygame.K_f]:
    plane=[1,3]
    rotate_first_plane(y_p,w_p,plane)
    rotate_second_plane(y_p,w_p,plane)

   if key[pygame.K_v]:
    plane=[1,3]
    rotate_first_plane(w_p,y_p,plane)
    rotate_second_plane(w_p,y_p,plane)


   if key[pygame.K_c]:
    plane=[2,3]
    rotate_first_plane(z_p,w_p,plane)
    rotate_second_plane(z_p,w_p,plane)

   if key[pygame.K_b]:
    plane=[2,3]
    rotate_first_plane(w_p,z_p,plane)
    rotate_second_plane(w_p,z_p,plane)



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







#rotates any plane based on the input
def rotate_first_plane(first_axis,second_axis,plane):
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



 #up dating points and computing direction

 #print(f'plane[0]={plane[0]} and plane[1]={plane[1]}')
 direction[plane[0]]=(direction[plane[0]]*math.cos(theta))-(direction[plane[1]]*math.sin(theta))
 direction[plane[1]]=(direction[plane[0]]*math.sin(theta))+(direction[plane[1]]*math.cos(theta))

 if first_axis == x_p:
  x_p=location

 if first_axis == y_p:
  y_p=location

 if first_axis == z_p:
  z_p=location

 if first_axis == w_p:
  w_p=location


# if second_axis == x_p:
#  x_p=location

# if second_axis == y_p:
#  y_p=location

# if second_axis == z_p:
#  z_p=location

# if second_axis == w_p:
#  w_p=location






def rotate_second_plane(first_axis,second_axis,plane):
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

    gluPerspective(40, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    

        t1=threading.Thread(target=move.press())
        t2=threading.Thread(target=move.steriographic())
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

