"""
Módulo de configuración del sistema.
Carga variables de entorno desde .env y las valida.
"""
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

class Settings:
    """Configuración centralizada del sistema."""
    
    APP_NAME = os.getenv("APP_NAME", "Sistema Usuarios")
    APP_VERSION = os.getenv("APP_VERSION", "1.0")
    ADMIN_USER = os.getenv("ADMIN_USER", "admin")
    MAX_USERS = int(os.getenv("MAX_USERS", "100"))
    
    @classmethod
    def mostrar_info(cls):
        """Muestra la configuración actual (útil para depuración)."""
        print(f"{cls.APP_NAME} v{cls.APP_VERSION}")
        print(f"Admin: {cls.ADMIN_USER} | Máx. usuarios: {cls.MAX_USERS}")