esp='======================================================'
def Caso5 (nombre):
    horas=int(input('INGRESE LA HORAS TRABAJADAS: '))
    if horas<=40:
        salario=horas*16
    else:
        salario_normal=40*16
        salario_extra=20*(horas-40)
        salario=salario_normal+salario_extra
    print('EL TRABAJADOR: ',nombre)
    print('SU SUELDO ES: ',salario)

print(esp)
Caso5('Maicol')
print(esp)