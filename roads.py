#!/usr/bin/python

def x(s):
    return float(s/2)

def y(s):
    return float(s+3)

class Road:
    """ base class for a road """
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

    ### change to take an obstacle, not an s and type
    def _addObstacle(self, obstacle):
        if self.obs_list == None:
            self.obs_list = []
        self.obs_list.append( obstacle )

    def _orderObstacles(self):
        s_list = []
        for item in self.obs_list:
            s_list.append( (float(item.getS()), item) )
        sorted(s_list)
        self.obs_list = [ii[1] for ii in sorted(s_list)]

    def getObstacles(self):
        return self.obs_list

