

def crearBaseDatos():
    print("CREATE DATABASE 'nombreBaseDeDatos';")

def dropDatabase():
    print("DROP DATABASE 'nombreBaseDeDatos'")

def importDatabase():
    print("mysqldump -u nombreUsuario -p nombre_bbdd > path/to/archivo.sql")

def exportDatabase():
    print("mysql -u usuario -p nombre_bbdd < path/to/archivo.sql")

def dropDatabase():
    print("DROP DATABASE nombre_bbdd")

def createTable():
    print("""
    CREATE TABLE facturas(
        numero INT(10) UNSIGNED ZEROFILL AUTO_INCREMENT,
        numeroitem SMALLINT UNSIGNED,
        descripcion VARCHAR(30),
        precioporunidad DECIMAL(5,2) UNSIGNED,
        cantidad TINYINT UNSIGNED,
        PRIMARY KEY (numero,numeroitem)
    )AUTO_INCREMENT=100;
    """)

def insertInto():
    print("INSERT INTO nombre_tabla values ('','');")

def alterTable():
    print("""
    ALTER TABLE ordenes ADD ticket VARCHAR(50) NOT NULL;
    ALTER TABLE ordenes ADD CONSTRAINT fk_ticket FOREIGN KEY (ticket) REFERENCES tickets(ticket);
    """)