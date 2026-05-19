"""
Módulo gestor de usuarios.
Contiene las operaciones principales del sistema.
"""
from .validaciones import (
    validar_nombre,
    validar_edad,
    validar_email,
    validar_usuario_unico
)

class GestorUsuarios:
    """Clase que maneja el CRUD de usuarios."""
    
    def __init__(self):
        self.usuarios = []      # lista de diccionarios
        self.contador_id = 1
    
    def registrar_usuario(self, nombre: str, edad: str, email: str) -> dict:
        """
        Registra un nuevo usuario después de validar los datos.
        Retorna el usuario creado o lanza una excepción.
        """
        # Validaciones
        if not validar_nombre(nombre):
            raise ValueError("El nombre no puede estar vacío.")
        if not validar_edad(edad):
            raise ValueError("Edad inválida. Debe ser un número entre 1 y 149.")
        if not validar_email(email):
            raise ValueError("Formato de email incorrecto.")
        if not validar_usuario_unico(self.usuarios, nombre):
            raise ValueError(f"El usuario '{nombre}' ya existe.")
        
        usuario = {
            "id": self.contador_id,
            "nombre": nombre.strip(),
            "edad": int(edad),
            "email": email.lower()
        }
        self.usuarios.append(usuario)
        self.contador_id += 1
        return usuario
    
    def listar_usuarios(self) -> list:
        """Retorna la lista completa de usuarios."""
        return self.usuarios
    
    def buscar_usuario(self, criterio: str, valor: str) -> list:
        """
        Busca usuarios por criterio: 'id', 'nombre' o 'email'.
        Retorna lista de coincidencias.
        """
        resultados = []
        valor_busqueda = valor.lower() if criterio != "id" else valor
        for u in self.usuarios:
            if criterio == "id" and str(u["id"]) == valor_busqueda:
                resultados.append(u)
            elif criterio == "nombre" and valor_busqueda in u["nombre"].lower():
                resultados.append(u)
            elif criterio == "email" and valor_busqueda in u["email"]:
                resultados.append(u)
        return resultados
    
    def total_usuarios(self) -> int:
        return len(self.usuarios)