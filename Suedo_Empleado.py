#Declaración de Variables
def main():
    vapellido = ''
    vsueldo = float()

#Ingreso de Datos
vapellido = input('Ingrese el apellido del empleado:')
vvalor_hora = float(input('Ingrese el valor de la hora de trabajo:'))
vhoras_trabajadas = float(input('Ingrese las horas trabajadas:'))

#Calcular Sueldo
vsueldo = (vvalor_hora * vhoras_trabajadas)

#Mostrar el Sueldo del Empleado
print('El empleado' , vapellido , 'cobrará un sueldo de $' , vsueldo)