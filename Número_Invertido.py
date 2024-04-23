'''
AyED
Autor: Francisco García
16/04/24
'''


#Declaración de variables
vvalor = 0
vv1 = 0
vv2 = 0
vv3 = 0
vv4 = 0
vvalor_final = 0

#Ingreso de Datos
vvalor = int(input('Igresar el Valor:'))

#Cálculo
vv1 = vvalor // 1000
vv2 = (vvalor // 100) % 10
vv3 = (vvalor // 10) % 10
vv4 = vvalor % 10

vvalor_final = vv4 * 1000 + vv3 * 100 + vv2 * 10 + vv1

#Mostrar Resultado
print(vvalor_final)