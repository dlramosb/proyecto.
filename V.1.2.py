from visual import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from array import array
import random

## Constantes --------

N=1
G=9.8
dt=0.01
t=0

## Generador de bolas en la caja ----

ball=range(N)

for i in range(N):
  ball[i]=sphere( pos=vector(-1*i,4,1) , radius=0.8 , color=color.red , mass=20 , velocity=vector(0,2,0), force=vector(0,0,0) )


## Caja ------
  
wallR =box(pos=vector(0,0,0),size=vector(12,0.5,12),color=color.white)
wall  =box(pos=vector(0,11.6,0),size=vector(12,0.5,12),color=color.white)

wallLR =box(pos=vector(5+1,5.8,0),size=vector(0.5,12,12),color=color.white)
wallL  =box(pos=vector(-5-1,5.8,0),size=vector(0.5,12,12),color=color.white)

wallUR  =box(pos=vector(0,5.8,-6),size=vector(12,12,0.5),color=color.white)
wallU  =box(pos=vector(0,5.8,6),size=vector(12,12,0.5),color=color.white,opacity=0.1)



## computer forces -------

for i in range(N):
      ball[i].force.y=ball[i].force.y-ball[i].mass*G

def computer_force(i):
    
    
 for i in range(N):      
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
       
## ---------------     

while t < 100:
  rate(80)
  t = t + dt

## Arranque ---------
  U=range(N)
  K=range(N)
  for i in range(N): 
      dr = ball[i].velocity*dt+ball[i].force*dt**2/(2*ball[i].mass)
      dv = ball[i].force*(dt/ball[i].mass)

      ball[i].pos=ball[i].pos+dr
      ball[i].velocity=ball[i].velocity+dv    

      U[i]=ball[i].mass*ball[i].pos.y*G
      K[i]=1/2*ball[i].mass*ball[i].velocity.y**2
  
  for i in range(N):
        computer_force(i)

plt.plot(K,U, color= 'black',label='K vs U')        
 
