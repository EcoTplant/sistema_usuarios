#!/usr/bin/env python
"""
Sistema Modular de Configuración y Gestión de Usuarios.
Ejecuta un menú en consola para registrar, listar y buscar usuarios.
"""
import sys
from app.config.settings import Settings
from app.usuarios.gestor import GestorUsuarios

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n" + "="*40)
    print(f"  {Settings.APP_NAME} v{Settings.APP_VERSION}")
    print("="*40)
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Mostrar configuración")
    print("5. Salir")
    print("="*40)

def registrar_usuario(gestor):
    """Solicita datos y registra un usuario."""
    print("\n--- Registro de nuevo usuario ---")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    email = input("Email: ")
    
    try:
        # Verificar límite máximo de usuarios (desde variable de entorno)
        if gestor.total_usuarios() >= Settings.MAX_USERS:
            print(f" Error: Se alcanzó el límite máximo de {Settings.MAX_USERS} usuarios.")
            return
        usuario = gestor.registrar_usuario(nombre, edad, email)
        print(f" Usuario registrado con éxito (ID: {usuario['id']})")
    except ValueError as e:
        print(f" Error: {e}")
    except Exception as e:
        print(f" Error inesperado: {e}")

def listar_usuarios(gestor):
    """Muestra todos los usuarios."""
    usuarios = gestor.listar_usuarios()
    if not usuarios:
        print("\n No hay usuarios registrados.")
        return
    print("\n--- Lista de usuarios ---")
    for u in usuarios:
        print(f"ID: {u['id']} | Nombre: {u['nombre']} | Edad: {u['edad']} | Email: {u['email']}")

def buscar_usuario(gestor):
    """Busca usuarios por criterio."""
    print("\n--- Búsqueda de usuarios ---")
    print("Criterios: id, nombre, email")
    criterio = input("Criterio: ").lower()
    if criterio not in ["id", "nombre", "email"]:
        print("Criterio inválido. Use 'id', 'nombre' o 'email'.")
        return
    valor = input(f"Valor a buscar ({criterio}): ")
    resultados = gestor.buscar_usuario(criterio, valor)
    if not resultados:
        print("No se encontraron coincidencias.")
    else:
        print(f"\n {len(resultados)} resultado(s):")
        for u in resultados:
            print(f"ID: {u['id']} | {u['nombre']} ({u['edad']} años) | {u['email']}")

def main():
    """Función principal."""
    # Mostrar configuración inicial
    print(f"Iniciando {Settings.APP_NAME} v{Settings.APP_VERSION}")
    print(f"Admin: {Settings.ADMIN_USER} | Máx. usuarios: {Settings.MAX_USERS}")
    
    gestor = GestorUsuarios()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_usuario(gestor)
        elif opcion == "2":
            listar_usuarios(gestor)
        elif opcion == "3":
            buscar_usuario(gestor)
        elif opcion == "4":
            Settings.mostrar_info()
        elif opcion == "5":
            print("¡Hasta luego!")
            sys.exit(0)
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()