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

res=500 #resolucion de la malla
L=list()
name='movie_11.tec'
archivo=open('infotec/'+name,'r')

for lines in archivo.readlines():
	L.append(lines)

tama=len(L)
elem=list()
for i in range(tama):
	if 'ZONE' in L[i]:
		elem.append(i+1)	

numele=len(elem) #numero de elementos
if numele>1:
	tamxele=elem[1]-1-elem[0] #numero de nodos por elemento
else:
	tamxele=tama-elem[0]
nn=int(mt.sqrt(tamxele)) #numero de puntos por col
X=list();
Y=list();

for i in range(numele): #organizar en columnas cada elemento
	x=list();
	y=list();
	for j in range(tamxele):	
		x.append(float(L[elem[i]+j].split()[0]))
		y.append(float(L[elem[i]+j].split()[1]))
	X.append(x)
	Y.append(y)
	del x
	del y

for i in range(numele): #graficar malla
    for j in range(nn):
        x=X[i][j*nn:j*nn+nn]
        y=Y[i][j*nn:j*nn+nn]
        cs=CubicSpline(y,x)
        ys=np.linspace(np.min(y),np.max(y),res)
        plt.plot(cs(ys),ys,'k',lw=0.1)
        
    for j in range(nn):
        Yh=list()
        Xh=list()
        for k in range(nn):
            Xh.append(X[i][k*nn+j])
            Yh.append(Y[i][k*nn+j])
        cs=CubicSpline(Xh,Yh)
        xs=np.linspace(np.min(Xh),np.max(Xh),res)
	del Yh
        del Xh        
	plt.plot(xs,cs(xs),'k',lw=0.1)

#if len(L[elem[0]].split())>4: #verificar si hay vector de contorno
#	print '--->Existen elementos de contorno en el archivo '+name.split('.')[0]+' por ello debe escribir cuantos contornos desea y el valor minimo del contorno para su correcta visualización.'	
#	P=list()
#	N=100
#	numcont=int(raw_input('# de contornos: ')) #define la cantidad de contornos que desea graficar
#	valmin=raw_input('--->Valor minimo, en caso de que necesite el valor minimo real, escriba min: ')
#	for i in range(numele): #organizar en columnas cada elemento
#		p=list();
#		for j in range(tamxele):	
#			p.append(float(L[elem[i]+j].split()[2]))
#		P.append(p)
#		del p
		
#	for i in range(numele):	#Grafica los contornos
#		if valmin=='min':
#			levmin=np.min(P[i]) #define el valor minimo del contorno
#		else:
#			levmin=float(valmin) #define el valor minimo del contorno
#		levels=np.linspace(levmin, np.max(P[i]), numcont)
#		xi3 = np.linspace(np.min(X[i]), np.max(X[i]), N)
#		yi3 = np.linspace(np.min(Y[i]), np.max(Y[i]), N)
#		zi3 = griddata((X[i], Y[i]), P[i], (xi3[None,:], yi3[:,None]), method='cubic')
#		#manual_locations = [(-1, -1.4), (-0.62, -0.7), (-2, 0.5), (1.7, 1.2), (2.0, 1.4), (2.4, 1.7)]
#		CS = plt.contour(xi3, yi3, zi3,levels, colors='k',)
#		plt.clabel(CS, inline=1, fontsize=8)#manual=manual_locations)

#--------------------------------------------------Graficar Vectores---------------------------------------------------------------------------#
U=list();
V=list();

for i in range(numele): #organizar en columnas cada elemento
	u=list();
	v=list();
	for j in range(tamxele):	
		u.append(float(L[elem[i]+j].split()[3]))
		v.append(float(L[elem[i]+j].split()[4]))
	U.append(u)
	V.append(v)
	del u
	del v
for i in range(numele):	#Grafica de vectores
	N=50
	plt.quiver(X[i][0:np.size(X[i]):N], Y[i][0:np.size(X[i]):N], U[i][0:np.size(X[i]):N], V[i][0:np.size(X[i]):N],scale=10,width=0.001,headwidth=5,headlength=5)
	


#plt.title(name.split('.')[0])
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig('imagenes/'+name.split('.')[0]+'.svg');
plt.show()
plt.close()	
archivo.close
