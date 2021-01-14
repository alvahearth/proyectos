CREATE DATABASE IF NOT EXISTS banco_rut;
USE banco_rut;

CREATE TABLE IF NOT EXISTS usuario(
    id INT(50) AUTO_INCREMENT not null,
    nombre VARCHAR(50) not null,
    apellido VARCHAR(50),
    rut VARCHAR(255) not null,
    contraseña VARCHAR(255) not null,
    CONSTRAINT pk_usuario PRIMARY KEY(id),
    CONSTRAINT uq_rut UNIQUE(rut)
)ENGINE=InnoDb;