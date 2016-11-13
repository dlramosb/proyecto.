from visual import *
from math import *
import numpy as np
from array import array
import random 
N=1
G=9.8
ball=range(N)
for i in range(N):
  ball[i]=sphere(pos=vector(-1,4,1),radius=0.8,color=color.red,mass=0,velocity=vector(0,-2,0))

for i in range(10):
 
 print(random.randrange(1,2))


wallR =box(pos=vector(0,-0.8,0),size=vector(12,0.5,12),color=color.white)
wall  =box(pos=vector(0,10.8,0),size=vector(12,0.5,12),color=color.white)

wallLR =box(pos=vector(5+1,5,0),size=vector(0.5,12,12),color=color.white)
wallL  =box(pos=vector(-5-1,5,0),size=vector(0.5,12,12),color=color.white)


wallUR  =box(pos=vector(0,5,-6),size=vector(12,12,0.5),color=color.white)
wallU  =box(pos=vector(0,5,6),size=vector(12,12,0.5),color=color.white,opacity=0.1)

dT=0.01
T=0
for i in range(N):
  ball[i].pos=ball[i].pos+ball[i].velocity*dT

while T < 100:
  rate(80)
  
  for i in range(N):  
    #print(ball.pos," ",T)
  
    if ball[i].pos.y < wallR.pos.y+1:
        ball[i].velocity.y=-ball[i].velocity.y
  for i in range(N): 
 
    if ball[i].pos.y > wall.pos.y-1:
       ball[i].velocity.y=-ball[i].velocity.y
  for i in range(N):      
    if ball[i].pos.x > wallLR.pos.x-1:
       ball[i].velocity.x=-ball[i].velocity.x
  for i in range(N):   
    if ball[i].pos.x < wallL.pos.x+1:
       ball[i].velocity.x=-ball[i].velocity.x
  for i in range(N):   
    if ball[i].pos.z < wallU.pos.z-1:
       ball[i].velocity.z=-ball[i].velocity.z
  for i in range(N):   
    if ball[i].pos.z > wallUR.pos.z+1:
       ball[i].velocity.z=-ball[i].velocity.z
       
    ball[i].pos = ball[i].pos + ball[i].velocity*dT 
    T = T + dT
