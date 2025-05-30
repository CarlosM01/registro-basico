from validations import Validations

V = Validations()


usuarios = []


def crear_cuenta():
    print('CREAR CUENTA')

    v_name = V.name('Ingrese su nombre: ')
    v_apellido_paterno = V.name('Ingrese su apellido paterno: ')
    v_apellido_materno = V.name('Ingrese su apellido materno: ')
    v_rut = V.rut('Ingrese su RUT: ')

    usuarios.append({
        'nombre': v_name,
        'apellido_paterno': v_apellido_paterno,
        'apellido_materno': v_apellido_materno,
        'rut': v_rut
    })

    opcion = input('desea crear otra cuenta? (s/n): ')
    if opcion.upper() == 'S':
        crear_cuenta()
    else:
        print('Gracias por usar nuestro sistema')
        print(usuarios)  

crear_cuenta()