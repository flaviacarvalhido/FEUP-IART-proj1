#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 12:11:57 2021

@author: leonorgomes
"""

class Video:
    def __init__(self, size):
        self.size = size
    
class CacheServer: 
    def __init__(self, maxCapacity):
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

class Endpoint:
    def __init__(self, latency):
        self.latency = latency
        self.dic = {}
    
    def addCacheServer(self, cacheServer, latency):
        self.dic[cacheServer] = latency

class Request:
    def __init__(self, video, endpoint):
        self.video = video
        self.endpoint = endpoint
    