# Codigo para utilizar acentos 
#----------------------------------↓
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_ 
#----------------------------------↑
#Practica 13    	Eliminar elementos con pop().				
#Desarrollado por Salazar Chavez Cristian Uriel :D

#Declaramos nuestra variable-lista con '[]'
Com =   ['CPU', 'MB', 'PSU', 'RAM', 'SSD', 'FAN' , 'CASE' , 'HDD']
print('Lista de componentes para una PC GAMER\n\t', Com)

#Se ejecuta el comando '.pop(n)' para borrar el dato de la lista que se seleccione
respaldo = Com.pop(-1)
print('\nLista de componentes (actualizado)\n\t',Com)

#Se imprime todo la lista con la variable Com despues de ejecutar el comando '.pop()'
print('\nEl componente eliminado de la lista es:', respaldo)
