# importing pygame module
import pygame
import threading
import time
import math

pygame.init()

#screen
SCREEN_WIDTH=400
SCREEN_HEIGHT=400
moving=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('moving')

global x,y,z,w

interval=0.1

x_speed=0
y_speed=0
z_speed=0
w_speed=0

x=0
y=0
z=0
w=0

r=0
theta=0
psi=0
omega=0

r_speed=0
theta_speed=0
psi_speed=0
omega_speed=0

class move:

 def __init__(self, interval, function,X):
  self._timer = None
  self.interval = interval
  self.function = function
  self.args = args
  self.kwargs = kwargs
  self.is_running = False
  self.next_call = time.time()
  self.start()
  self.rect.center=(x)
  Thread.__init__(self)


 def press(x_axis,y_axis,z_axis,w_axis):
 
   global x_speed, y_speed, z_speed, w_speed, velocity
   x_speed=x_axis
   y_speed=y_axis
   z_speed=z_axis
   w_speed=w_axis

  
   key=pygame.key.get_pressed()
   if key[pygame.K_d]:
    x_speed=x_speed+1
   if key[pygame.K_a]:
    x_speed=x_speed-1
   if key[pygame.K_w]:
    y_speed=y_speed+1
   if key[pygame.K_s]:
    y_speed=y_speed-1
   if key[pygame.K_UP]:
    z_speed=z_speed+1
   if key[pygame.K_DOWN]:
    z_speed=z_speed-1
   if key[pygame.K_RIGHT]:
    w_speed=w_speed+1
   if key[pygame.K_LEFT]:
    w_speed=w_speed-1
  
   velocity=math.sqrt(x_speed**2+y_speed**2+z_speed**2+w_speed**2)

 def printing(x_speed, y_speed, z_speed ,w_speed):

   time.sleep(.1)
   print(f'x={x_speed} y={y_speed} z={z_speed} w={w_speed}')
   print(f'Your velocity is: {velocity}')
  


 def start(self):
   if not self.is_running:
     self.next_call += self.interval
     self._timer = threading.Timer(self.next_call - time.time(), self._run)
     self._timer.start()
     self.is_running = True



 def move(x_speed,y_speed,z_speed,w_speed,x,y,z,w):

   x=x+x_speed
   y=y+y_speed
   z=z+z_speed
   w=w+w_speed
   
   distance=math.sqrt(x**2+y**2+z**2+w**2)
   print(f'Distance from orgin= {distance}\n')

   
location=move
run=True
while run:

 t1=threading.Thread(target=move.press(x_speed,y_speed,z_speed,w_speed))
 t2=threading.Thread(target=move.printing(x_speed,y_speed,z_speed,w_speed))
 tmove=threading.Thread(target=move.move(x_speed,y_speed,z_speed,w_speed,x,y,z,w))

 t1.start()
 t2.start()
 tmove.start()


 for event in pygame.event.get():
  if event.type==pygame.QUIT:
   run=False

pygame.quit()
