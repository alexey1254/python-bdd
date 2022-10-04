CREATE DATABASE sql_py;
USE sql_py;

CREATE TABLE respuestas(
    id INT NOT NULL AUTO_INCREMENT,
    nombre varchar(30) NOT NULL,
    descripcion varchar(2000),
    PRIMARY KEY(id)
);