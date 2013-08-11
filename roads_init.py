#!/usr/bin/python
__author__ = "Katie Malone (cmmalone.158@gmail.com)"

import roads

def initElCamino():
    def x(s):
        return float(s/2)
    def y(s):
        return float(s+3)
    r = roads.Road(x,y)
    return r

def initUniversityAve():
    def x(s):
        return float(2)
    def y(s):
        return float(2*s+1)
    r = roads.Road(x,y,"University Ave")
    return r
