from visual import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from array import array

import random

## Constantes --------

N=1
G=9.8
dt=0.001
t=0
k=1000.18

## Generador de bolas en la caja ----

ball=range(N)

for i in range(N):
  ball[i]=sphere( pos=vector(1,4,1) , radius=0.8 , color=color.red , mass=20 , velocity=vector(-1,0,-3), force=vector(0,0,0) )


## Caja ------

larg=6.2 #es la distancia del centro de la baja a las paredes  
alt=6    #es la altura hasta la mitada de la caja 

ancho=0.5 # ancho de las paredes
lon=12.4  # largo de las paredes
  
wallR =box(pos=vector(0,0,0),size=vector(lon,ancho,lon),color=color.white)
wall  =box(pos=vector(0,2*alt,0),size=vector(lon,ancho,lon),color=color.white)

wallLR =box(pos=vector(larg,alt,0),size=vector(ancho,lon,lon),color=color.white, opacity=0.1)
wallL  =box(pos=vector(-larg,alt,0),size=vector(ancho,lon,lon),color=color.white)

wallUR  =box(pos=vector(0,alt,-larg),size=vector(12,12,ancho),color=color.white)
wallU  =box(pos=vector(0,alt,larg),size=vector(12,12,ancho),color=color.white, opacity=0.1)



## computer forces -------



def computer_force(i):
    
## for i in range(N):
##      ball[i].force.y=-ball[i].mass*G
      
 for i in range(N):
    delta=ball[i].radius-ball[i].pos.y
    if delta > 0:
       ball[i].force.y= k*delta

 for i in range(N):    
    delta=ball[i].radius+ball[i].pos.y-2*alt
    if delta > 0:
       ball[i].force.y= -k*delta

       
 for i in range(N):      
    delta=ball[i].radius+ball[i].pos.x-wallLR.pos.x
    if delta > 0:
       ball[i].force.x= -k*delta
       
 for i in range(N):   
    delta=-ball[i].radius-ball[i].pos.x+wallL.pos.x+ancho
    if delta > 0:
       ball[i].force.x= k*delta
       
 for i in range(N):      
    delta=ball[i].radius+ball[i].pos.z+wallUR.pos.z
    if delta > 0:
       ball[i].force.z= -k*delta
       
 for i in range(N):   
    delta=-ball[i].radius-ball[i].pos.z+2*wallU.pos.z+ancho
    if delta > 0:
       ball[i].force.z= k*delta
## ---------------     
nops=10
U=range(10001) ## este valor sale de hacer nobs/dt+1   
K=range(10001)
T=range(10001)
a=-1

while t < nops:
  rate(80)
  t = t + dt
  a=1+a ## para hacer funcionar la grafica, irrelevante
  
## Arranque ---------
 
  for i in range(N): 
      dr = ball[i].velocity*dt+ball[i].force*dt**2/(2*ball[i].mass)
      dv = ball[i].force*(dt/ball[i].mass)
      
      ball[i].pos=ball[i].pos+dr
      ball[i].velocity=ball[i].velocity+dv
      
##------------------- cosas para graficar la energia
      U[a]=ball[i].mass*ball[i].pos.y*G
      K[a]=ball[i].mass*ball[i].velocity.y**2/2
      T[a]=t
##-----------------  
  for i in range(N):
        computer_force(i)
  
  
  
 

from pylab import *
plot(T,K)
show() 
