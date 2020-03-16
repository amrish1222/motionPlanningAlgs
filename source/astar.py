# -*- coding: utf-8 -*-
import sys
import time

from queue import PriorityQueue

maxVal = sys.float_info.max
root2 = round(2**0.5,4)

class nodeInfo:
    def __init__(self,
                 _parentNodeIndex = -1,
                 _cost2Come = maxVal,
                 _cost2Go = maxVal,
                 _currentPos = (-1.0,-1.0,-1.0)):
                     
        self.parentNodeIndex = _parentNodeIndex   # index in the list
        self.currentPos = _currentPos # tuple (x, y) 
        self.cost2Come = _cost2Come    
        self.cost2Go = _cost2Go
        
    def totalCost(self):
        return self.cost2Come + self.cost2Go

class Astar():
    def __init__(self, env):
        self.env = env
        self.gridGoalPt = self.env.getGridPt(self.env.goalPt)
        self.gridStartPt = self.env.getGridPt(self.env.startPt)
    
    def executeAlg(self):
        # executes and returns path, time taken
        startTime = time.time()
        
        q = PriorityQueue()
        isGoalVisited = False
        visitedSet = set([])
        nodeInfoList = []
        pos2NodeIndex = dict()
        finalPath = []
        
        tempParentNode = -1
        tempCost2Come = self.cost2Come(self.gridStartPt, self.gridGoalPt)
        tempCost2Go = self.cost2Go(self.gridStartPt, self.gridGoalPt)
        tempCurPos = self.gridStartPt
        
        tempNodeInfo = nodeInfo(tempParentNode, tempCost2Come, tempCost2Go, tempCurPos)
        nodeInfoList.append(tempNodeInfo)
        
        parentIndex = 0
        currentIndex = 0
        
        # add the first point to the queue
        q.put([nodeInfoList[parentIndex].totalCost(),parentIndex])
        visitedSet.add(self.env.getGridPt(tempCurPos))
        pos2NodeIndex[tempCurPos] = parentIndex
        
        while not q.empty():
            tempGetQ = q.get()
            
            parentIndex = tempGetQ[1]
            parentPos = nodeInfoList[parentIndex].currentPos
            parentCost2Come = nodeInfoList[parentIndex].cost2Come
            
            if self.hasReachedGoal(parentPos):
                isGoalVisited = True
                goalNode = parentIndex
                break
            
            nextNodes = self.getNextNodesAndCost(parentPos)
            
            for node in nextNodes:
                if not node[0] in visitedSet:
                    if not self.env.isGridPtInObs(node[0]):
                        tempParentNode = parentIndex
                        tempCost2Come = parentCost2Come + node[1]
                        tempCurPos = node[0]
                        tempCost2Go = self.cost2Go(tempCurPos, self.gridGoalPt)
                        
                        tempNodeInfo = nodeInfo(tempParentNode, tempCost2Come, tempCost2Go, tempCurPos)
                        nodeInfoList.append(tempNodeInfo)
                        
                        currentIndex += 1
                        
                        q.put([round(nodeInfoList[currentIndex].totalCost(),4),currentIndex])
                        
                        visitedSet.add(node[0])
                        pos2NodeIndex[node[0]] = currentIndex
                        
                        self.env.setVisitedAndRender(node[0])
                else:
                    if not self.env.isGridPtInObs(node[0]):
                        tempCost2Come =  parentCost2Come + node[1]
                        tempCurPos = node[0]
                        indexOfPos = pos2NodeIndex.get(tempCurPos)
                        tempCost2Go = self.cost2Go(tempCurPos, self.gridGoalPt)
                        tempTotalCost = tempCost2Come + tempCost2Go
                        
                        if tempTotalCost < nodeInfoList[indexOfPos].totalCost():
                            tempParentNode = parentIndex
                            tempCurPos = node[0]
                            
                            tempNodeInfo = nodeInfo(tempParentNode, tempCost2Come, tempCost2Go, tempCurPos)
                            nodeInfoList[indexOfPos]=tempNodeInfo
                            q.put([round(nodeInfoList[indexOfPos].totalCost(),4),indexOfPos])
        
        if isGoalVisited:
            print("Path Found")
            nextParentNode = goalNode
            finalPath.append(self.gridGoalPt)
            while (nextParentNode != -1):
                nextParentNI = nodeInfoList[nextParentNode]
                nextParentNode = nextParentNI.parentNodeIndex
                self.env.setPathAndRender(nextParentNI.currentPos)
                finalPath.append(nextParentNI.currentPos)
        else:
            print("No Path available")
        
        endTime = time.time()
        totalTimeTaken = (endTime - startTime)
        
        return finalPath, totalTimeTaken
    
    def cost2Come(self, pt1, pt2):
        fromPtx, fromPty = pt1
        toPtx, toPty = pt2
        # calculate L2 distance
        cost = ((toPtx-fromPtx)**2 + (toPty-fromPty)**2)**0.5
        return cost
    
    def cost2Go(self, pt1, pt2):
        fromPtx, fromPty = pt1
        toPtx, toPty = pt2
        # calculate L2 distance
        cost = ((toPtx-fromPtx)**2 + (toPty-fromPty)**2)**0.5
        return cost
    
    def hasReachedGoal(self, gridPt):        
        return gridPt == self.gridGoalPt
    
    def getNextNodesAndCost(self, pt):
        xc,yc = pt
        nearbyList = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if xc+i>=0 and yc+j >=0 and xc+i<=self.env.GRID_NX and yc+j<=self.env.GRID_NY:
                    if abs(i*j) == 1:
                        temp = [(xc+i,yc+j),root2]
                        nearbyList.append(temp)
                    elif not(i == 0 and j == 0):
                        temp =[(xc+i,yc+j),1]
                        nearbyList.append(temp)
        return nearbyList
        