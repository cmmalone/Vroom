#!/usr/bin/python
__author__ = "Katie Malone (cmmalone.158@gmail.com)"

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import roads
import roads_init
import obstacles
import obstacles_init
import time_stepper

print "you're now testing via a script"

r = roads_init.initElCamino()
print "instantiated Road ", r.getName(), " with current obstacles ", r.getObstacles()
print

ua = roads_init.initUniversityAve()
print "instantiated Road ", ua.getName(), " with current obstacles ", ua.getObstacles()
print

c = obstacles_init.initSexyBlueAudi(r)
c.Print()

print

c2 = obstacles_init.initStang(r)

l = obstacles.Light(0.5, r, "green", "traffic light") #args are (s, road, color)
print "instantiated light", l.getName(), " with s, road, color ", l.getS(), l.getRoad().getName(), l.getColor()

fig = plt.figure() 
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 10), ylim=(0, 10))
ax.grid()
cars, = ax.plot([], [], 'o')

dt = time_stepper.TimeStepper()
interval = dt.getDt()

for ii in range(0, 10):
    r.moveAll( dt.getDt() )
    n_o = c.getNearestObstacle()  # find the obstacle immediately in front of car c (sexy blue audi)
    if n_o != None:  # the frontmost obstacle has no nearest obstacle--return None in this case
#        print c.getNearestObstacle().getName(), " is the obstacle in front of ", c.getName()
        c.Print()
        c2.Print()
        print c.getPos()

def animate(i):
    global interval, ax, fig
    r.moveAll( dt.getDt() )
    cpos = c.getPos()
    c2pos = c2.getPos()
    print cpos, c2pos
    cars.set_data([cpos[0], c2pos[0]], [c2pos[1],c2pos[1]])
    return cars

ani = animation.FuncAnimation(fig, animate, 100) 
plt.show()
