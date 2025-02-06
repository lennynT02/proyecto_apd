import os

# Configuración de conexión a MySQL
class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql-master")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "root")
    MYSQL_DB = os.getenv("MYSQL_DB", "testdb")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
