from vpython import *
import math

N=10
ball=[]
for i in range(N):
  ball[i]=sphere(pos=vec(0,i+2,0),radius=0.2,color=color.magenta,mass=0,velocity=vec(i+10,((-i)*(-i))+5,7+i))

wallR =box(pos=vec(0,-0.8,0),size=vector(12,0.5,12),color=color.green)
wall  =box(pos=vec(0,10.8,0),size=vector(12,0.5,12),color=color.green)

wallLR =box(pos=vec(5+1,5,0),size=vector(0.5,12,12),color=color.green)
wallL  =box(pos=vec(-5-1,5,0),size=vector(0.5,12,12),color=color.green)


wallUR  =box(pos=vec(0,5,-6),size=vector(12,12,0.5),color=color.green)
wallU  =box(pos=vec(0,5,6),size=vector(12,12,0.5),color=color.green,opacity=0.1)

dT=0.01
T=0
for i in range(N):
  ball[i].pos=ball[i].pos+ball[i].velocity*dT

while T < 30:
  rate(80)
  print(ball[0].mass)
  for i in range(N):  
    #print(ball.pos," ",T)
    
    if ball[i].pos.y < wallR.pos.y+1:
        ball[i].velocity.y=-ball[i].velocity.y
    
    if ball[i].pos.y > wall.pos.y-1:
       ball[i].velocity.y=-ball[i].velocity.y
       
    if ball[i].pos.x > wallLR.pos.x-1:
       ball[i].velocity.x=-ball[i].velocity.x
    
    if ball[i].pos.x < wallL.pos.x+1:
       ball[i].velocity.x=-ball[i].velocity.x
    
    if ball[i].pos.z < wallU.pos.z-1:
       ball[i].velocity.z=-ball[i].velocity.z
    
    if ball[i].pos.z > wallUR.pos.z+1:
       ball[i].velocity.z=-ball[i].velocity.z
       
    ball[i].pos = ball[i].pos + ball[i].velocity*dT 
    T = T + dT

