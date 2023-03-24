import os

x = int (input ('Ingresa el valor de x: '))
y = int (input ('Ingresa el valor de y: '))

if x>0 and y>0:
    print ('El Cuadrante se encuentra en la zona I')
if x<0 and y>0:
    print ('El Cuadrante se encuentra en la zona II')
if x<0 and y<0:
    print ('El Cuadrante se encuentra en la zona III')
if x>0 and y<0:
    print ('El Cuadrante se encuentra en la zona IV')
print ()
os.system ('pause')