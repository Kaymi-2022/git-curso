esp='======================================================'
def IngresoMuseo():
    edad=int(input('INGRESE SU EDAD: '))
    if edad<18:
        resp='NO INGRESA AL MUSEO'
    else:
        resp='SI INGRESA AL MUSEO'
    
    print('USTED ',resp)

print(esp)
IngresoMuseo()
print(esp)