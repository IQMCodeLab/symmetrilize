# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:18:19 2020

WRITEBIN

@author: 25223
"""

import tkinter as tk
from tkinter import filedialog
import struct
import numpy as np

def write_bin(field,nx,ny,current,bias,x,y,filename):
    binfile=open(str(filename)+".bin","wb")
    data=struct.pack(">i",nx)
    binfile.write(data)
    data=struct.pack(">i",ny)
    binfile.write(data)  
    data=struct.pack(">d",bias)
    binfile.write(data)
    data=struct.pack(">d",current)
    binfile.write(data)
    
    for i in range(len(x)):
        data=struct.pack(">d",x[i])
        binfile.write(data)
    for i in range(len(y)):
        data=struct.pack(">d",y[i])
        binfile.write(data)
        
    for i in range(nx):
        for j in range(ny):
            data=struct.pack(">d",field[i][j])
            binfile.write(data)
    binfile.close()
    