def calcular_sueldo(empleado):
    nombre = empleado['nombre']
    tipo = empleado['tipo']
    if tipo == 'A':
        sueldo = 2500000
    elif tipo == 'D':
        sueldo = 3000000
    else:
        sueldo = 'N/A'

    sueldo_empleado = {
        'nombre': nombre,
        'sueldo': sueldo,
        'tipo': tipo

    }
    return sueldo_empleado


empleado = {
    'id_empleado': 1,
    'nombre': 'Luis Ojeda',
    'tipo': 'D'
}


print(calcular_sueldo(empleado))
