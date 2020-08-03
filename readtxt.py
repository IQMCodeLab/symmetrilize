# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:55:55 2020

read txt
@author: 25223
"""

import tkinter as tk
from tkinter import filedialog
import struct
import math
import numpy as np


refx=np.array([[-1,0],[0,1]])

def read_txt():
    root=tk.Tk()
    root.withdraw()
    
    Filepath = filedialog.askopenfilename()
    # Filepath="D:/code/data/data/topo/200/BraggReg.txt"
    print(Filepath)
    file=open(Filepath,"r")
    data=[0,0]
    
    for i in range(2):
        s=str(file.readline())[0:-2]
        data[i]=s.split("\t")
        for j in range(2):
            data[i][j]=float(data[i][j])
        # print(s)
    # print(1)
    
    file.close()
    return data   


def unitvector(x,y):
    unit=[x/math.sqrt(x*x+y*y),y/math.sqrt(x*x+y*y)]
    return unit

def putrotation_matrix(theta):
    matrix=np.zeros((2,2))
    matrix[0][0] = math.cos(theta)
    matrix[0][1] = math.sin(theta)
    matrix[1][0] = -math.sin(theta)
    matrix[1][1] = math.cos(theta)
    return matrix
    

def getReflection_matrix(a,b):
    angle=math.atan(b/a)#ba弧度制
    rot=putrotation_matrix(angle)
    minusrot=putrotation_matrix(-angle)
    
    ans=dot2d(dot2d(rot, refx),minusrot)#？？
    return ans#ans的意义？？

def get_value_at(data,x,y):
    mean=np.mean(data)
    if x < 0 or y < 0 or x > len(data) or y > len(data[0]):
        return mean
    else:
        xx=int(x)
        yy=int(y)
        xm=xx;xp=xx;ym=yy;yp=yy
        a=x-xx;b=y-yy
        if a <= 0.5 and b <= 0.5:
            xm = xx-1; xp = xx; ym = yy-1; yp = yy
        elif a > 0.5 and b <= 0.5:
            xm = xx; xp = xx+1; ym = yy-1; yp = yy
        elif a <= 0.5 and b > 0.5:
            xm = xx-1; xp = xx; ym = yy; yp = yy+1
        elif a > 0.5 and b > 0.5:
            xm = xx; xp = xx+1; ym = yy; yp = yy+1
            
        ap = x-(xm+0.5)
        bp = y-(ym+0.5)
        
        if xm<0:
            xm = 0; xx = 0
        if ym<0:
            ym = 0; yy = 0
            
        if xp>=len(data):
            xp = len(data)-1; xx = len(data)-1
        if yp>=len(data[0]):
            yp=len(data[0])-1;yy=len(data[0])-1
            
        # if xm>=512 or ym>=512 or xp>=512 or yp>=512:
        #     print("over")
        #     print(xm,ym,x,y,xp,yp)
            
        return data[xm][ym]*(1-ap)*(1-bp) + data[xp][ym]*ap*(1-bp) + data[xm][yp]*(1-ap)*bp + data[xp][yp]*ap*bp;
            
        
    

def applyLinearTransformation(data,matrix):
    nx=len(data)
    ny=len(data[0])
    
    ox=round(nx/2)
    oy=round(ny/2)
    
    result=np.zeros((nx,ny),dtype=np.float64)
    for i in range(nx):
        for j in range(ny):
            
            x=i-ox
            y=j-oy
            
            xp=matrix[0][0]*x + matrix[1][0]*y;
            yp=matrix[0][1]*x + matrix[1][1]*y;
            
            ip=xp+nx/2
            jp=yp+nx/2
            
            result[i][j] = get_value_at(data, ip+0.5, jp+0.5)
            
    return result

def dot2d(a,b):
    ans=np.zeros((2,2))
    print(np.shape(a))
    print(np.shape(b))
    ans[0][0] = a[0][0]*b[0][0] + a[1][0]*b[0][1];
    ans[0][1] = a[0][1]*b[0][0] + a[1][1]*b[0][1];
    ans[1][0] = a[0][0]*b[1][0] + a[1][0]*b[1][1];
    ans[1][1] = a[0][1]*b[1][0] + a[1][1]*b[1][1];
    
    return ans
            
    
    
    
# getReflection_matrix(1,1)    
# read_txt()
# print(read_txt())