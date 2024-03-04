# Codigo para utilizar acentos 
#----------------------------------↓
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_ 
#----------------------------------↑
#Practica 12    	Eliminar elementos con remove().			
#Desarrollado por Salazar Chavez Cristian Uriel :D

#Declaramos nuestra variable-lista con '[]'
Com =   ['CPU', 'MB', 'PSU', 'RAM', 'SSD', 'FAN' , 'CASE' , 'HDD']
print('Lista de componentes para una PC GAMER\n\t', Com)

#Se ejecuta el comando '.remove' para borrar el dato de la lista 
Com.remove('HDD')
Com.remove('FAN')

#Se imprime todo la lista con la variable Com despues de ejecutar el comando '.remove()'
print('Lista de componentes para una PC GAMER(actualizado)\n\t', Com)
