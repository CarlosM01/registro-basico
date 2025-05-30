# Sistema de Login y Registro de Usuarios

Este proyecto implementa un sistema de login y registro de usuarios con validaciones para datos personales en formato chileno.

## Características

- Validación de nombres y apellidos (solo letras)
- Validación de RUT chileno con dígito verificador
- Validación de contraseñas seguras
- Sistema de registro de usuarios
- Almacenamiento de datos en memoria

## Requisitos

- Python 3.x
- No se requieren dependencias externas

## Estructura del Proyecto

```
LoginPython/
├── main.py           # Punto de entrada de la aplicación
├── validations.py    # Clase de validaciones
└── README.md         # Este archivo
```

## Clase Validations

La clase `Validations` proporciona métodos estáticos para validar diferentes tipos de datos:

### Métodos Disponibles

#### name(info: str = '') -> str | None
Valida que el nombre o apellido contenga solo letras.
- **Parámetros:**
  - `info`: Mensaje a mostrar al solicitar el input
- **Retorna:**
  - String con el nombre capitalizado si es válido
  - None si no es válido

#### password(info: str = '') -> str | None
Valida la fortaleza de la contraseña.
- **Requisitos:**
  - Mínimo 8 caracteres
  - Debe contener letras y números
- **Parámetros:**
  - `info`: Mensaje a mostrar al solicitar el input
- **Retorna:**
  - String con la contraseña si es válida
  - None si no es válida

#### rut(info: str = '') -> str | None
Valida un RUT chileno.
- **Formato requerido:**
  - Debe incluir guion y dígito verificador (ejemplo: 12345678-9)
  - No se permiten puntos
- **Parámetros:**
  - `info`: Mensaje a mostrar al solicitar el input
- **Retorna:**
  - String con el RUT validado si es válido
  - None si no es válido

## Uso

```python
from validations import Validations

# Crear instancia de Validations
V = Validations()

# Validar nombre
nombre = V.name('Ingrese su nombre: ')

# Validar RUT
rut = V.rut('Ingrese su RUT: ')

# Validar contraseña
password = V.password('Ingrese su contraseña: ')
```

## Ejemplo de Registro de Usuario

```python
def crear_cuenta():
    print('CREAR CUENTA')
    
    v_name = V.name('Ingrese su nombre: ')
    v_apellido_paterno = V.name('Ingrese su apellido paterno: ')
    v_apellido_materno = V.name('Ingrese su apellido materno: ')
    v_rut = V.rut('Ingrese su RUT: ')
    
    # Almacenar usuario
    usuarios.append({
        'nombre': v_name,
        'apellido_paterno': v_apellido_paterno,
        'apellido_materno': v_apellido_materno,
        'rut': v_rut
    })
```

## Validaciones Implementadas

### RUT Chileno
- Verifica el formato correcto (con guion)
- Valida el dígito verificador
- Acepta 'K' como dígito verificador válido
- No permite puntos en el formato

### Nombres y Apellidos
- Solo permite letras
- Elimina espacios en blanco
- Capitaliza la primera letra

### Contraseñas
- Longitud mínima de 8 caracteres
- Debe contener al menos una letra
- Debe contener al menos un número
