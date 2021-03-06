# -*- coding: utf-8 -*-

import math
import numpy as np
import cv2

from obstacleSpace import isInObstacleWs

class Environment:
    def __init__(self, resolution, botRadius):
        self.res = resolution
        self.totalClearance = botRadius
        self.startPt = [0.0, 0.0]
        self.goalPt = [8.0,4.5]
        self.MAP_X, self.MAP_Y = 11.1, 10.1
        self.GRID_NX, self.GRID_NY = int(self.MAP_X/self.res), int(self.MAP_Y/self.res)
        self.obstacleSet = self.getObstacleSet()
        
        self.obstacleMap = self.getObstacleMap()
        
        self.runningMap = np.copy(self.obstacleMap)
        self.renderCounter = 0
        
    def getObstacleSet(self):
        outputSet = set([])
        # create the set using for loops
        for p in range(0,int(self.MAP_X/self.res+1)):
            for q in range(0,int(self.MAP_Y/self.res+1)):
                if (isInObstacleWs((p+0.5)*self.res,(q+0.5)*self.res, self.totalClearance)):
                    outputSet.add((p,q))
        return outputSet
    
    def isPtInObs(self, x, y):
        temp = self.getGridPt([x,y])
        return temp in self.obstacleSet
    
    def isGridPtInObs(self, pt):
        return pt in self.obstacleSet
    
    def getGridPt(self,pt):
        return (math.floor(pt[0]/self.res), math.floor(pt[1]/self.res))
    
    def updateMap(self,display,pt,val):
        # For Display
        # set up color map for display
        # 0 - empty, white
        # 1 - startPt, red
        # 2 - goalPt, green
        # 3 - visited, yellow
        # 4 - obstacle, black
        # 5 - path, blue
        red =0
        green =0
        blue =0
        if val ==0:
            red,green,blue = 255,255,255
        elif val == 1:
            red,green,blue = 255,0,0
        elif val == 2:
            red,green,blue = 0,255,0
        elif val == 3:
            red,green,blue = 255,255,0
        elif val == 4:
            red,green,blue = 0,0,0
        elif val == 5:
            red,green,blue = 0,0,255
        else:
            # to catch errors
            red,green,blue = 255,0,255
        display[pt[0],pt[1],0] = blue
        display[pt[0],pt[1],1] = green
        display[pt[0],pt[1],2] = red
        return display
    
    def getObstacleMap(self):
        # fill a np array image with obstacles for rendering
        obsMap = 255 * np.ones((self.GRID_NX+1,self.GRID_NY+1,3))
        
        for obs in self.obstacleSet:
            obsMap = self.updateMap(obsMap, obs, 4)
        return obsMap
    
    def render(self):
        self.runningMap = self.updateMap(self.runningMap,self.getGridPt(self.startPt),1)
        self.runningMap = self.updateMap(self.runningMap,self.getGridPt(self.goalPt),2)
        if self.renderCounter%60 == 0:
            toDisplay = cv2.resize(self.runningMap,(self.GRID_NY * 1000 // self.GRID_NX,1000), interpolation = cv2.INTER_AREA)
            cv2.imshow("",np.rot90(toDisplay,1))
            cv2.waitKey(1)
        self.renderCounter+=1
        
    def setVisitedAndRender(self, pt):
        self.runningMap = self.updateMap(self.runningMap,pt,3)
        self.runningMap = self.updateMap(self.runningMap,self.getGridPt(self.goalPt),2)
        if self.renderCounter%60 == 0:
            toDisplay = cv2.resize(self.runningMap,(self.GRID_NY * 1000 // self.GRID_NX,1000), interpolation = cv2.INTER_AREA)
            cv2.imshow("",np.rot90(toDisplay,1))
            cv2.waitKey(1)
        self.renderCounter+=1
        
    def setPathAndRender(self, pt):
        self.runningMap = self.updateMap(self.runningMap,pt,5)
        self.runningMap = self.updateMap(self.runningMap,self.getGridPt(self.startPt),1)
        self.runningMap = self.updateMap(self.runningMap,self.getGridPt(self.goalPt),2)
        if self.renderCounter%2 == 0:
            toDisplay = cv2.resize(self.runningMap,(self.GRID_NY * 1000 // self.GRID_NX,1000), interpolation = cv2.INTER_AREA)
            cv2.imshow("",np.rot90(toDisplay,1))
            cv2.waitKey(1)
        self.renderCounter+=1
    
    def reset(self):
        # reset image to obstacle
        self.runningMap = np.copy(self.obstacleMap)
        self.renderCounter = 0
        pass