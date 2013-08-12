#!/usr/bin/python
__author__ = "Katie Malone (cmmalone.158@gmail.com)"

import obstacles

class Road:
    def __init__(self, x_func, y_func, name="El Camino"):
        self.obs_list = None
        self.x_func = x_func
        self.y_func = y_func
        self.name = name
        self.terminal_obstacle = obstacles.Terminal(self)

    def getXFunc(self):
        return self.x_func
       
    def getYFunc(self):
        return self.y_func

    def getPos(self, s):
        x = self.x_func(s)
        y = self.y_func(s)
        return x, y 

    def getName(self):
        return self.name

    def getObstacles(self):
        return self.obs_list

    def moveAll(self, dt):
        """ moves all the obstacles on the road (except lights), then reorders by S """
        for obstacle in self.getObstacles():
            if obstacle.getType() != "Light": #traffic lights don't move
                obstacle.move(dt)
        self._orderObstacles()
        for obstacle in self.getObstacles(): # have all cars re-find their nearest obstacles
            if obstacle.getType() != "Light":
                obstacle.nearestObstacle = obstacle.getNearestObstacle() 

    def _addObstacle(self, obstacle):
        """ when you instantiate a car or light, you correspondingly
            add an obstacle to the road """
        if self.obs_list == None:
            self.obs_list = []
        self.obs_list.append( obstacle )

    def _orderObstacles(self):
        """ order the obstacles in the road by increasing S """
        s_list = []
        for item in self.obs_list:
            s_list.append( (float(item.getS()), item) )
        self.obs_list = [ii[1] for ii in sorted(s_list)]


    """ base class for a road """
