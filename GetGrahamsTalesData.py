# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:22:03 2019

@author: Satya
"""
import urllib.request
import os 

def download():
    datadir=os.getcwd()+"/data/";
    serverurl="https://www.cs.cmu.edu/~spok/grimmtmp/"
    for i in range(1,220):
        if i<10:
            filename="00"+str(i)+".txt"
        elif i>=10 and i<100:
            filename="0"+str(i)+".txt"
        elif i>=100:
            filename=str(i)+".txt";
        clientfile=datadir+filename
        serverfile=serverurl+filename
        urllib.request.urlretrieve(serverfile, clientfile)

download()