# -*- coding: utf-8 -*-

import numpy as np

def isInObstacleWs(x,y, totClearance):
    boo = False;
    boo = boo or isInRect(x,y, 4.74, 0.35, 7.48, 1.87, totClearance)#3
    boo = boo or isInRect(x,y, 5.29, 2.65, 7.12, 3.41, totClearance)#4
    boo = boo or isInRect(x,y, 4.38, 3.15, 5.29, 4.98, totClearance)#2
    boo = boo or isInRect(x,y, 1.4995, 7.501, 3.0985, 9.1, totClearance)#1
    boo = boo or isInRect(x,y, 6.85, 0, 11.1, 0.35, totClearance)#5
    boo = boo or isInRect(x,y, 7.79, 0.35, 8.96, 0.93, totClearance)#7
    boo = boo or isInRect(x,y, 9.27, 0.35, 11.1, 1.11, totClearance)#10
    boo = boo or isInRect(x,y, 10.52, 1.7825, 11.1, 2.9525, totClearance)#14
    boo = boo or isInRect(x,y, 7.845, 2.67, 9.365, 3.84, totClearance)#8
    boo = boo or isInRect(x,y, 10.19, 3.625, 11.1, 4.485, totClearance)#12
    boo = boo or isInRect(x,y, 10.52, 4.485, 11.1, 5.625, totClearance)#13
    boo = boo or isInRect(x,y, 7.44, 6.21, 11.1, 6.97, totClearance) #6
    boo = boo or isInRect(x,y, 8.32, 8.27, 9.18, 10.1, totClearance)#9
    boo = boo or isInRect(x,y, 9.83, 9.19, 10.26, 10.1, totClearance)#11
    
    boo = boo or isInCircle(x,y, 3.9, 0.45, 0.8100, totClearance)
    boo = boo or isInCircle(x,y, 4.38, 2.74, 0.8100, totClearance)
    boo = boo or isInCircle(x,y, 4.38, 7.36, 0.8100, totClearance)
    boo = boo or isInCircle(x,y, 3.9, 9.55, 0.8100, totClearance)
    boo = boo or isInCircle(x,y, 1.4995, 8.3005, 1.5990, totClearance)
    boo = boo or isInCircle(x,y, 3.0985, 8.3005, 1.5990, totClearance)
    
    boo = boo or isOutRect(x,y, 0.0, 0.0, 11.1, 10.1, totClearance)
    return boo

def isInRect(x,y, LLx, LLy, URx, URy, totClearance):
    boo = True;
    boo = boo and x<=URx + totClearance
    boo = boo and y<=URy + totClearance
    boo = boo and x>=LLx - totClearance
    boo = boo and y>=LLy - totClearance
    return boo

def isInCircle(x,y,cx,cy,D,totClearance):
    boo = True
    boo = boo and (D/2 + totClearance) >= np.linalg.norm(np.array([[cx-x],[cy-y]]))
    return boo
    
def isOutRect(x,y, LLx, LLy, URx, URy, totClearance):
    boo = False;
    boo = boo or x>=URx - totClearance
    boo = boo or y>=URy - totClearance
    boo = boo or x<=LLx + totClearance
    boo = boo or y<=LLy + totClearance
    return boo