import os
import platform
from xmlrpc.client import boolean

def bienvenida():
        return (""" 
    Bienvenido/a a mis apuntes de MySql :)
        ///////////////////////////////
        /// Para salir pulsa el 0!! ///
        ///////////////////////////////    

        
            Gestionar la base de datos:
        1. Como crear una base de datos.
        2. Como importar una base de datos.
        3. Como exportar una base de datos.
        4. Como eliminar una base de datos.

            Tablas:
        5. Como crear una tabla.
        6. Como insertar valores en una tabla.
        7. Alter table.

            Select:
        8. Como hacer un select
        9. Como hacer un select con un join
        10. Insert con select
        11. Select en una vista

            Vistas:
        12. Crear una vista
        13. Eliminar una vista.

            Procedures:
        14. Crear un procedure.
        15. Eliminar un procedure.
        16. Llamar a un procedure.
        17. Procedure con un case.
        18. Procedure con un if.
        19. Procedure almacenado (Llamar a otro procedure desde un procedure existente)

            Update:
        20. Como hacer un update a una tabla.

            Triggers:
        21. Como crear un trigger.
        22. Como eliminar un trigger.

            Delete-Join:
        23. Como hacer un delete-join


    """)

def stay(txt: str):
    if txt == "n" or txt == "N":
        return False
    else:
        limpiarConsola()
        return True


def limpiarConsola():
    sistema = platform.system()
    if sistema == "Linux":
        os.system("clear")
    if sistema == "Windows":
        os.system("cls")




def crearBaseDatos():
    print("CREATE DATABASE 'nombreBaseDeDatos';")

def dropDatabase():
    print("DROP DATABASE 'nombreBaseDeDatos'")
