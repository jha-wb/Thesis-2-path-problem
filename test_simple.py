# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:55:26 2020

@author: amit jha
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:01:41 2020

@author: amit jha
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import scipy
import random
import pandas as pd
import time
#generate sample data
start_time=time.time()
K=500
draw=3
def shortest_path(K,draw):
    #check input
    if ((K%2!=0) or (K < 0)):
        print("K must be even and positive!")
    else:
        C = [[random.random() for i in range(int(K/2+1))] for j in range(int(K/2+1))]
        
        #number of nodes 
        n=int(1/48*((K+2)*(K+4)*(2*K+6)))
        #Node co-ordinates 
        Hash=np.zeros((n,3))
        
        #first Nodes first co-ordinate
        Hash[0][:]=[0,0,0]
        j=1
        n=1
        count=0
        #Populate nodes according to the topography
        while n <=1/48*((K+4)*(K+2)*(K+6))-1:
            if count==j+1:
                j=j+1
                count=0
            i2=-j+2*count
            i1=np.linspace(i2,j,j-count+1) 
            for i in range(0,len(i1)):        
                Hash[n+i,0]=j
                Hash[n+i,1]=i1[i]
                Hash[n+i,2]=i2
            count=count+1
            n=n+len(i1)
        count=0
        j=j+1
        while n <=1/48*((K+2)*(K+4)*(2*K+6))-1:
            if count==K-j+1:
                j=j+1
                count=0
            i2=-(K-j)+2*count
            i1=np.linspace(i2,K-j,K-j-count+1)
            for i in range(0,len(i1)):        
                Hash[n+i,0]=j
                Hash[n+i,1]=i1[i]
                Hash[n+i,2] = i2          
            n=n+len(i1)
            count=count+1    
        print(Hash)    

        n=int(1/48*((K+2)*(K+4)*(2*K+6)))
        lp=0 
        j2=0
        #finding Path cost and node cost
        
        sPath=np.zeros((K,3))
        Node_val=np.matrix(np.ones((n,3)) * np.inf)
        Node_val[0,:]=[0,1,1]
        for v1 in range(0,n-1):
            j1=Hash[v1,0]+1
            if j2!=j1:
                j2=j1
                        
                if j2<=K/2:
                    lp=int(1/2*(j2*(j2+1)))+lp      
                    l1=lp+1
                    l2=int(1/2*(j2+1)*(j2+2))+lp
              
                
                else:
                    lp=int(1/2*(K-j2+2)*(K-j2+3))+lp
                    #print(lp)
                    l1=lp+1
                    l2=int(1/2*(K-j2+1)*(K-j2+2))+lp
            
            #print(l1,l2)
            
            for v2 in range((l1-1),l2):
                j=Hash[v2,0]
                #is there an edge from v1 to v2, namely
                #determine if an edge exist to j-level vertex v2
                 #from the previous(j-1)-level vertex v1
                  #at least the vertices are at the right j-levels
                    #get the j coordinate of vertex v2
                    #potentially there is an edge, but need to inevstigate further
                    #namely, check if it is
                    #too early/late to differentiate the paths OR
                    #the vertices are far apart (i-distance is at least 2)
                if (j < 2 or j > K-2 or \
                    abs(Hash[v2,1]-Hash[v2,2]) >= 2) and \
                    (abs(Hash[v2,1]-Hash[v1,1]) <=  1) and \
                    (abs(Hash[v2,2]-Hash[v1,2]) <=  1):
                    #in this case, add the edge
                    #determine its (cumulative) cost first
                    i1 = Hash[v2,1]
                    i2 = Hash[v2,2]
                    #get cost of visiting (i1,j)
                    ip = int(1/2*(j-i1))
                    jp = int(1/2*(j+i1))
                    #print(ip,jp)
                    Cijk = C[ip][jp]
                    #add cost of visiting (i2,j)
                    ip = int(1/2*(j-i2))
                    jp = int(1/2*(j+i2))
                    Cijk = Cijk+C[ip][jp]
                    #print(Cijk,Node_val[v1,0])   
                    if (Node_val[v2,0]>(Cijk+Node_val[v1,0])):           
                        Node_val[v2,:]=[Cijk+Node_val[v1,0],v1,v2]
        #print(Node_val)
        sPath[K-1,:]=Node_val[n-1,:]
        for m in range(K-2,-1,-1):
            print(m)
            sPath[m,:]=Node_val[int(sPath[m+1,1]),:]
            
        print(sPath)
        end_time=time.time()
        print(end_time - start_time)
    
shortest_path(10,3)
    
