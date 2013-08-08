#!/usr/bin/python

class Obstacle:
    """ base class for obstacles (lights and cars for now """
    def __init__(self, s, road, type, name="obstacle"):
        self.s = s
        self.road = road
        self.type = type
        self.name = name
        road._addObstacle(self)

    def getS(self): # position along the road
        return self.s

    def getType(self):  # currently either light or car
        return self.type

    def getRoad(self):
        return self.road

    def getName(self):
        return self.name

    def getPos(self): # (x,y) coordinates along road
        return self.road.getPos(self.s) # get position by asking road

    def getNearestObstacle(self):
        obstacle_list = self.road.getObstacles()
        ii = 0
        while ii < len(obstacle_list):
            if obstacle_list[ii] == self: # find myself in the list 
                ### if self is the front car on the road, no obstacles to worry about
                if ii == len(obstacle_list)-1:  
                    print obstacle_list[ii].getName(), " is the front obstacle in the road"
                    return None
                ### else return the obstacle in front of self
                else:
                    return obstacle_list[ii+1]
            ii += 1


class Light(Obstacle):
    """ class for lights, obstacles with vel=0 and a color status """
    def __init__(self, s, road, color, name="light"):
        Obstacle.__init__(self, s, road, "Light", name)
        self.color = color  # red or green

    def getColor(self):
        return self.color
    
class Car(Obstacle):
    def __init__(self, s, road, vel, name="car"):
        Obstacle.__init__(self, s, road, "Car", name)
        self.vel = vel  # a car has a velocity 

    def getVel(self):
        return self.vel
    
    def move(self, dt):
        self.s = self.s + self.vel * dt

    """ class for cars """
