import numpy as np
from numpy import log

def F(x,y):
    return  x*y*np.log(x**2+y**2)
x01=0.1
y01=0.1
h=0.1
n=0
#код написан для точности 0,001 поэтому все повторяется три раза

x11=x01+h
y11=y01+h
while F(x11,y01)<F(x01, y01):
    x01=x11
    x11=x01+h
    if F(x11,y01)>F(x01, y01):
        x11=x01
        print(x11)
while F(x11,y11)<F(x11, y01):
    y01=y11
    y11=y01+h
    if F(x11,y11)>F(x11, y01):
        y11=y01
        print(y11)
x01=0.4 #
y01=0.4
h=0.01
n=0
x11=x01+h
y11=y01+h
while F(x11,y01)<F(x01, y01):
    x01=x11
    x11=x01+h
    if F(x11,y01)>F(x01, y01):
        x11=x01
        print(x11)
while F(x11,y11)<F(x11, y01):
    y01=y11
    y11=y01+h
    if F(x11,y11)>F(x11, y01):
        y11=y01
        print(y11)



