import numpy as np
import pylab as pl
#Crea un vector (arreglo) con los valores del eje X
x=[1997,1998,1999,2000,2001,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
#Crea un vector (arreglo) con valores en el eje Y para cada valor en el eje X
y=[0,1,1,1,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5]
#Grafica del vector x contra el vector y
pl.plot(x,y, 'pm')
pl.ylabel('Numero de novios y mascotas')
pl.xlabel('Anios')
pl.title('Numero de novios y mascotas por anios de vida')
#Guarda la grafica
pl.savefig('temp1.png')
