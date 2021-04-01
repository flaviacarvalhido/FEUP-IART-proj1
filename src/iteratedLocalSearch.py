from structure.Structure import *
from parserfunc import *
from copy import *
import random



def ils(numIters,ILSiters,alpha,beta):
    data=readData('../src/input/small.in')
    lPareto=[]
    i=1
    while i<=numIters:
        x=Solution(data.numCaches,data.sizeCaches)
        k=i
        






ils(10,5,0,0.1)