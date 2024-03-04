# Codigo para utilizar acentos 
#----------------------------------↓
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_ 
#----------------------------------↑
#Practica 16    	Ordenar elementos con sort().					
#Desarrollado por Salazar Chavez Cristian Uriel :D


#Declaramos nuestra variable-lista con '[]'
Com =   ['CPU', 'MB', 'PSU', 'RAM', 'SSD', 'FAN' , 'CASE' , 'HDD']
print('Lista de componentes para una PC GAMER\n\t', Com)

#Se ejecuta el comando '.sort()' para ordenar la  lista de manera alfabetica
Com.sort() 
print('\nLista de componentes (actualizado alfabeticamente)\n\t',Com)

#Se ejecuta el comando '.sort(reverse=True)' para ordenar la  lista de manera alfabetica
Com.sort(reverse=True)
print('\nLista de componentes (actualizado inversamente al alfabeto)\n\t',Com)

#Se ejecuta el comando '.sorted(com)' para ordenar la  lista de manera alfabetica temporalmente
print('\nLista de componentes (actualizado alfabeticamente temporalmente)\n\t', sorted(Com))

#El siguiente impresion regresa al ultimo orden ejecutada
print('\nLista de componentes para una PC GAMER\n\t', Com)
