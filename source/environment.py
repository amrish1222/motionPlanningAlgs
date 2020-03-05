# -*- coding: utf-8 -*-

import math

from obstacleSpace import isInObstacleWs

class Environment:
    def __init__(self, resolution, botRadius):
        self.res = resolution
        self.totalClearance = botRadius
        self.MAP_X, self.MAP_Y = 11.1, 10.1
        self.GRID_NX, self.GRID_NY = int(self.MAP_X/self.res), int(self.MAP_Y/self.res)
        self.obstacleSet = self.getObstacleSet()
        
        self.obstacleMap = self.getObstacleMap()
        
    def getObstacleSet(self):
        outputSet = set([])
        # create the set using for loops
        for p in range(0,int(self.MAP_X/self.res+1)):
            for q in range(0,int(self.MAP_Y/self.res+1)):
                if (isInObstacleWs(p*self.res,q*self.res, self.totalClearance)):
                    outputSet.add((p,q))
        return outputSet
    
    def isPtInObs(self, x, y):
        temp = (math.ceil(x/self.res), math.ceil(y/self.res))
        return temp in self.obstacleSet
    
    def getObstacleMap(self):
        # fill a np array image with obstacles for rendering
        pass
    
    def render(self):
        pass
    
    def reset(self):
        # reset image to obstacle
        pass