print "you're now testing via a script"

import roads
import obstacles
import time_stepper

x = roads.x
y = roads.y
print

r = roads.Road(x,y)
print "instantiated Road ", r.getName(), " with current obstacles ", r.getObstacles()
print

c = obstacles.Car(0.8, r, 1.0, "sexy blue audi") #args are (s, road, velocity)
print "instatiated Car", c.getName(), " with s, road, velocity ", c.getS(), c.getRoad().getName(), c.getVel()
print "c's position is ", c.getPos()
print "now road ", c.getRoad().getName(), " has an obstacle list of ", c.getRoad().getObstacles()
print

c2 = obstacles.Car(1., r, 0.5, "'stang")
print "instatiated Car", c2.getName(), " with s, road, velocity ", c2.getS(), c2.getRoad().getName(), c2.getVel()
print "now road ", c.getRoad().getName(), " has an obstacle list of ", c.getRoad().getObstacles()
print

l = obstacles.Light(0.5, r, "green", "traffic light") #args are (s, road, color)
print "instantiated light", l.getName(), " with s, road, color ", l.getS(), l.getRoad().getName(), l.getColor()

dt = time_stepper.TimeStepper()
#print "dt ",dt.getDt()
for ii in range(0, 10):
    c.move( float(dt.getDt()) )
    c2.move( float(dt.getDt()) )
    r._orderObstacles()
    c.getNearestObstacle()
#    print c2.getS()
#    print "now road ", c.getRoad().getName(), " has an obstacle list of ", c.getRoad().getObstacles()
#    for obstacle in c.getRoad().getObstacles():
#        print "   ", obstacle.getName(), obstacle.getS()

