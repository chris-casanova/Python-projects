-- Base de datos de práctica para SQL
-- Tablas: categorias, productos, clientes, ordenes, orden_detalle

CREATE DATABASE IF NOT EXISTS practica_sql;
USE practica_sql;

DROP TABLE IF EXISTS orden_detalle;
DROP TABLE IF EXISTS ordenes;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS categorias;

CREATE TABLE categorias (
  categoria_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(255)
);

CREATE TABLE productos (
  producto_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  categoria_id INT,
  stock INT NOT NULL DEFAULT 0,
  FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);

CREATE TABLE clientes (
  cliente_id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  ciudad VARCHAR(50),
  pais VARCHAR(50)
);

CREATE TABLE ordenes (
  orden_id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT NOT NULL,
  fecha DATE NOT NULL,
  estado VARCHAR(20) NOT NULL DEFAULT 'Pendiente',
  total DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

CREATE TABLE orden_detalle (
  orden_id INT NOT NULL,
  producto_id INT NOT NULL,
  cantidad INT NOT NULL,
  precio_unitario DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (orden_id, producto_id),
  FOREIGN KEY (orden_id) REFERENCES ordenes(orden_id),
  FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);

INSERT INTO categorias (nombre, descripcion) VALUES
('Electrónica', 'Artículos de tecnología y dispositivos'),
('Hogar', 'Productos para la casa y la cocina'),
('Juguetes', 'Juegos y entretenimiento para niños');

INSERT INTO productos (nombre, precio, categoria_id, stock) VALUES
('Auriculares inalámbricos', 49.99, 1, 25),
('Smartphone', 299.99, 1, 15),
('Cafetera', 79.50, 2, 12),
('Sartén antiadherente', 24.90, 2, 20),
('Juego de mesa', 19.99, 3, 30),
('Pelota de fútbol', 14.00, 3, 18);

INSERT INTO clientes (nombre, email, ciudad, pais) VALUES
('Ana Pérez', 'ana.perez@example.com', 'Lima', 'Perú'),
('Carlos Ruiz', 'carlos.ruiz@example.com', 'Bogotá', 'Colombia'),
('Lucía Díaz', 'lucia.diaz@example.com', 'Madrid', 'España');

INSERT INTO ordenes (cliente_id, fecha, estado, total) VALUES
(1, '2026-06-01', 'Enviado', 74.89),
(2, '2026-06-03', 'Pendiente', 319.99),
(3, '2026-06-05', 'Cancelado', 44.99);

INSERT INTO orden_detalle (orden_id, producto_id, cantidad, precio_unitario) VALUES
(1, 1, 1, 49.99),
(1, 4, 1, 24.90),
(2, 2, 1, 299.99),
(3, 5, 1, 19.99),
(3, 6, 1, 14.00);

-- Consultas de ejemplo para practicar
-- SELECT básicos
SELECT * FROM clientes;
SELECT nombre, precio FROM productos WHERE stock > 10;

-- JOIN entre órdenes y clientes
SELECT o.orden_id, c.nombre AS cliente, o.fecha, o.total
FROM ordenes o
JOIN clientes c ON o.cliente_id = c.cliente_id;

-- JOIN con detalle y producto
SELECT o.orden_id, p.nombre AS producto, d.cantidad, d.precio_unitario
FROM orden_detalle d
JOIN ordenes o ON d.orden_id = o.orden_id
JOIN productos p ON d.producto_id = p.producto_id;

-- Agrupaciones y agregados
SELECT c.pais, COUNT(*) AS total_clientes
FROM clientes c
GROUP BY c.pais;

SELECT p.categoria_id, SUM(d.cantidad) AS cantidad_vendida, AVG(d.precio_unitario) AS precio_promedio
FROM orden_detalle d
JOIN productos p ON d.producto_id = p.producto_id
GROUP BY p.categoria_id;

-- Subconsulta
SELECT nombre, precio
FROM productos
WHERE precio > (
  SELECT AVG(precio)
  FROM productos
);

-- Actualización y eliminación
UPDATE productos SET stock = stock - 1 WHERE producto_id = 1;
DELETE FROM clientes WHERE cliente_id = 3;

-- Vista de ejemplo
CREATE OR REPLACE VIEW vista_ordenes_clientes AS
SELECT o.orden_id, c.nombre AS cliente, o.fecha, o.estado, o.total
FROM ordenes o
JOIN clientes c ON o.cliente_id = c.cliente_id;

SELECT * FROM vista_ordenes_clientes;
