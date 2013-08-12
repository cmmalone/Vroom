#!/usr/bin/python
__author__ = "Katie Malone (cmmalone.158@gmail.com)"

class Obstacle:
    """ base class for obstacles (lights and cars for now """
    def __init__(self, s, road, type, name="obstacle"):
        self.s = s
        self.road = road
        self.type = type
        self.name = name
        if self.type != "terminal": #"terminal" obstacle marks the end of the road
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
        """ return obstacle immediately in front of self; returns None if obstacle is 
            frontmost obstacle on the road """
        obstacle_list = self.road.getObstacles()
        ii = 0
        while ii < len(obstacle_list):
            if obstacle_list[ii] == self: # find myself in the list 
                ### if self is the front car on the road, no obstacles to worry about, return terminal
                if ii == len(obstacle_list)-1:  
                    return self.road.terminal_obstacle
                ### else return the obstacle in front of self
                else:
                    return obstacle_list[ii+1]
            ii += 1

    def Print(self):
        """ a bunch of useful information printed to the screen """
        print self.type, self.name, " is at s ", self.s, " with nearest obstacle ", self.getNearestObstacle().getName(), " at s ", self.getNearestObstacle().getS()


class Light(Obstacle):
    """ class for lights, obstacles with vel=0 and a color status """
    def __init__(self, s, road, color, name="light"):
        Obstacle.__init__(self, s, road, "Light", name)
        self.color = color  # red or green, type(color) == string

    def getColor(self):
        return self.color

    def changeColor(self):
        if self.color == "green":
            self.color = "red"
        else:
            self.color = "green"        
    
    
class Car(Obstacle):
    """ class for cars """
    def __init__(self, s, road, vel, name="car"):
        Obstacle.__init__(self, s, road, "Car", name)
        self.vel = vel  # a car has a velocity 
        self.nearestObstacle = self.getNearestObstacle()  # cars watch out for what's in front of them

    def getVel(self):
        return self.vel
    
    def move(self, dt):
        self.s = self.s + self.vel * dt


class Terminal(Obstacle):
    """ a special obstacle type for the terminal obstacle on the road--
        useful for when calling getNearestObstacle() on the front obstacle
        on a road """
    def __init__(self, road):  #(self, road)
        Obstacle.__init__(self, -999, road, "terminal", "terminal")
