CREATE DATABASE IF NOT EXISTS base_prueba;
USE base_prueba;

CREATE TABLE IF NOT EXISTS usuarios(
    id INT(50) AUTO_INCREMENT not null,
    nombre VARCHAR(50) not null,
    apellido VARCHAR(50),
    email VARCHAR(100) not null,
    contraseña VARCHAR(255) not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS notas(
    id INT(50) AUTO_INCREMENT not null,
    usuario_id INT(50) not null,
    titulo VARCHAR(50) not null,
    contenido TEXT,
    fecha DATE,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;