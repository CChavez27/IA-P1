# Codigo para utilizar acentos 
#----------------------------------↓
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_ 
#----------------------------------↑
#Practica 11    	Eliminar elementos con del.		
#Desarrollado por Salazar Chavez Cristian Uriel :D

#Declaramos nuestra variable-lista con '[]'
Com =   ['CPU', 'MB', 'PSU', 'RAM', 'SSD', 'FAN' , 'CASE' , 'HDD']
print('Lista de componentes para una PC GAMER\n\t', Com)

#Se ejecuta el comando del para borrar los datos en la lista -4 
del Com [-4]

#Se imprime todo la lista con la variable Com despues del comando 'del'
print('Lista de componentes para una PC GAMER(actualizado)\n\t', Com)
