import sqlite3
import datetime

conexion = sqlite3.connect('UniNacional.db')
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre varchar(255),
    apellido varchar(255),
    dni int (20),
    telefono int(40),
    email varchar(255),
    facultad varchar(255),
    observaciones text
);
""")
conexion.commit()

class Registro:
    def abrir(self):
        conexion=sqlite3.connect('UniNacional.db')
        return conexion

    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="""INSERT INTO estudiantes(nombre, apellido, dni, telefono, email, facultad, observaciones) VALUES (?,?,?,?,?,?,?);"""
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="SELECT * FROM estudiantes WHERE dni=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def todo(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT * FROM estudiantes ORDER BY ID DESC"
        cursor.execute(sql)
        return cursor.fetchall()
       
    def baja(self,datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="DELETE FROM estudiantes WHERE dni=?"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
        return cursor.rowcount
        