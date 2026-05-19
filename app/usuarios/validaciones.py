"""
Módulo de validaciones para datos de usuario.
"""
import re

def validar_nombre(nombre: str) -> bool:
    """Valida que el nombre no esté vacío ni contenga solo espacios."""
    return bool(nombre and nombre.strip())

def validar_edad(edad_str: str) -> bool:
    """
    Valida que la edad sea un número entero positivo.
    Retorna True si es válida, False en caso contrario.
    """
    try:
        edad = int(edad_str)
        return 0 < edad < 150
    except ValueError:
        return False

def validar_email(email: str) -> bool:
    """Validación simple de formato de email."""
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

def validar_usuario_unico(usuarios: list, nombre: str) -> bool:
    """Verifica que el nombre de usuario no exista ya en la lista."""
    return not any(u["nombre"].lower() == nombre.lower() for u in usuarios)