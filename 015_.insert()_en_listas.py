# Codigo para utilizar acentos 
#----------------------------------↓
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_ 
#----------------------------------↑
#Practica 15    	Insertar elementos con insert().				
#Desarrollado por Salazar Chavez Cristian Uriel :D

#Declaramos nuestra variable-lista con '[]'
Com =   ['CPU', 'MB', 'PSU', 'RAM', 'SSD', 'FAN' , 'CASE' , 'HDD']
print('Lista de componentes para una PC GAMER\n\t', Com)

#Se ejecuta el comando '.insert(n,info)' para borrar el dato de la lista que se seleccione
Com.insert( 0 , 'RGB')
print('\nLista de componentes (actualizado)\n\t',Com)
