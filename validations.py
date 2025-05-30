import re
from datetime import datetime

class Validations:
    def __init__(self):
        pass

    @staticmethod
    def name(info: str = '') -> str | None:
        """Valida que el nombre solo contenga letras y espacios."""
        while True:
            name = input(info).strip()
            if name.isalpha():
                return name.capitalize()
            print('Ingrese un nombre/apellido válido (solo letras, sin espacios).')

    @staticmethod
    def password(info: str = '') -> str | None:
        """Valida la fortaleza de la contraseña."""
        while True:
            input_password = input(info).strip()
            if (len(input_password) >= 8 and 
                any(char.isdigit() for char in input_password) and 
                any(char.isalpha() for char in input_password)):
                return input_password   
            print('La contraseña debe tener al menos 8 caracteres, contener letras y números.')
    
    @staticmethod
    def rut(info: str = '') -> str | None:
        """
        Valida un RUT chileno utilizando el algoritmo del dígito verificador.

        Args:
            rut (str): El RUT a validar, puede incluir guion y puntos.
                       Ejemplos: "12.345.678-9", "12345678-K", "123456789"

        Returns:
            str: RUT validado si es válido, None en caso contrario.
        """
        while True:
            rut = input(info).strip()
            
            # Validar formato básico
            if len(rut) < 3:
                print('El RUT es demasiado corto')
                continue
                
            if rut[-2] != '-':
                print('El RUT debe incluir guion y digito verificador (123456789-0)')
                continue

            rut = rut.upper()  # Convertir a mayúsculas para manejar la 'K'
            rut_ingresado = rut
            rut = rut.replace("-", "")  # Eliminar guion

            # Separar el cuerpo del RUT del dígito verificador
            cuerpo = rut[:-1]
            dv_ingresado = rut[-1]

            # Verificar que el cuerpo sean solo dígitos
            if not cuerpo.isdigit():
                print('El RUT debe contener solo números y guion, sin puntos (123456789-0)')
                continue

            # Calcular el dígito verificador esperado
            suma = 0
            multiplicador = 2

            # Recorrer el cuerpo del RUT de derecha a izquierda
            for digito in reversed(cuerpo):
                suma += int(digito) * multiplicador
                multiplicador += 1
                if multiplicador > 7:
                    multiplicador = 2

            dv_calculado = 11 - (suma % 11)

            if dv_calculado == 11:
                dv_final = '0'
            elif dv_calculado == 10:
                dv_final = 'K'
            else:
                dv_final = str(dv_calculado)

            if dv_final == dv_ingresado:
                return rut_ingresado
            else:
                print('El RUT es inválido.')
                continue