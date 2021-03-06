from structure.Structure import *

# reads date from input file and transforms to data 
def readData(filepath):
    with open(filepath, 'r') as file:
        # 1st line
        numVideos, numEndp, numRequests, numCache, sizeCache = [int(i) for i in file.readline().split(" ")]

        # video sizes
        videoSizes = [int(i) for i in file.readline().split(" ")]
       
        #create videos
        videos=[]
        i=0
        for vid in videoSizes:
            videos.append(Video(vid,i))
            i=i+1
            
        # endpoints
        endpoints = []
        for e in range(numEndp):
            dcLatency, numCaches = [int(i) for i in file.readline().split(" ")]
            endp=Endpoint(dcLatency,e)
            

            # get all connected caches
            for num in range(numCaches):
               
                c, latency = [int(i) for i in file.readline().split(" ")]
                endp.addCacheServer(c,latency)
                
            endpoints.append(endp);

        
        # requests
        requests = []
        for r in range(numRequests):
            idVideo, idEndp, numR = [int(i) for i in file.readline().split(" ")]
            requests.append(Request(videos[idVideo], endpoints[idEndp], numR,r))
           

        data=Data(videos,numCache,sizeCache, endpoints,requests)
        return data
