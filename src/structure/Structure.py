#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 12:11:57 2021

@author: leonorgomes
"""

import random
import math
from copy import *

class Video:
    def __init__(self, size, id):
        self.size = size
        self.id=id

    

class CacheServer: 
    def __init__(self, maxCapacity,id):
        self.id=id
        self.maxCapacity = maxCapacity
        self.videos = []
        self.currentCapacity = 0
    
    def addVideo(self, video):
        temp = self.currentCapacity + video.size
        if temp <= self.maxCapacity and video not in self.videos:
            self.videos.append(video)
            self.currentCapacity = temp
            return True
        return False
    
    def takeVideo(self, video):
        if self.checkVideo(video):
            for i in range(len(self.videos)):
                if self.videos[i].id == video.id:
                    self.videos.pop(i)
                    return True
        return False


    
    def checkVideo(self,video):
        return video in self.videos
    
    def canSwapVideos(self, oldVideo, newVideo):
        return self.currentCapacity + newVideo.size - oldVideo.size <= self.maxCapacity

   


class Endpoint:
    def __init__(self, latency,id):
        self.id=id
        self.latency = latency
        self.dic = {}
    
    def addCacheServer(self, cacheServer, latency):
        self.dic[cacheServer] = latency

    def checkCache(self, cache):
        return cache in self.dic

    


class Request:
    def __init__(self, video, endpoint,ammount, id):
        self.video = video
        self.endpoint = endpoint
        self.ammount = ammount
        self.id=id


class Solution:
    def __init__(self, numCaches,size):
        self.caches=[]
        for i in range(numCaches):
            self.caches.append(CacheServer(size,i))

    
    def mutate(self):
        randC1=random.randrange(len(self.caches))
        randC2=random.randrange(len(self.caches))
        c1=self.caches[randC1]
        c2=self.caches[randC2]
        self.caches[randC1].videos=c2.videos
        self.caches[randC2].videos=c1.videos

    def printVideosinCaches(self):
    #print(self)
        for c in self.caches:
            a="Cache "+str(c.id)+": "
            for v in c.videos:
                a+=str(v.id)+", "
            print(a)

class Data:

    def __init__(self, videos, numCaches,sizeCaches, endpoints, requests):
        self.videos=videos
        self.numCaches=numCaches
        self.sizeCaches=sizeCaches
        self.endpoints=endpoints
        self.requests=requests

    

    #returns random video in a random cache
    #if cache has 0 videos, returns 0 for video
    def getRandomVideoFromCache(self):
        nCaches = len(self.caches)
        randCache = self.caches[random.randrange(nCaches)]
        nVideos = len(randCache.videos)
        if nVideos == 0:
            return nVideos, randCache
        randVideo = randCache.videos[random.randrange(nVideos)]
        return randVideo, randCache

    def getRandomVideo(self):
        return self.videos[random.randrange(len(self.videos))]

    def subCache(self, newCache):
        for i in range(len(self.caches)):
            if self.caches[i].id == newCache.id:
                self.caches.pop(i)
                self.caches.append(newCache)
                return True
        return False

    def getSavedTime(self, request,sol):
        dataCenterTime=request.endpoint.latency
       
        time=dataCenterTime
        
        for cache in sol.caches:
            if cache.checkVideo(request.video) and request.endpoint.checkCache(cache.id):
                if time> request.endpoint.dic[cache.id] : 
                    time = request.endpoint.dic[cache.id]     # searches for lower streaming time for each request
            else:
                continue
        return (dataCenterTime-time)*request.ammount    # multiplies saved time by the ammount of times a video is requested


    def evaluation(self,sol):
        time=0
        for r in self.requests:
            time+= self.getSavedTime(r,sol)
        #print('inside eval', time)
        return time


    #generates a random solution with caches full of random videos
    def generateRandomSol(self):
        sol=Solution(self.numCaches,self.sizeCaches)
        for c in sol.caches:
            nFails=0
            while(nFails<15 and c.currentCapacity<=c.maxCapacity):
                if c.addVideo(self.getRandomVideo())==False: nFails+=1
            
        return sol

    #TODO not needed anymore
    def mutate(self):
        randC1=random.randrange(len(self.caches))
        randC2=random.randrange(len(self.caches))
        c1=(self.caches[randC1])
        c2=(self.caches[randC2])
        self.caches[randC1].videos=(c2.videos)
        self.caches[randC2].videos=(c1.videos)

    #TODO not needed anymore
    def printVideosinCaches(self):
        #print(self)
        for c in self.caches:
            a="Cache "+str(c.id)+": "
            for v in c.videos:
                a+=str(v.id)+", "
            print(a)




  
def subVideo(sol):
    (randVideo, randCache) = sol.getRandomVideoFromCache()
    if randVideo == 0:
        while True:
            randVideo = sol.getRandomVideo()
            if randCache.addVideo(randVideo):
                break
    else:
        while True:
            otherRandVideo = sol.getRandomVideo()
            if not randCache.checkVideo(otherRandVideo) and randCache.canSwapVideos(randVideo, otherRandVideo):
                randCache.takeVideo(randVideo)
                randCache.addVideo(otherRandVideo)
                break
    newSol = sol
    newSol.subCache(randCache)
    return newSol

def swapVideos(sol):
    while True:
        (randVideo1, randCache1) = sol.getRandomVideoFromCache()
        (randVideo2, randCache2) = sol.getRandomVideoFromCache()
        if randVideo1.id != randVideo2.id and randCache1.id != randCache2.id and randCache1.canSwapVideos(randVideo1, randVideo2) and randCache2.canSwapVIdeos(randVideo2, randVideo1):
            randCache1.takeVideo(randVideo1)
            randCache2.takeVideo(randVideo2)
            randCache1.addVideo(randVideo2)
            randCache2.addVideo(randVideo1)
            break
    newSol = sol
    newSol.subCache(randCache1)
    newSol.subCache(randCache2)
    return newSol

def neighbourFunc(sol):
    if random.randrange(2):
        return swapVideos(sol)
    else: return subVideo(sol)




