# -*- coding: utf-8 -*-
from environment import Environment
from dijkstra import Dijkstra

if __name__ == "__main__":
    resolution = 0.1
    botRadius = 0
    env = Environment(resolution, botRadius)
    env.render()
    
    alg = Dijkstra(env)
    alg.executeAlg()