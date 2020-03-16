# -*- coding: utf-8 -*-
from environment import Environment
from dijkstra import Dijkstra
from astar import Astar

if __name__ == "__main__":
    resolution = 0.1
    botRadius = 0
    env = Environment(resolution, botRadius)
    env.render()
    
    alg = Dijkstra(env)
    alg.executeAlg()
    
    env.reset()
    
    alg1 = Astar(env)
    alg1.executeAlg()