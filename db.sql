CREATE DATABASE IF NOT EXISTS club_deportivo;

USE club_deportivo;

-- Tabla para los roles (Administrador, Entrenador, Miembro)
CREATE TABLE roles (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla para los usuarios (miembros, entrenadores, administradores)
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    id_rol INT NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

-- Tabla para las actividades deportivas (ej. Fútbol, Baloncesto, Natación)
CREATE TABLE actividades (
    id_actividad INT PRIMARY KEY AUTO_INCREMENT,
    nombre_actividad VARCHAR(100) NOT NULL UNIQUE
);

-- Tabla para los entrenamientos
CREATE TABLE entrenamientos (
    id_entrenamiento INT PRIMARY KEY AUTO_INCREMENT,
    id_entrenador INT NOT NULL,
    id_actividad INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_entrenador) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_actividad) REFERENCES actividades(id_actividad)
);
