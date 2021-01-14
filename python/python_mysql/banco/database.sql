CREATE DATABASE IF NOT EXISTS datos_banco;
USE datos_banco;

CREATE TABLE IF NOT EXISTS usuarios(
    id INT(100) AUTO_INCREMENT not null,
    nombre VARCHAR(50) not null,
    apellido VARCHAR(50) not null,
    clave VARCHAR(255) not null,
    dinero INT(100) not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id)
)