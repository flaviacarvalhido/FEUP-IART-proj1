#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 12:11:57 2021

@author: leonorgomes
"""

import random
import math
from copy import *

import time

# class to represent videos
class Video:
    def __init__(self, size, id):
        self.size = size
        self.id=id

    
# class to represent caches
class CacheServer: 
    def __init__(self, maxCapacity,id):
        self.id=id
        self.maxCapacity = maxCapacity
        self.videos = set()
        self.currentCapacity = 0
    
    # adds video to cache if it fits
    def addVideo(self, video):
        temp = self.currentCapacity + video.size
        if temp <= self.maxCapacity and video not in self.videos:
            self.videos.add(video)
            self.currentCapacity = temp
            return True
        return False
    
    #takes out video from cache
    def takeVideo(self, video):
        if self.checkVideo(video):
            for vid in self.videos:
                if vid.id == video.id:
                    self.videos.remove(vid)
                    return True
        return False

    # checks if video is in cache
    def checkVideo(self,video):
        return video in self.videos
    
    # checks if newVideo can replace oldVideo
    def canSwapVideos(self, oldVideo, newVideo):
        return self.currentCapacity + newVideo.size - oldVideo.size <= self.maxCapacity

#class to represent endpoints
class Endpoint:
    def __init__(self, latency,id):
        self.id=id
        self.latency = latency
        self.dic = {}
    
    #adds cache to endpoint
    def addCacheServer(self, cacheServer, latency):
        self.dic[cacheServer] = latency

    #checks if cache is in endpoint
    def checkCache(self, cache):
        return cache in self.dic

#class to represent a request
class Request:
    def __init__(self, video, endpoint,ammount, id):
        self.video = video
        self.endpoint = endpoint
        self.ammount = ammount
        self.id=id

#class to represent a possible solution
class Solution:
    def __init__(self, numCaches,size):
        self.caches=[]
        for i in range(numCaches):
            self.caches.append(CacheServer(size,i))

    def __eq__(self, x):
        return self.convertToMatrix()==x.convertToMatrix()

    def __hash__(self):
        return hash(frozenset(self.caches))

    def mutate(self):
        randC1=random.randrange(len(self.caches))
        randC2=random.randrange(len(self.caches))
        c1=copy(self.caches[randC1])
        c2=copy(self.caches[randC2])
        
        self.caches[randC1].videos=c2.videos
        self.caches[randC2].videos=c1.videos

    def perturbate(self):
        sol=copy(self)
        randC1=random.randrange(len(sol.caches))
        randC2=random.randrange(len(sol.caches))
        c1=copy(sol.caches[randC1])
        c2=copy(sol.caches[randC2])
        sol.caches[randC1].videos=c2.videos
        sol.caches[randC2].videos=c1.videos
        return sol

    # prints videos that are allocated in caches
    def printVideosinCaches(self):
        print('Cache constituiton:\n')
        for c in self.caches:
            a="Cache "+str(c.id)+": "
            for v in c.videos:
                a+=str(v.id)+", "
            print(a)

    #returns random video in a random cache
    #if cache has 0 videos, returns 0 for video
    def getRandomVideoFromCache(self):
        randCacheid=random.randrange(len(self.caches))
        randCache = self.caches[randCacheid]
        nVideos = len(randCache.videos)
        if nVideos == 0:
            return nVideos, randCache.id
        tempList = list(randCache.videos)
        randVideo = tempList[random.randrange(nVideos)]
        return randVideo, randCacheid
    
    #substitutes the old version of cache with the new one
    def subCache(self, newCache):
        for i in range(len(self.caches)):
            if self.caches[i].id == newCache.id:
                self.caches.pop(i)
                self.caches.append(newCache)
                return True
        return False
    
    #converts solution to matrix
    def convertToMatrix(self):
        matrix=[]
        for c in self.caches:
            cacheLine=[]
            for v in c.videos:
                cacheLine.append(v.id)
            matrix.append(sorted(cacheLine))
        return matrix

    # checks for empty caches in given solution
    def emptyCaches(self):
        result=0
        for c in self.caches:
            if len(c.videos) == 0:
                result+=1
        
        return (result != 0)

    # checks for requested videos that are not stored in any cache in given solution
    def notCachedVideos(self, data):
        result=0
        found=False
        for r in data.requests:
            for c in self.caches:
                if r.video in c.videos:
                    found=True
                    break
            
            if found:
                found=False
            else: result+=1

        return (result!=0)


#class to store all the information of the problem
class Data:

    def __init__(self, videos, numCaches,sizeCaches, endpoints, requests):
        self.videos=videos
        self.numCaches=numCaches
        self.sizeCaches=sizeCaches
        self.endpoints=endpoints
        self.requests=requests

    
    #creates matrix of 0's and 1's : row index:caches & col index:videos
    def convertToMatrix(self,sol):
        matrix=[]
        for c in sol.caches:
            cacheLine=[]
            for v in self.videos:
                if c.checkVideo(v):
                    cacheLine.append(1)
                else :
                     cacheLine.append(0)
            matrix.append(cacheLine)
        return matrix

    # returns a random video
    def getRandomVideo(self):
        return self.videos[random.randrange(len(self.videos))]

    
    # returns the saved time of each atended request
    def getSavedTime(self, request,sol):
        dataCenterTime=request.endpoint.latency
       
        time=dataCenterTime
    
        for cacheId in request.endpoint.dic.keys():
            cache=sol.caches[cacheId]
            if cache.checkVideo(request.video):
                tenp=request.endpoint.dic[cacheId]
                if time> tenp : 
                    time = tenp     # searches for lower streaming time for each request
            else:
                continue

        return (dataCenterTime-time)*request.ammount    # multiplies saved time by the ammount of times a video is requested

    # evaluation function
    def evaluation(self,sol):

        t0=time.perf_counter()
        t=sum([self.getSavedTime(r,sol) for r in self.requests])

        t1=time.perf_counter()
        # print(t1-t0)
        return t
    
    #aux function to calculate the size of the neighbourhood
    def neighbourhoodSize(self):
        if self.numCaches>100:
            return int(self.numCaches*0.4)
        elif self.numCaches>50:
            return int(self.numCaches)
        else:
            return int(self.numCaches*4)


    # returns a list that contains a neighbourhood of given size 
    def neighbourhood(self,sol):
        numNeighbours=self.neighbourhoodSize()
        neighbourhood=[]
        for i in range(numNeighbours):
            neighbourhood.append(neighbourFunc(self,sol))
        
        return neighbourhood

    # generates a random solution with caches full of random videos
    def generateRandomSol(self):
        sol=Solution(self.numCaches,self.sizeCaches)
        for c in sol.caches:
            nFails=0
            while(nFails<15 and c.currentCapacity<=c.maxCapacity):
                if c.addVideo(self.getRandomVideo())==False: nFails+=1
            
        return sol

    

# one of our neighbouring functions: substitutes a video in a caches by anotehr one
def subVideo(data,sol):
    count = 0
    while True:
        (randVideo, randCacheid) = sol.getRandomVideoFromCache()

        count += 1
        if count>=30:
            newSol = data.generateRandomSol()
            return newSol
        randCache=sol.caches[randCacheid]
        if randVideo == 0:
            if sol.caches[randCacheid].currentCapacity == sol.caches[randCacheid].maxCapacity:
                continue
            randVideo = data.getRandomVideo()
            if sol.caches[randCacheid].addVideo(randVideo):
                break
        else:
            otherRandVideo = data.getRandomVideo()
            if not randCache.checkVideo(otherRandVideo) and randCache.canSwapVideos(randVideo, otherRandVideo):
                randCache.takeVideo(randVideo)
                randCache.addVideo(otherRandVideo)
                break
    newSol = deepcopy(sol)
    #newSol = sol
    newSol.subCache(randCache)
    return newSol


# one of our neighbouring functions: swaps 2 videos in different caches
def swapVideos(data,sol):
    count = 0
    while True:
        (randVideo1, randCacheid1) = sol.getRandomVideoFromCache()
        (randVideo2, randCacheid2) = sol.getRandomVideoFromCache()
       
        count += 1
        if count == 30:
            newSol = data.generateRandomSol()
            return newSol
        if(randVideo1==0 or randVideo2==0): continue
        randCache1=sol.caches[randCacheid1]
        randCache2=sol.caches[randCacheid2]
      
        if randVideo1.id != randVideo2.id and randCache1.id != randCache2.id and randCache1.canSwapVideos(randVideo1, randVideo2) and randCache2.canSwapVideos(randVideo2, randVideo1):
            randCache1.takeVideo(randVideo1)
            randCache2.takeVideo(randVideo2)
            randCache1.addVideo(randVideo2)
            randCache2.addVideo(randVideo1)
            break

    newSol = deepcopy(sol)

    newSol.subCache(randCache1)
    newSol.subCache(randCache2)
    return newSol

# function that decides with neighbourhod function to use
def neighbourFunc(data,sol):
    nsol=deepcopy(sol)
    if random.randrange(2) == 0:
        return swapVideos(data,nsol)
    else: return subVideo(data,nsol)

# swaps videos from each cache
def swapCachesContent(cache1,cache2):
    vid1=(cache1.videos)
    cache1.videos=(cache2.videos)
    cache2.videos=(vid1)



