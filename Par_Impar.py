#AyED
#Autor: Francisco García
#19/04/24

'''
Se ingresa un Número Entero.
Mostrar el mensaje 'Par' ó 'Impar' según corresponda
'''

#Declaración de Variables
vnumero = 0
vcalculo = 0

#Ingreso de Datos
vnumero = int(input('Ingresar número:'))

#Cálculo
vcalculo = vnumero % 2

#Condición
if vcalculo == 0:
    print('Este númoero es PAR')
else:
    print('Este número es IMPAR')
