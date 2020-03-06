# -*- coding: utf-8 -*-
import sys
import time

from queue import PriorityQueue

maxVal = sys.float_info.max


class nodeInfo:
    def __init__(self,
                 _parentNodeIndex = -1,
                 _totCost = maxVal,
                 _cost2Come = maxVal,
                 _currentPos = (-1.0,-1.0,-1.0),
                 _wVel = (0.0,0.0)):
                     
        self.parentNodeIndex = _parentNodeIndex   # index in the list
        self.currentPos = _currentPos # tuple (x, y, theta) 
        self.cost2Come = _cost2Come    
        self.totCost = _totCost
        self.wVel = _wVel           # tuple (left velocity, right velocity)
                                    # to get to the current node    

class AlgorithmStub():
    def __init__(self, env):
        self.env = env
    
    def executeAlg(self):
        # executes and returns path, time taken
        startTime = time.time()
        
        endTime = time.time()
        totalTimeTaken = (endTime - startTime)
        pass
