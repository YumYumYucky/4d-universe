import math


def c_p(x,y,z,w):
  global r, theta, psi, omega
  r=math.sqrt(x**2+y**2+z**2+w**2)
  theta=math.acos(w/r)
  psi=math.acos(z/math.sqrt(x**2+y**2+z**2))
  omega=math.atan(x/y)


  print(f'magnatude= {r}')
  print(f'theta= {theta}')
  print(f'psi= {psi}')
  print(f'omega= {omega}')

def p_c(r,theta,psi,omega):

 global x, y, z, w

 x=round(r*math.sin(theta)*math.sin(psi)*math.sin(omega))
 y=round(r*math.sin(theta)*math.sin(psi)*math.cos(omega))
 z=round(r*math.sin(theta)*math.cos(psi))
 w=round(r*math.cos(theta))

 print(f'x= {x}')
 print(f'y= {y}')
 print(f'z= {z}')
 print(f'w= {w}')


x=int(input('x='))
y=int(input('y='))
z=int(input('z='))
w=int(input('w='))

c_p(x,y,z,w)

p_c(r,theta,psi,omega)



