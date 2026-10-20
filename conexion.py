import os
from contextlib import contextmanager

from psycopg2 import pool

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "dbname": os.getenv("DB_NAME", "chat_unintep"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
    "options": "-c lc_messages=C",
}

_pool = None


def iniciar_pool():
    """Crea el pool de conexiones una sola vez y lo reutiliza."""
    global _pool
    if _pool is None:
        _pool = pool.ThreadedConnectionPool(1, 10, **DB_CONFIG)


def cerrar_pool():
    global _pool
    if _pool is not None:
        _pool.closeall()
        _pool = None


@contextmanager
def obtener_conexion():
    """Presta una conexión del pool, guarda los cambios y la devuelve."""
    iniciar_pool()
    conexion = _pool.getconn()
    try:
        yield conexion
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        _pool.putconn(conexion)


def crear_tablas():
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id SERIAL PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    identificacion VARCHAR(30) UNIQUE NOT NULL,
                    password_hash VARCHAR(64) NOT NULL,
                    activo BOOLEAN NOT NULL DEFAULT TRUE,
                    creado_en TIMESTAMP NOT NULL DEFAULT NOW()
                );
            """)