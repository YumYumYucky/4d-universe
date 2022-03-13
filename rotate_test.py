 # dirived from https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/

import pygame
import time
import threading
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *





global x_p, y_p, z_p, w_p, direction, theta

x_p=[1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,0]
y_p=[-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,0]
z_p=[-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,0]
w_p=[1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,2]
direction=[0,1,0,0]

l=2.1


#rotation increments
theta=(math.pi)/128



class move:


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









 def positions():
    print(f'\n{x_p[1]}')
    print(f'{y_p[1]}')
    print(f'{z_p[1]}')
    print(f'{w_p[1]}')


    print(f'\nend\n{x_p[15]}')
    print(f'{y_p[15]}')
    print(f'{z_p[15]}')
    print(f'{w_p[15]}')

    print(f'direction= {direction}')

    print(f'direction magnitude={math.sqrt((direction[0])**2+(direction[1])**2)}')






def rotate_direction(plane, rotation):
 global direction

 if rotation=='rotate':
  #print(f'plane[0]={plane[0]} and plane[1]={plane[1]}')
  direction0=(direction[plane[0]]*math.cos(theta))-(direction[plane[1]]*math.sin(theta))
  direction1=(direction[plane[0]]*math.sin(theta))+(direction[plane[1]]*math.cos(theta))

  direction[plane[0]]=direction0
  direction[plane[1]]=direction1

 if rotation=='counter_rotate':
  direction0=(direction[plane[0]]*math.cos(theta))+(direction[plane[1]]*math.sin(theta))
  direction1=-(direction[plane[0]]*math.sin(theta))+(direction[plane[1]]*math.cos(theta))


  direction[plane[0]]=direction0
  direction[plane[1]]=direction1





def rotate_plane(first_axis,second_axis,plane):
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

















def main():
    pygame.init()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    



        t1=threading.Thread(target=move.press())
        t4=threading.Thread(target=move.positions())
    

        t1.start()

        #steriograhic projection
        #t2.start()

        #orthographic projection
        #t3.start()

      #  t5.start()

        for a in range(100):
         plane=[0,1]
         rotation='rotate'
         rotate_plane(x_p,y_p,plane)
         rotate_direction(plane,rotation)

      

main()




