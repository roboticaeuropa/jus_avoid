#!/usr/bin/python

import time
import maestro as m

# Crear objeto MicroMaestro
s= m.Controller()

# Asignacion de canales
sharp=1


# Lecturas de distancia a obstaculo antes de arrancar
iter=1
while (1):
	pos_ini_min=s.getPosition(sharp)
	pos_ini_max=s.getPosition(sharp)
	print "ITERACION ",iter
	iter=iter+1
        print "sensing..."
        time.sleep(0.5)
	print "Voltaje (min)=",pos_ini_min
	print "Voltaje (max)=",pos_ini_max
	

