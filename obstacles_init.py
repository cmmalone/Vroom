#!/usr/bin/python
__author__ = "Katie Malone (cmmalone.158@gmail.com)"

import obstacles
import roads_init

def initSexyBlueAudi(r):
    c = obstacles.Car(0.8, r, 4.0, "sexy blue audi") #args are (s, road, velocity)
    print "instatiated Car", c.getName(), " with s, road, velocity ", c.getS(), c.getRoad().getName(), c.getVel()
    return c
   
def initStang(r):
    c = obstacles.Car(5., r, 2.0, "'stang")
    print "instatiated Car", c.getName(), " with s, road, velocity ", c.getS(), c.getRoad().getName(), c.getVel()
    return c
     


