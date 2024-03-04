# Codigo para utilizar acentos 
#----------------------------------↓
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_ 
#----------------------------------↑
#Practica 3 concatenar strings 
#Desarrollado por Salazar Chavez Cristian Uriel :D

#Declaramos nuestros strings
string1 =   'Bienvenid@'        
string2 =   'humano :D'

#Concatenamos los string usando la operacion '+' 
string3 =   string1 +   ' ' +   string2
print(string3)

#Concatenamos los string y reciclando una variable al realizar la operacion '+'
string1 =   string1 +   ' ' +   string2
print(string1)

#concatenamos los string usando 'print'
print(string1   +   '\n'    + 'Cómo se encuentra?')
