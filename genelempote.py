#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: grupogedes

"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt
from scipy.interpolate import CubicSpline
from scipy.interpolate import griddata
import matplotlib.mlab as mlab

#10,17,24,31

N = 12500 #number of points for plotting/interpolation



name='PROBLEMA_1_movie_17.tec'
x, y, p, u, v = np.genfromtxt('archivos/'+name, unpack=True)
levmin=0.101 #define el valor minimo del contorno
numcont=8 #define la cantidad de contornos que desea graficar
levels=np.linspace(levmin, np.max(p), numcont)
tamt=np.size(x)
nn=int(mt.sqrt(tamt))
print levels
xi3 = np.linspace(x.min(), x.max(), N)
yi3 = np.linspace(y.min(), y.max(), N)
zi3 = griddata((x, y), p, (xi3[None,:], yi3[:,None]), method='linear')
print zi3
#

plt.close('all')
fig = plt.figure()

####dibuja la grilla y los puntos de la malla 
for i in range(nn):
	X=x[i*nn:i*nn+nn];
	Y=y[i*nn:i*nn+nn];
	cs=CubicSpline(Y,X)
	ys=np.arange(Y.min(),Y.max(),0.0001)
	plt.plot(cs(ys),ys,'k',lw=0.1)
	

for k in range(nn):
	Yh=list()
	Xh=list()
	for i in range(nn):
		Xh.append(x[i*nn+k])
		Yh.append(y[i*nn+k])
	cs=CubicSpline(Xh,Yh)
	xs=np.arange(np.min(Xh),np.max(Xh),0.0001)
	plt.plot(xs,cs(xs),'k',lw=0.1)
	del Yh
	del Xh

#plt.scatter(x,y,p,lw=20,c='r')
CS = plt.contour(xi3, yi3, zi3,levels, colors='k',)
plt.clabel(CS, inline=1, fontsize=8)


plt.title(name.split('.')[0])
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig('imagenes/'+name.split('.')[0]+'.svg');
plt.show()
plt.close('all')
