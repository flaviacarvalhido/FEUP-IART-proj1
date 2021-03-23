#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 10:32:31 2021

@author: leonorgomes
"""

class Edge: 
    def __init__(self, origin, dest, cost):
        self.origin = origin
        self.dest = dest
        self.cost = cost
        
class Node:
    def __init__(self, state):
        self.state = state
        self.edges = []
        self.parent = None
        self.depth = 0
    
    def setParent(self, parentNode):
        self.parent = parentNode
    
    def setDepth(self, depth):
        self.depth = depth
    
    def addEdge(self, destiny, cost):
        self.edges.append(Edge(self, destiny, cost))
        destiny.setParent(self)
        destiny.setDepth(self.depth + 1)
    
    def getChildren(self):
        children = []
        for e in self.edges:
            children.append(e)
        return children

class Tree:
    def __init__(self, rootNode):
        self.root = rootNode
        self.nodes = []
    
    def addNode(self, parentNode, childNode, cost):
        parentNode.addEdge(childNode, cost)
        self.nodes.append(childNode)
        