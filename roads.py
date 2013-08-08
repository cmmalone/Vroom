#!/usr/bin/python

def x(s):
    return float(s/2)

def y(s):
    return float(s+3)

class Road:
    def __init__(self, x_func, y_func, name="El Camino"):
        self.obs_list = None
        self.x_func = x_func
        self.y_func = y_func
        self.name = name

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
