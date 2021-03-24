#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 12:11:57 2021

@author: leonorgomes
"""


class Video:
    def __init__(self, size, id):
        self.size = size
        self.id=id

    def getStreamingTime(self, latency):
        return self.time/latency



class CacheServer: 
    def __init__(self, maxCapacity,id):
        self.id=id
        self.maxCapacity = maxCapacity
        self.videos = []
        self.currentCapacity = 0
    
    def addVideo(self, video):
        temp = self.currentCapacity + video.size
        if temp <= self.maxCapacity:
            self.videos.append(video)
            self.currentCapacity = temp
            return True
        return False

    def checkVideo(self,video):
        return video in videos


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

    def __init__(self, videos, caches, endpoints, requests):
        self.videos=videos
        self.caches=caches
        self.endpoints=endpoints
        self.requests=requests
        

    def getSavedTime(self, request):
        dataCenterTime=request.endpoint.latency
        time=request.video.getStreamingTime(dataCenterTime)
        for cache in caches:
            if cache.checkVideo(request.video) and request.endpoint.checkCache(cache) and time > request.video.getStreamingTime(request.endpoint.dic[cache]):
                time = request.video.getStreamingTime(request.endpoint.dic[cache])      # searches for lower streaming time for each request
            else:
                continue
        return (request.video.getStreamingTime(dataCenterTime)-time)*request.ammount    # multiplies saved time by the ammount of times a video is requested


    def evaluation(self):
        time=0
        for r in self.requests:
           time+= getSavedTime(r)
        return time

    


    def generateRandomSol(self):
        numVids=len(self.videos)
        numCaches=len(self.caches)
        