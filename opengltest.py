# dirived from https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/

import pygame
import time
import threading
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *



global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16



x1=1
x2=1
x3=1
x4=1
x5=-1
x6=-1
x7=-1
x8=-1
x9=1
x10=1
x11=1
x12=1
x13=-1
x14=-1
x15=-1
x16=-1

y1=-1
y2=1
y3=-1
y4=1
y5=-1
y6=1
y7=-1
y8=1
y9=-1
y10=1
y11=-1
y12=1
y13=-1
y14=1
y15=-1
y16=1

z1=-1
z2=-1
z3=1
z4=1
z5=-1
z6=-1
z7=1
z8=1
z9=-1
z10=-1
z11=1
z12=1
z13=-1
z14=-1
z15=1
z16=1

w1=1
w2=1
w3=1
w4=1
w5=1
w6=1
w7=1
w8=1
w9=-1
w10=-1
w11=-1
w12=-1
w13=-1
w14=-1
w15=-1
w16=-1

x=1
y=1
z=1
w=1


global x_p, y_p, z_p, w_p, theta, light

x_p=[1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1]
y_p=[-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1]
z_p=[-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1]
w_p=[1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1]

#rotation increments
theta=(math.pi)/128

#projection distance
l=2


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
    (x15,y15,z15)
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
    (7,15)

    )

  def orthographic(x_axis,y_axis,z_axis,w_axis):
 
    global verticies2, edges2
    x=x_axis
    y=y_axis
    z=z_axis
    w=w_axis


    verticies2 = (
     (x_p[0],y_p[0],z_p[0]),
     (x_p[1],y_p[1],z_p[1]),
     (x_p[2],y_p[2],z_p[2]),
     (x_p[3],y_p[3],z_p[3]),
     (x_p[4],y_p[4],z_p[4]),
     (x_p[5],y_p[5],z_p[5]),
     (x_p[6],y_p[6],z_p[6]),
     (x_p[7],y_p[7],z_p[7]),
     (x_p[8],y_p[8],z_p[8]),
     (x_p[9],y_p[9],z_p[9]),
     (x_p[10],y_p[10],z_p[10]),
     (x_p[11],y_p[11],z_p[11]),
     (x_p[12],y_p[12],z_p[12]),
     (x_p[13],y_p[13],z_p[13]),
     (x_p[14],y_p[14],z_p[14]),
     (x_p[15],y_p[15],z_p[15])
     )

    edges2 = (
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
     (7,15) 

    
     )


  def positions():
    x0=(x_p[0])*(1/(l-w_p[0]))
    print(f'orthographic cords of x0={x_p[0]}')
    print(f'steriographic cords of x0={x0}')


  def press(x,y,z,w):

   #just have one function that takes the input of the two axis of rotation and then plugs those into the function and have the same axis but fliped for counter rotate
  
   key=pygame.key.get_pressed()
   if key[pygame.K_j]:
    rotate_xy(x,y,z,w)

   if key[pygame.K_l]:
    counter_rotate_xy(x,y,z,w)


   if key[pygame.K_i]:
    rotate_xz(x,y,z,w)

   if key[pygame.K_k]:
    counter_rotate_xz(x,y,z,w)


   if key[pygame.K_d]:
    rotate_xw(x,y,z,w)

   if key[pygame.K_a]:
    counter_rotate_xw(x,y,z,w)


   if key[pygame.K_w]:
    rotate_yz(x,y,z,w)

   if key[pygame.K_s]:
    counter_rotate_yz(x,y,z,w)


   if key[pygame.K_UP]:
    rotate_yw(x,y,z,w)

   if key[pygame.K_DOWN]:
    counter_rotate_yw(x,y,z,w)


   if key[pygame.K_RIGHT]:
    rotate_zw(x,y,z,w)

   if key[pygame.K_LEFT]:
    counter_rotate_zw(x,y,z,w)






#rotates any plane based on the input
def rotate_first_plane(first_axis,second_axis):

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







def rotate_second_plane(first_axis,second_axis):

# how to return


 location=[]

 #point0
 s0=(first_axis[0]*math.sin(theta))+(second_axis[0]*math.cos(theta))


 locaion.append(s0)

 #point1
 s1=(first_axis[1]*math.sin(theta))+(second_axis[1]*math.cos(theta))


 locaion.append(s1)

 #point2
 s2=(first_axis[2]*math.sin(theta))+(second_axis[2]*math.cos(theta))


 locaion.append(s2)

 #point3
 s3=(first_axis[3]*math.sin(theta))+(second_axis[3]*math.cos(theta))


 locaion.append(s3)

 #point4
 s4=(first_axis[4]*math.sin(theta))+(second_axis[4]*math.cos(theta))


 locaion.append(s4)

 #point5
 s5=(first_axis[5]*math.sin(theta))+(second_axis[5]*math.cos(theta))


 locaion.append(s5)

 #point6
 s6=(first_axis[6]*math.sin(theta))+(second_axis[6]*math.cos(theta))


 locaion.append(s6)

 #point7
 s7=(first_axis[7]*math.sin(theta))+(second_axis[7]*math.cos(theta))


 locaion.append(s7)

 #point8
 s8=(first_axis[8]*math.sin(theta))+(second_axis[8]*math.cos(theta))


 locaion.append(s8)

 #point9
 s9=(first_axis[9]*math.sin(theta))+(second_axis[9]*math.cos(theta))


 locaion.append(s9)

 #point10
 s10=(first_axis[10]*math.sin(theta))+(second_axis[10]*math.cos(theta))


 locaion.append(s10)

 #point11
 s11=(first_axis[11]*math.sin(theta))+(second_axis[11]*math.cos(theta))


 locaion.append(s11)

 #point12
 s12=(first_axis[12]*math.sin(theta))+(second_axis[12]*math.cos(theta))


 locaion.append(s12)

 #point13
 s13=(first_axis[13]*math.sin(theta))+(second_axis[13]*math.cos(theta))


 locaion.append(s13)

 #point14
 s14=(first_axis[14]*math.sin(theta))+(second_axis[14]*math.cos(theta))


 locaion.append(s14)

 #point15
 s15=(first_axis[15]*math.sin(theta))+(second_axis[15]*math.cos(theta))


 locaion.append(s15)














#rotate xy plane
def rotate_xy(x,y,z,w):

 #point0
 x=(x_p[0]*math.cos(theta))-(y_p[0]*math.sin(theta))
 y=(x_p[0]*math.sin(theta))+(y_p[0]*math.cos(theta))

 x_p[0]=x
 y_p[0]=y

 #point1
 x=(x_p[1]*math.cos(theta))-(y_p[1]*math.sin(theta))
 y=(x_p[1]*math.sin(theta))+(y_p[1]*math.cos(theta))

 x_p[1]=x
 y_p[1]=y

 #point2
 x=(x_p[2]*math.cos(theta))-(y_p[2]*math.sin(theta))
 y=(x_p[2]*math.sin(theta))+(y_p[2]*math.cos(theta))

 x_p[2]=x
 y_p[2]=y

 #point3
 x=(x_p[3]*math.cos(theta))-(y_p[3]*math.sin(theta))
 y=(x_p[3]*math.sin(theta))+(y_p[3]*math.cos(theta))

 x_p[3]=x
 y_p[3]=y

 #point4
 x=(x_p[4]*math.cos(theta))-(y_p[4]*math.sin(theta))
 y=(x_p[4]*math.sin(theta))+(y_p[4]*math.cos(theta))

 x_p[4]=x
 y_p[4]=y

 #point5
 x=(x_p[5]*math.cos(theta))-(y_p[5]*math.sin(theta))
 y=(x_p[5]*math.sin(theta))+(y_p[5]*math.cos(theta))

 x_p[5]=x
 y_p[5]=y

 #point6
 x=(x_p[6]*math.cos(theta))-(y_p[6]*math.sin(theta))
 y=(x_p[6]*math.sin(theta))+(y_p[6]*math.cos(theta))

 x_p[6]=x
 y_p[6]=y

 #point7
 x=(x_p[7]*math.cos(theta))-(y_p[7]*math.sin(theta))
 y=(x_p[7]*math.sin(theta))+(y_p[7]*math.cos(theta))

 x_p[7]=x
 y_p[7]=y

 #point8
 x=(x_p[8]*math.cos(theta))-(y_p[8]*math.sin(theta))
 y=(x_p[8]*math.sin(theta))+(y_p[8]*math.cos(theta))

 x_p[8]=x
 y_p[8]=y

 #point9
 x=(x_p[9]*math.cos(theta))-(y_p[9]*math.sin(theta))
 y=(x_p[9]*math.sin(theta))+(y_p[9]*math.cos(theta))

 x_p[9]=x
 y_p[9]=y

 #point10
 x=(x_p[10]*math.cos(theta))-(y_p[10]*math.sin(theta))
 y=(x_p[10]*math.sin(theta))+(y_p[10]*math.cos(theta))

 x_p[10]=x
 y_p[10]=y

 #point11
 x=(x_p[11]*math.cos(theta))-(y_p[11]*math.sin(theta))
 y=(x_p[11]*math.sin(theta))+(y_p[11]*math.cos(theta))

 x_p[11]=x
 y_p[11]=y

 #point12
 x=(x_p[12]*math.cos(theta))-(y_p[12]*math.sin(theta))
 y=(x_p[12]*math.sin(theta))+(y_p[12]*math.cos(theta))

 x_p[12]=x
 y_p[12]=y

 #point13
 x=(x_p[13]*math.cos(theta))-(y_p[13]*math.sin(theta))
 y=(x_p[13]*math.sin(theta))+(y_p[13]*math.cos(theta))

 x_p[13]=x
 y_p[13]=y

 #point14
 x=(x_p[14]*math.cos(theta))-(y_p[14]*math.sin(theta))
 y=(x_p[14]*math.sin(theta))+(y_p[14]*math.cos(theta))

 x_p[14]=x
 y_p[14]=y

 #point15
 x=(x_p[15]*math.cos(theta))-(y_p[15]*math.sin(theta))
 y=(x_p[15]*math.sin(theta))+(y_p[15]*math.cos(theta))

 x_p[15]=x
 y_p[15]=y





#counter rotate xy plane
def counter_rotate_xy(x,y,z,w):

 #point0
 x=(x_p[0]*math.cos(theta))+(y_p[0]*math.sin(theta))
 y=-(x_p[0]*math.sin(theta))+(y_p[0]*math.cos(theta))

 x_p[0]=x
 y_p[0]=y

 #point1
 x=(x_p[1]*math.cos(theta))+(y_p[1]*math.sin(theta))
 y=-(x_p[1]*math.sin(theta))+(y_p[1]*math.cos(theta))

 x_p[1]=x
 y_p[1]=y

 #point2
 x=(x_p[2]*math.cos(theta))+(y_p[2]*math.sin(theta))
 y=-(x_p[2]*math.sin(theta))+(y_p[2]*math.cos(theta))

 x_p[2]=x
 y_p[2]=y

 #point3
 x=(x_p[3]*math.cos(theta))+(y_p[3]*math.sin(theta))
 y=-(x_p[3]*math.sin(theta))+(y_p[3]*math.cos(theta))

 x_p[3]=x
 y_p[3]=y

 #point4
 x=(x_p[4]*math.cos(theta))+(y_p[4]*math.sin(theta))
 y=-(x_p[4]*math.sin(theta))+(y_p[4]*math.cos(theta))

 x_p[4]=x
 y_p[4]=y

 #point5
 x=(x_p[5]*math.cos(theta))+(y_p[5]*math.sin(theta))
 y=-(x_p[5]*math.sin(theta))+(y_p[5]*math.cos(theta))

 x_p[5]=x
 y_p[5]=y

 #point6
 x=(x_p[6]*math.cos(theta))+(y_p[6]*math.sin(theta))
 y=-(x_p[6]*math.sin(theta))+(y_p[6]*math.cos(theta))

 x_p[6]=x
 y_p[6]=y

 #point7
 x=(x_p[7]*math.cos(theta))+(y_p[7]*math.sin(theta))
 y=-(x_p[7]*math.sin(theta))+(y_p[7]*math.cos(theta))

 x_p[7]=x
 y_p[7]=y

 #point8
 x=(x_p[8]*math.cos(theta))+(y_p[8]*math.sin(theta))
 y=-(x_p[8]*math.sin(theta))+(y_p[8]*math.cos(theta))

 x_p[8]=x
 y_p[8]=y

 #point9
 x=(x_p[9]*math.cos(theta))+(y_p[9]*math.sin(theta))
 y=-(x_p[9]*math.sin(theta))+(y_p[9]*math.cos(theta))

 x_p[9]=x
 y_p[9]=y

 #point10
 x=(x_p[10]*math.cos(theta))+(y_p[10]*math.sin(theta))
 y=-(x_p[10]*math.sin(theta))+(y_p[10]*math.cos(theta))

 x_p[10]=x
 y_p[10]=y

 #point11
 x=(x_p[11]*math.cos(theta))+(y_p[11]*math.sin(theta))
 y=-(x_p[11]*math.sin(theta))+(y_p[11]*math.cos(theta))

 x_p[11]=x
 y_p[11]=y

 #point12
 x=(x_p[12]*math.cos(theta))+(y_p[12]*math.sin(theta))
 y=-(x_p[12]*math.sin(theta))+(y_p[12]*math.cos(theta))

 x_p[12]=x
 y_p[12]=y

 #point13
 x=(x_p[13]*math.cos(theta))+(y_p[13]*math.sin(theta))
 y=-(x_p[13]*math.sin(theta))+(y_p[13]*math.cos(theta))

 x_p[13]=x
 y_p[13]=y

 #point14
 x=(x_p[14]*math.cos(theta))+(y_p[14]*math.sin(theta))
 y=-(x_p[14]*math.sin(theta))+(y_p[14]*math.cos(theta))

 x_p[14]=x
 y_p[14]=y

 #point15
 x=(x_p[15]*math.cos(theta))+(y_p[15]*math.sin(theta))
 y=-(x_p[15]*math.sin(theta))+(y_p[15]*math.cos(theta))

 x_p[15]=x
 y_p[15]=y




#rotate xz plane
def rotate_xz(x,y,z,w):

 #point0
 x=(x_p[0]*math.cos(theta))-(z_p[0]*math.sin(theta))
 z=(x_p[0]*math.sin(theta))+(z_p[0]*math.cos(theta))

 x_p[0]=x
 z_p[0]=z

 #point1
 x=(x_p[1]*math.cos(theta))-(z_p[1]*math.sin(theta))
 z=(x_p[1]*math.sin(theta))+(z_p[1]*math.cos(theta))

 x_p[1]=x
 z_p[1]=z

 #point2
 x=(x_p[2]*math.cos(theta))-(z_p[2]*math.sin(theta))
 z=(x_p[2]*math.sin(theta))+(z_p[2]*math.cos(theta))

 x_p[2]=x
 z_p[2]=z

 #point3
 x=(x_p[3]*math.cos(theta))-(z_p[3]*math.sin(theta))
 z=(x_p[3]*math.sin(theta))+(z_p[3]*math.cos(theta))

 x_p[3]=x
 z_p[3]=z

 #point4
 x=(x_p[4]*math.cos(theta))-(z_p[4]*math.sin(theta))
 z=(x_p[4]*math.sin(theta))+(z_p[4]*math.cos(theta))

 x_p[4]=x
 z_p[4]=z

 #point5
 x=(x_p[5]*math.cos(theta))-(z_p[5]*math.sin(theta))
 z=(x_p[5]*math.sin(theta))+(z_p[5]*math.cos(theta))

 x_p[5]=x
 z_p[5]=z

 #point6
 x=(x_p[6]*math.cos(theta))-(z_p[6]*math.sin(theta))
 z=(x_p[6]*math.sin(theta))+(z_p[6]*math.cos(theta))

 x_p[6]=x
 z_p[6]=z

 #point7
 x=(x_p[7]*math.cos(theta))-(z_p[7]*math.sin(theta))
 z=(x_p[7]*math.sin(theta))+(z_p[7]*math.cos(theta))

 x_p[7]=x
 z_p[7]=z

 #point8
 x=(x_p[8]*math.cos(theta))-(z_p[8]*math.sin(theta))
 z=(x_p[8]*math.sin(theta))+(z_p[8]*math.cos(theta))

 x_p[8]=x
 z_p[8]=z

 #point9
 x=(x_p[9]*math.cos(theta))-(z_p[9]*math.sin(theta))
 z=(x_p[9]*math.sin(theta))+(z_p[9]*math.cos(theta))

 x_p[9]=x
 z_p[9]=z

 #point10
 x=(x_p[10]*math.cos(theta))-(z_p[10]*math.sin(theta))
 z=(x_p[10]*math.sin(theta))+(z_p[10]*math.cos(theta))

 x_p[10]=x
 z_p[10]=z

 #point11
 x=(x_p[11]*math.cos(theta))-(z_p[11]*math.sin(theta))
 z=(x_p[11]*math.sin(theta))+(z_p[11]*math.cos(theta))

 x_p[11]=x
 z_p[11]=z

 #point12
 x=(x_p[12]*math.cos(theta))-(z_p[12]*math.sin(theta))
 z=(x_p[12]*math.sin(theta))+(z_p[12]*math.cos(theta))

 x_p[12]=x
 z_p[12]=z

 #point13
 x=(x_p[13]*math.cos(theta))-(z_p[13]*math.sin(theta))
 z=(x_p[13]*math.sin(theta))+(z_p[13]*math.cos(theta))

 x_p[13]=x
 z_p[13]=z

 #point14
 x=(x_p[14]*math.cos(theta))-(z_p[14]*math.sin(theta))
 z=(x_p[14]*math.sin(theta))+(z_p[14]*math.cos(theta))

 x_p[14]=x
 z_p[14]=z

 #point15
 x=(x_p[15]*math.cos(theta))-(z_p[15]*math.sin(theta))
 z=(x_p[15]*math.sin(theta))+(z_p[15]*math.cos(theta))

 x_p[15]=x
 z_p[15]=z



#counter rotate xz plane
def counter_rotate_xz(x,y,z,w):

 #point0
 x=(x_p[0]*math.cos(theta))+(z_p[0]*math.sin(theta))
 z=-(x_p[0]*math.sin(theta))+(z_p[0]*math.cos(theta))

 x_p[0]=x
 z_p[0]=z

 #point1
 x=(x_p[1]*math.cos(theta))+(z_p[1]*math.sin(theta))
 z=-(x_p[1]*math.sin(theta))+(z_p[1]*math.cos(theta))

 x_p[1]=x
 z_p[1]=z

 #point2
 x=(x_p[2]*math.cos(theta))+(z_p[2]*math.sin(theta))
 z=-(x_p[2]*math.sin(theta))+(z_p[2]*math.cos(theta))

 x_p[2]=x
 z_p[2]=z

 #point3
 x=(x_p[3]*math.cos(theta))+(z_p[3]*math.sin(theta))
 z=-(x_p[3]*math.sin(theta))+(z_p[3]*math.cos(theta))

 x_p[3]=x
 z_p[3]=z

 #point4
 x=(x_p[4]*math.cos(theta))+(z_p[4]*math.sin(theta))
 z=-(x_p[4]*math.sin(theta))+(z_p[4]*math.cos(theta))

 x_p[4]=x
 z_p[4]=z

 #point5
 x=(x_p[5]*math.cos(theta))+(z_p[5]*math.sin(theta))
 z=-(x_p[5]*math.sin(theta))+(z_p[5]*math.cos(theta))

 x_p[5]=x
 z_p[5]=z

 #point6
 x=(x_p[6]*math.cos(theta))+(z_p[6]*math.sin(theta))
 z=-(x_p[6]*math.sin(theta))+(z_p[6]*math.cos(theta))

 x_p[6]=x
 z_p[6]=z

 #point7
 x=(x_p[7]*math.cos(theta))+(z_p[7]*math.sin(theta))
 z=-(x_p[7]*math.sin(theta))+(z_p[7]*math.cos(theta))

 x_p[7]=x
 z_p[7]=z

 #point8
 x=(x_p[8]*math.cos(theta))+(z_p[8]*math.sin(theta))
 z=-(x_p[8]*math.sin(theta))+(z_p[8]*math.cos(theta))

 x_p[8]=x
 z_p[8]=z

 #point9
 x=(x_p[9]*math.cos(theta))+(z_p[9]*math.sin(theta))
 z=-(x_p[9]*math.sin(theta))+(z_p[9]*math.cos(theta))

 x_p[9]=x
 z_p[9]=z

 #point10
 x=(x_p[10]*math.cos(theta))+(z_p[10]*math.sin(theta))
 z=-(x_p[10]*math.sin(theta))+(z_p[10]*math.cos(theta))

 x_p[10]=x
 z_p[10]=z

 #point11
 x=(x_p[11]*math.cos(theta))+(z_p[11]*math.sin(theta))
 z=-(x_p[11]*math.sin(theta))+(z_p[11]*math.cos(theta))

 x_p[11]=x
 z_p[11]=z

 #point12
 x=(x_p[12]*math.cos(theta))+(z_p[12]*math.sin(theta))
 z=-(x_p[12]*math.sin(theta))+(z_p[12]*math.cos(theta))

 x_p[12]=x
 z_p[12]=z

 #point13
 x=(x_p[13]*math.cos(theta))+(z_p[13]*math.sin(theta))
 z=-(x_p[13]*math.sin(theta))+(z_p[13]*math.cos(theta))

 x_p[13]=x
 z_p[13]=z

 #point14
 x=(x_p[14]*math.cos(theta))+(z_p[14]*math.sin(theta))
 z=-(x_p[14]*math.sin(theta))+(z_p[14]*math.cos(theta))

 x_p[14]=x
 z_p[14]=z

 #point15
 x=(x_p[15]*math.cos(theta))+(z_p[15]*math.sin(theta))
 z=-(x_p[15]*math.sin(theta))+(z_p[15]*math.cos(theta))

 x_p[15]=x
 z_p[15]=z



#rotate xw plane
def rotate_xw(x,y,z,w):

 #point0
 x=(x_p[0]*math.cos(theta))-(w_p[0]*math.sin(theta))
 w=(x_p[0]*math.sin(theta))+(w_p[0]*math.cos(theta))

 x_p[0]=x
 w_p[0]=w

 #point1
 x=(x_p[1]*math.cos(theta))-(w_p[1]*math.sin(theta))
 w=(x_p[1]*math.sin(theta))+(w_p[1]*math.cos(theta))

 x_p[1]=x
 w_p[1]=w

 #point2
 x=(x_p[2]*math.cos(theta))-(w_p[2]*math.sin(theta))
 w=(x_p[2]*math.sin(theta))+(w_p[2]*math.cos(theta))

 x_p[2]=x
 w_p[2]=w

 #point3
 x=(x_p[3]*math.cos(theta))-(w_p[3]*math.sin(theta))
 w=(x_p[3]*math.sin(theta))+(w_p[3]*math.cos(theta))

 x_p[3]=x
 w_p[3]=w

 #point4
 x=(x_p[4]*math.cos(theta))-(w_p[4]*math.sin(theta))
 w=(x_p[4]*math.sin(theta))+(w_p[4]*math.cos(theta))

 x_p[4]=x
 w_p[4]=w

 #point5
 x=(x_p[5]*math.cos(theta))-(w_p[5]*math.sin(theta))
 w=(x_p[5]*math.sin(theta))+(w_p[5]*math.cos(theta))

 x_p[5]=x
 w_p[5]=w

 #point6
 x=(x_p[6]*math.cos(theta))-(w_p[6]*math.sin(theta))
 w=(x_p[6]*math.sin(theta))+(w_p[6]*math.cos(theta))

 x_p[6]=x
 w_p[6]=w

 #point7
 x=(x_p[7]*math.cos(theta))-(w_p[7]*math.sin(theta))
 w=(x_p[7]*math.sin(theta))+(w_p[7]*math.cos(theta))

 x_p[7]=x
 w_p[7]=w

 #point8
 x=(x_p[8]*math.cos(theta))-(w_p[8]*math.sin(theta))
 w=(x_p[8]*math.sin(theta))+(w_p[8]*math.cos(theta))

 x_p[8]=x
 w_p[8]=w

 #point9
 x=(x_p[9]*math.cos(theta))-(w_p[9]*math.sin(theta))
 w=(x_p[9]*math.sin(theta))+(w_p[9]*math.cos(theta))

 x_p[9]=x
 w_p[9]=w

 #point10
 x=(x_p[10]*math.cos(theta))-(w_p[10]*math.sin(theta))
 w=(x_p[10]*math.sin(theta))+(w_p[10]*math.cos(theta))

 x_p[10]=x
 w_p[10]=w

 #point11
 x=(x_p[11]*math.cos(theta))-(w_p[11]*math.sin(theta))
 w=(x_p[11]*math.sin(theta))+(w_p[11]*math.cos(theta))

 x_p[11]=x
 w_p[11]=w

 #point12
 x=(x_p[12]*math.cos(theta))-(w_p[12]*math.sin(theta))
 w=(x_p[12]*math.sin(theta))+(w_p[12]*math.cos(theta))

 x_p[12]=x
 w_p[12]=w

 #point13
 x=(x_p[13]*math.cos(theta))-(w_p[13]*math.sin(theta))
 w=(x_p[13]*math.sin(theta))+(w_p[13]*math.cos(theta))

 x_p[13]=x
 w_p[13]=w

 #point14
 x=(x_p[14]*math.cos(theta))-(w_p[14]*math.sin(theta))
 w=(x_p[14]*math.sin(theta))+(w_p[14]*math.cos(theta))

 x_p[14]=x
 w_p[14]=w

 #point15
 x=(x_p[15]*math.cos(theta))-(w_p[15]*math.sin(theta))
 w=(x_p[15]*math.sin(theta))+(w_p[15]*math.cos(theta))

 x_p[15]=x
 w_p[15]=w




#counter rotate xw plane
def counter_rotate_xw(x,y,z,w):

 #point0
 x=(x_p[0]*math.cos(theta))+(w_p[0]*math.sin(theta))
 w=-(x_p[0]*math.sin(theta))+(w_p[0]*math.cos(theta))

 x_p[0]=x
 w_p[0]=w

 #point1
 x=(x_p[1]*math.cos(theta))+(w_p[1]*math.sin(theta))
 w=-(x_p[1]*math.sin(theta))+(w_p[1]*math.cos(theta))

 x_p[1]=x
 w_p[1]=w

 #point2
 x=(x_p[2]*math.cos(theta))+(w_p[2]*math.sin(theta))
 w=-(x_p[2]*math.sin(theta))+(w_p[2]*math.cos(theta))

 x_p[2]=x
 w_p[2]=w

 #point3
 x=(x_p[3]*math.cos(theta))+(w_p[3]*math.sin(theta))
 w=-(x_p[3]*math.sin(theta))+(w_p[3]*math.cos(theta))

 x_p[3]=x
 w_p[3]=w

 #point4
 x=(x_p[4]*math.cos(theta))+(w_p[4]*math.sin(theta))
 w=-(x_p[4]*math.sin(theta))+(w_p[4]*math.cos(theta))

 x_p[4]=x
 w_p[4]=w

 #point5
 x=(x_p[5]*math.cos(theta))+(w_p[5]*math.sin(theta))
 w=-(x_p[5]*math.sin(theta))+(w_p[5]*math.cos(theta))

 x_p[5]=x
 w_p[5]=w

 #point6
 x=(x_p[6]*math.cos(theta))+(w_p[6]*math.sin(theta))
 w=-(x_p[6]*math.sin(theta))+(w_p[6]*math.cos(theta))

 x_p[6]=x
 w_p[6]=w

 #point7
 x=(x_p[7]*math.cos(theta))+(w_p[7]*math.sin(theta))
 w=-(x_p[7]*math.sin(theta))+(w_p[7]*math.cos(theta))

 x_p[7]=x
 w_p[7]=w

 #point8
 x=(x_p[8]*math.cos(theta))+(w_p[8]*math.sin(theta))
 w=-(x_p[8]*math.sin(theta))+(w_p[8]*math.cos(theta))

 x_p[8]=x
 w_p[8]=w

 #point9
 x=(x_p[9]*math.cos(theta))+(w_p[9]*math.sin(theta))
 w=-(x_p[9]*math.sin(theta))+(w_p[9]*math.cos(theta))

 x_p[9]=x
 w_p[9]=w

 #point10
 x=(x_p[10]*math.cos(theta))+(w_p[10]*math.sin(theta))
 w=-(x_p[10]*math.sin(theta))+(w_p[10]*math.cos(theta))

 x_p[10]=x
 w_p[10]=w

 #point11
 x=(x_p[11]*math.cos(theta))+(w_p[11]*math.sin(theta))
 w=-(x_p[11]*math.sin(theta))+(w_p[11]*math.cos(theta))

 x_p[11]=x
 w_p[11]=w

 #point12
 x=(x_p[12]*math.cos(theta))+(w_p[12]*math.sin(theta))
 w=-(x_p[12]*math.sin(theta))+(w_p[12]*math.cos(theta))

 x_p[12]=x
 w_p[12]=w

 #point13
 x=(x_p[13]*math.cos(theta))+(w_p[13]*math.sin(theta))
 w=-(x_p[13]*math.sin(theta))+(w_p[13]*math.cos(theta))

 x_p[13]=x
 w_p[13]=w

 #point14
 x=(x_p[14]*math.cos(theta))+(w_p[14]*math.sin(theta))
 w=-(x_p[14]*math.sin(theta))+(w_p[14]*math.cos(theta))

 x_p[14]=x
 w_p[14]=w

 #point15
 x=(x_p[15]*math.cos(theta))+(w_p[15]*math.sin(theta))
 w=-(x_p[15]*math.sin(theta))+(w_p[15]*math.cos(theta))

 x_p[15]=x
 w_p[15]=w




#rotate yz plane
def rotate_yz(x,y,z,w):

 #point0
 y=(y_p[0]*math.cos(theta))-(z_p[0]*math.sin(theta))
 z=(y_p[0]*math.sin(theta))+(z_p[0]*math.cos(theta))

 y_p[0]=y
 z_p[0]=z

 #point1
 y=(y_p[1]*math.cos(theta))-(z_p[1]*math.sin(theta))
 z=(y_p[1]*math.sin(theta))+(z_p[1]*math.cos(theta))

 y_p[1]=y
 z_p[1]=z

 #point2
 y=(y_p[2]*math.cos(theta))-(z_p[2]*math.sin(theta))
 z=(y_p[2]*math.sin(theta))+(z_p[2]*math.cos(theta))

 y_p[2]=y
 z_p[2]=z

 #point3
 y=(y_p[3]*math.cos(theta))-(z_p[3]*math.sin(theta))
 z=(y_p[3]*math.sin(theta))+(z_p[3]*math.cos(theta))

 y_p[3]=y
 z_p[3]=z

 #point4
 y=(y_p[4]*math.cos(theta))-(z_p[4]*math.sin(theta))
 z=(y_p[4]*math.sin(theta))+(z_p[4]*math.cos(theta))

 y_p[4]=y
 z_p[4]=z

 #point5
 y=(y_p[5]*math.cos(theta))-(z_p[5]*math.sin(theta))
 z=(y_p[5]*math.sin(theta))+(z_p[5]*math.cos(theta))

 y_p[5]=y
 z_p[5]=z

 #point6
 y=(y_p[6]*math.cos(theta))-(z_p[6]*math.sin(theta))
 z=(y_p[6]*math.sin(theta))+(z_p[6]*math.cos(theta))

 y_p[6]=y
 z_p[6]=z

 #point7
 y=(y_p[7]*math.cos(theta))-(z_p[7]*math.sin(theta))
 z=(y_p[7]*math.sin(theta))+(z_p[7]*math.cos(theta))

 y_p[7]=y
 z_p[7]=z

 #point8
 y=(y_p[8]*math.cos(theta))-(z_p[8]*math.sin(theta))
 z=(y_p[8]*math.sin(theta))+(z_p[8]*math.cos(theta))

 y_p[8]=y
 z_p[8]=z

 #point9
 y=(y_p[9]*math.cos(theta))-(z_p[9]*math.sin(theta))
 z=(y_p[9]*math.sin(theta))+(z_p[9]*math.cos(theta))

 y_p[9]=y
 z_p[9]=z

 #point10
 y=(y_p[10]*math.cos(theta))-(z_p[10]*math.sin(theta))
 z=(y_p[10]*math.sin(theta))+(z_p[10]*math.cos(theta))

 y_p[10]=y
 z_p[10]=z

 #point11
 y=(y_p[11]*math.cos(theta))-(z_p[11]*math.sin(theta))
 z=(y_p[11]*math.sin(theta))+(z_p[11]*math.cos(theta))

 y_p[11]=y
 z_p[11]=z

 #point12
 y=(y_p[12]*math.cos(theta))-(z_p[12]*math.sin(theta))
 z=(y_p[12]*math.sin(theta))+(z_p[12]*math.cos(theta))

 y_p[12]=y
 z_p[12]=z

 #point13
 y=(y_p[13]*math.cos(theta))-(z_p[13]*math.sin(theta))
 z=(y_p[13]*math.sin(theta))+(z_p[13]*math.cos(theta))

 y_p[13]=y
 z_p[13]=z

 #point14
 y=(y_p[14]*math.cos(theta))-(z_p[14]*math.sin(theta))
 z=(y_p[14]*math.sin(theta))+(z_p[14]*math.cos(theta))

 y_p[14]=y
 z_p[14]=z

 #point15
 y=(y_p[15]*math.cos(theta))-(z_p[15]*math.sin(theta))
 z=(y_p[15]*math.sin(theta))+(z_p[15]*math.cos(theta))

 y_p[15]=y
 z_p[15]=z





#counter rotate yz plane
def counter_rotate_yz(x,y,z,w):

 #point0
 y=(y_p[0]*math.cos(theta))+(z_p[0]*math.sin(theta))
 z=-(y_p[0]*math.sin(theta))+(z_p[0]*math.cos(theta))

 y_p[0]=y
 z_p[0]=z

 #point1
 y=(y_p[1]*math.cos(theta))+(z_p[1]*math.sin(theta))
 z=-(y_p[1]*math.sin(theta))+(z_p[1]*math.cos(theta))

 y_p[1]=y
 z_p[1]=z

 #point2
 y=(y_p[2]*math.cos(theta))+(z_p[2]*math.sin(theta))
 z=-(y_p[2]*math.sin(theta))+(z_p[2]*math.cos(theta))

 y_p[2]=y
 z_p[2]=z

 #point3
 y=(y_p[3]*math.cos(theta))+(z_p[3]*math.sin(theta))
 z=-(y_p[3]*math.sin(theta))+(z_p[3]*math.cos(theta))

 y_p[3]=y
 z_p[3]=z

 #point4
 y=(y_p[4]*math.cos(theta))+(z_p[4]*math.sin(theta))
 z=-(y_p[4]*math.sin(theta))+(z_p[4]*math.cos(theta))

 y_p[4]=y
 z_p[4]=z

 #point5
 y=(y_p[5]*math.cos(theta))+(z_p[5]*math.sin(theta))
 z=-(y_p[5]*math.sin(theta))+(z_p[5]*math.cos(theta))

 y_p[5]=y
 z_p[5]=z

 #point6
 y=(y_p[6]*math.cos(theta))+(z_p[6]*math.sin(theta))
 z=-(y_p[6]*math.sin(theta))+(z_p[6]*math.cos(theta))

 y_p[6]=y
 z_p[6]=z

 #point7
 y=(y_p[7]*math.cos(theta))+(z_p[7]*math.sin(theta))
 z=-(y_p[7]*math.sin(theta))+(z_p[7]*math.cos(theta))

 y_p[7]=y
 z_p[7]=z

 #point8
 y=(y_p[8]*math.cos(theta))+(z_p[8]*math.sin(theta))
 z=-(y_p[8]*math.sin(theta))+(z_p[8]*math.cos(theta))

 y_p[8]=y
 z_p[8]=z

 #point9
 y=(y_p[9]*math.cos(theta))+(z_p[9]*math.sin(theta))
 z=-(y_p[9]*math.sin(theta))+(z_p[9]*math.cos(theta))

 y_p[9]=y
 z_p[9]=z

 #point10
 y=(y_p[10]*math.cos(theta))+(z_p[10]*math.sin(theta))
 z=-(y_p[10]*math.sin(theta))+(z_p[10]*math.cos(theta))

 y_p[10]=y
 z_p[10]=z

 #point11
 y=(y_p[11]*math.cos(theta))+(z_p[11]*math.sin(theta))
 z=-(y_p[11]*math.sin(theta))+(z_p[11]*math.cos(theta))

 y_p[11]=y
 z_p[11]=z

 #point12
 y=(y_p[12]*math.cos(theta))+(z_p[12]*math.sin(theta))
 z=-(y_p[12]*math.sin(theta))+(z_p[12]*math.cos(theta))

 y_p[12]=y
 z_p[12]=z

 #point13
 y=(y_p[13]*math.cos(theta))+(z_p[13]*math.sin(theta))
 z=-(y_p[13]*math.sin(theta))+(z_p[13]*math.cos(theta))

 y_p[13]=y
 z_p[13]=z

 #point14
 y=(y_p[14]*math.cos(theta))+(z_p[14]*math.sin(theta))
 z=-(y_p[14]*math.sin(theta))+(z_p[14]*math.cos(theta))

 y_p[14]=y
 z_p[14]=z

 #point15
 y=(y_p[15]*math.cos(theta))+(z_p[15]*math.sin(theta))
 z=-(y_p[15]*math.sin(theta))+(z_p[15]*math.cos(theta))

 y_p[15]=y
 z_p[15]=z




#rotate yw plane
def rotate_yw(x,y,z,w):

 #point0
 y=(y_p[0]*math.cos(theta))-(w_p[0]*math.sin(theta))
 w=(y_p[0]*math.sin(theta))+(w_p[0]*math.cos(theta))

 y_p[0]=y
 w_p[0]=w

 #point1
 y=(y_p[1]*math.cos(theta))-(w_p[1]*math.sin(theta))
 w=(y_p[1]*math.sin(theta))+(w_p[1]*math.cos(theta))

 y_p[1]=y
 w_p[1]=w

 #point2
 y=(y_p[2]*math.cos(theta))-(w_p[2]*math.sin(theta))
 w=(y_p[2]*math.sin(theta))+(w_p[2]*math.cos(theta))

 y_p[2]=y
 w_p[2]=w

 #point3
 y=(y_p[3]*math.cos(theta))-(w_p[3]*math.sin(theta))
 w=(y_p[3]*math.sin(theta))+(w_p[3]*math.cos(theta))

 y_p[3]=y
 w_p[3]=w

 #point4
 y=(y_p[4]*math.cos(theta))-(w_p[4]*math.sin(theta))
 w=(y_p[4]*math.sin(theta))+(w_p[4]*math.cos(theta))

 y_p[4]=y
 w_p[4]=w

 #point5
 y=(y_p[5]*math.cos(theta))-(w_p[5]*math.sin(theta))
 w=(y_p[5]*math.sin(theta))+(w_p[5]*math.cos(theta))

 y_p[5]=y
 w_p[5]=w

 #point6
 y=(y_p[6]*math.cos(theta))-(w_p[6]*math.sin(theta))
 w=(y_p[6]*math.sin(theta))+(w_p[6]*math.cos(theta))

 y_p[6]=y
 w_p[6]=w

 #point7
 y=(y_p[7]*math.cos(theta))-(w_p[7]*math.sin(theta))
 w=(y_p[7]*math.sin(theta))+(w_p[7]*math.cos(theta))

 y_p[7]=y
 w_p[7]=w

 #point8
 y=(y_p[8]*math.cos(theta))-(w_p[8]*math.sin(theta))
 w=(y_p[8]*math.sin(theta))+(w_p[8]*math.cos(theta))

 y_p[8]=y
 w_p[8]=w

 #point9
 y=(y_p[9]*math.cos(theta))-(w_p[9]*math.sin(theta))
 w=(y_p[9]*math.sin(theta))+(w_p[9]*math.cos(theta))

 y_p[9]=y
 w_p[9]=w

 #point10
 y=(y_p[10]*math.cos(theta))-(w_p[10]*math.sin(theta))
 w=(y_p[10]*math.sin(theta))+(w_p[10]*math.cos(theta))

 y_p[10]=y
 w_p[10]=w

 #point11
 y=(y_p[11]*math.cos(theta))-(w_p[11]*math.sin(theta))
 w=(y_p[11]*math.sin(theta))+(w_p[11]*math.cos(theta))

 y_p[11]=y
 w_p[11]=w

 #point12
 y=(y_p[12]*math.cos(theta))-(w_p[12]*math.sin(theta))
 w=(y_p[12]*math.sin(theta))+(w_p[12]*math.cos(theta))

 y_p[12]=y
 w_p[12]=w

 #point13
 y=(y_p[13]*math.cos(theta))-(w_p[13]*math.sin(theta))
 w=(y_p[13]*math.sin(theta))+(w_p[13]*math.cos(theta))

 y_p[13]=y
 w_p[13]=w

 #point14
 y=(y_p[14]*math.cos(theta))-(w_p[14]*math.sin(theta))
 w=(y_p[14]*math.sin(theta))+(w_p[14]*math.cos(theta))

 y_p[14]=y
 w_p[14]=w

 #point15
 y=(y_p[15]*math.cos(theta))-(w_p[15]*math.sin(theta))
 w=(y_p[15]*math.sin(theta))+(w_p[15]*math.cos(theta))

 y_p[15]=y
 w_p[15]=w




#counter rotate yw plane
def counter_rotate_yw(x,y,z,w):

 #point0
 y=(y_p[0]*math.cos(theta))+(w_p[0]*math.sin(theta))
 w=-(y_p[0]*math.sin(theta))+(w_p[0]*math.cos(theta))

 y_p[0]=y
 w_p[0]=w

 #point1
 y=(y_p[1]*math.cos(theta))+(w_p[1]*math.sin(theta))
 w=-(y_p[1]*math.sin(theta))+(w_p[1]*math.cos(theta))

 y_p[1]=y
 w_p[1]=w

 #point2
 y=(y_p[2]*math.cos(theta))+(w_p[2]*math.sin(theta))
 w=-(y_p[2]*math.sin(theta))+(w_p[2]*math.cos(theta))

 y_p[2]=y
 w_p[2]=w

 #point3
 y=(y_p[3]*math.cos(theta))+(w_p[3]*math.sin(theta))
 w=-(y_p[3]*math.sin(theta))+(w_p[3]*math.cos(theta))

 y_p[3]=y
 w_p[3]=w

 #point4
 y=(y_p[4]*math.cos(theta))+(w_p[4]*math.sin(theta))
 w=-(y_p[4]*math.sin(theta))+(w_p[4]*math.cos(theta))

 y_p[4]=y
 w_p[4]=w

 #point5
 y=(y_p[5]*math.cos(theta))+(w_p[5]*math.sin(theta))
 w=-(y_p[5]*math.sin(theta))+(w_p[5]*math.cos(theta))

 y_p[5]=y
 w_p[5]=w

 #point6
 y=(y_p[6]*math.cos(theta))+(w_p[6]*math.sin(theta))
 w=-(y_p[6]*math.sin(theta))+(w_p[6]*math.cos(theta))

 y_p[6]=y
 w_p[6]=w

 #point7
 y=(y_p[7]*math.cos(theta))+(w_p[7]*math.sin(theta))
 w=-(y_p[7]*math.sin(theta))+(w_p[7]*math.cos(theta))

 y_p[7]=y
 w_p[7]=w

 #point8
 y=(y_p[8]*math.cos(theta))+(w_p[8]*math.sin(theta))
 w=-(y_p[8]*math.sin(theta))+(w_p[8]*math.cos(theta))

 y_p[8]=y
 w_p[8]=w

 #point9
 y=(y_p[9]*math.cos(theta))+(w_p[9]*math.sin(theta))
 w=-(y_p[9]*math.sin(theta))+(w_p[9]*math.cos(theta))

 y_p[9]=y
 w_p[9]=w

 #point10
 y=(y_p[10]*math.cos(theta))+(w_p[10]*math.sin(theta))
 w=-(y_p[10]*math.sin(theta))+(w_p[10]*math.cos(theta))

 y_p[10]=y
 w_p[10]=w

 #point11
 y=(y_p[11]*math.cos(theta))+(w_p[11]*math.sin(theta))
 w=-(y_p[11]*math.sin(theta))+(w_p[11]*math.cos(theta))

 y_p[11]=y
 w_p[11]=w

 #point12
 y=(y_p[12]*math.cos(theta))+(w_p[12]*math.sin(theta))
 w=-(y_p[12]*math.sin(theta))+(w_p[12]*math.cos(theta))

 y_p[12]=y
 w_p[12]=w

 #point13
 y=(y_p[13]*math.cos(theta))+(w_p[13]*math.sin(theta))
 w=-(y_p[13]*math.sin(theta))+(w_p[13]*math.cos(theta))

 y_p[13]=y
 w_p[13]=w

 #point14
 y=(y_p[14]*math.cos(theta))+(w_p[14]*math.sin(theta))
 w=-(y_p[14]*math.sin(theta))+(w_p[14]*math.cos(theta))

 y_p[14]=y
 w_p[14]=w

 #point15
 y=(y_p[15]*math.cos(theta))+(w_p[15]*math.sin(theta))
 w=-(y_p[15]*math.sin(theta))+(w_p[15]*math.cos(theta))

 y_p[15]=y
 w_p[15]=w




#rotate zw plane
def rotate_zw(x,y,z,w):

 #point0
 z=(z_p[0]*math.cos(theta))-(w_p[0]*math.sin(theta))
 w=(z_p[0]*math.sin(theta))+(w_p[0]*math.cos(theta))

 z_p[0]=z
 w_p[0]=w

 #point1
 z=(z_p[1]*math.cos(theta))-(w_p[1]*math.sin(theta))
 w=(z_p[1]*math.sin(theta))+(w_p[1]*math.cos(theta))

 z_p[1]=z
 w_p[1]=w

 #point2
 z=(z_p[2]*math.cos(theta))-(w_p[2]*math.sin(theta))
 w=(z_p[2]*math.sin(theta))+(w_p[2]*math.cos(theta))

 z_p[2]=z
 w_p[2]=w

 #point3
 z=(z_p[3]*math.cos(theta))-(w_p[3]*math.sin(theta))
 w=(z_p[3]*math.sin(theta))+(w_p[3]*math.cos(theta))

 z_p[3]=z
 w_p[3]=w

 #point4
 z=(z_p[4]*math.cos(theta))-(w_p[4]*math.sin(theta))
 w=(z_p[4]*math.sin(theta))+(w_p[4]*math.cos(theta))

 z_p[4]=z
 w_p[4]=w

 #point5
 z=(z_p[5]*math.cos(theta))-(w_p[5]*math.sin(theta))
 w=(z_p[5]*math.sin(theta))+(w_p[5]*math.cos(theta))

 z_p[5]=z
 w_p[5]=w

 #point6
 z=(z_p[6]*math.cos(theta))-(w_p[6]*math.sin(theta))
 w=(z_p[6]*math.sin(theta))+(w_p[6]*math.cos(theta))

 z_p[6]=z
 w_p[6]=w

 #point7
 z=(z_p[7]*math.cos(theta))-(w_p[7]*math.sin(theta))
 w=(z_p[7]*math.sin(theta))+(w_p[7]*math.cos(theta))

 z_p[7]=z
 w_p[7]=w

 #point8
 z=(z_p[8]*math.cos(theta))-(w_p[8]*math.sin(theta))
 w=(z_p[8]*math.sin(theta))+(w_p[8]*math.cos(theta))

 z_p[8]=z
 w_p[8]=w

 #point9
 z=(z_p[9]*math.cos(theta))-(w_p[9]*math.sin(theta))
 w=(z_p[9]*math.sin(theta))+(w_p[9]*math.cos(theta))

 z_p[9]=z
 w_p[9]=w

 #point10
 z=(z_p[10]*math.cos(theta))-(w_p[10]*math.sin(theta))
 w=(z_p[10]*math.sin(theta))+(w_p[10]*math.cos(theta))

 z_p[10]=z
 w_p[10]=w

 #point11
 z=(z_p[11]*math.cos(theta))-(w_p[11]*math.sin(theta))
 w=(z_p[11]*math.sin(theta))+(w_p[11]*math.cos(theta))

 z_p[11]=z
 w_p[11]=w

 #point12
 z=(z_p[12]*math.cos(theta))-(w_p[12]*math.sin(theta))
 w=(z_p[12]*math.sin(theta))+(w_p[12]*math.cos(theta))

 z_p[12]=z
 w_p[12]=w

 #point13
 z=(z_p[13]*math.cos(theta))-(w_p[13]*math.sin(theta))
 w=(z_p[13]*math.sin(theta))+(w_p[13]*math.cos(theta))

 z_p[13]=z
 w_p[13]=w

 #point14
 z=(z_p[14]*math.cos(theta))-(w_p[14]*math.sin(theta))
 w=(z_p[14]*math.sin(theta))+(w_p[14]*math.cos(theta))

 z_p[14]=z
 w_p[14]=w

 #point15
 z=(z_p[15]*math.cos(theta))-(w_p[15]*math.sin(theta))
 w=(z_p[15]*math.sin(theta))+(w_p[15]*math.cos(theta))

 z_p[15]=z
 w_p[15]=w




#counter rotate zw plane
def counter_rotate_zw(x,y,z,w):

 #point0
 z=(z_p[0]*math.cos(theta))+(w_p[0]*math.sin(theta))
 w=-(z_p[0]*math.sin(theta))+(w_p[0]*math.cos(theta))

 z_p[0]=z
 w_p[0]=w

 #point1
 z=(z_p[1]*math.cos(theta))+(w_p[1]*math.sin(theta))
 w=-(z_p[1]*math.sin(theta))+(w_p[1]*math.cos(theta))

 z_p[1]=z
 w_p[1]=w

 #point2
 z=(z_p[2]*math.cos(theta))+(w_p[2]*math.sin(theta))
 w=-(z_p[2]*math.sin(theta))+(w_p[2]*math.cos(theta))

 z_p[2]=z
 w_p[2]=w

 #point3
 z=(z_p[3]*math.cos(theta))+(w_p[3]*math.sin(theta))
 w=-(z_p[3]*math.sin(theta))+(w_p[3]*math.cos(theta))

 z_p[3]=z
 w_p[3]=w

 #point4
 z=(z_p[4]*math.cos(theta))+(w_p[4]*math.sin(theta))
 w=-(z_p[4]*math.sin(theta))+(w_p[4]*math.cos(theta))

 z_p[4]=z
 w_p[4]=w

 #point5
 z=(z_p[5]*math.cos(theta))+(w_p[5]*math.sin(theta))
 w=-(z_p[5]*math.sin(theta))+(w_p[5]*math.cos(theta))

 z_p[5]=z
 w_p[5]=w

 #point6
 z=(z_p[6]*math.cos(theta))+(w_p[6]*math.sin(theta))
 w=-(z_p[6]*math.sin(theta))+(w_p[6]*math.cos(theta))

 z_p[6]=z
 w_p[6]=w

 #point7
 z=(z_p[7]*math.cos(theta))+(w_p[7]*math.sin(theta))
 w=-(z_p[7]*math.sin(theta))+(w_p[7]*math.cos(theta))

 z_p[7]=z
 w_p[7]=w

 #point8
 z=(z_p[8]*math.cos(theta))+(w_p[8]*math.sin(theta))
 w=-(z_p[8]*math.sin(theta))+(w_p[8]*math.cos(theta))

 z_p[8]=z
 w_p[8]=w

 #point9
 z=(z_p[9]*math.cos(theta))+(w_p[9]*math.sin(theta))
 w=-(z_p[9]*math.sin(theta))+(w_p[9]*math.cos(theta))

 z_p[9]=z
 w_p[9]=w

 #point10
 z=(z_p[10]*math.cos(theta))+(w_p[10]*math.sin(theta))
 w=-(z_p[10]*math.sin(theta))+(w_p[10]*math.cos(theta))

 z_p[10]=z
 w_p[10]=w

 #point11
 z=(z_p[11]*math.cos(theta))+(w_p[11]*math.sin(theta))
 w=-(z_p[11]*math.sin(theta))+(w_p[11]*math.cos(theta))

 z_p[11]=z
 w_p[11]=w

 #point12
 z=(z_p[12]*math.cos(theta))+(w_p[12]*math.sin(theta))
 w=-(z_p[12]*math.sin(theta))+(w_p[12]*math.cos(theta))

 z_p[12]=z
 w_p[12]=w

 #point13
 z=(z_p[13]*math.cos(theta))+(w_p[13]*math.sin(theta))
 w=-(z_p[13]*math.sin(theta))+(w_p[13]*math.cos(theta))

 z_p[13]=z
 w_p[13]=w

 #point14
 z=(z_p[14]*math.cos(theta))+(w_p[14]*math.sin(theta))
 w=-(z_p[14]*math.sin(theta))+(w_p[14]*math.cos(theta))

 z_p[14]=z
 w_p[14]=w

 #point15
 z=(z_p[15]*math.cos(theta))+(w_p[15]*math.sin(theta))
 w=-(z_p[15]*math.sin(theta))+(w_p[15]*math.cos(theta))

 z_p[15]=z
 w_p[15]=w





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
        t3=threading.Thread(target=move.orthographic(x,y,z,w))
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
