# 4d-universe



creates a hypercube with a hyper pyramid on one side of it.

rotates the hyper cube along two axis

j- rotates xy plane
l- counter-rotates xy plane

i- rotates xz plane
k- counter-rotates xz plane

t- rotates xw plane
u- counter-rotates xw plane

y- rotates yz plane
h- counter-rotates yz plane

f- rotates yw plane
v- counter-rotates yw plane

c- rotates zw plane
b- counter-rotates zw plane


The hyper cube can also be moved

d- x higher
a- x lower

w- y higher
s- y lower

UP- z higher
DOWN- z lower

RIGHT- w higher
LEFT- w lower


Uses a steriographic projection to display the hyper cube

Uses OpenGl to display the hyper cube


Trying to add that the movement goes in the direction that the hypercube is facing the hyper pyramid being the direction that it is facing.
Try to give the cube a velocity that can be updated every unit of time.
Try to impliment gravity having the source be at 0,0,0,0 can have a velocity vetor that faces twords the orgin and magnatude of 1/r^3 so it is like 4D gravity
Try to Make a hyper sphere around the orgin and have collision when the hyper cube goes into it. 




new.py              moves a point around 4d space
polar.py            convers a polar cordinate system into a cartesian cordinate system of the other way around
opengltest.py       was the first try to impliment rotataion of a hyper cube in 4d
OpenGlrotation.py   was the second time implimenting rotataion of a hyper cube but more efficient
gametime.py         Attempt to make a game timer

