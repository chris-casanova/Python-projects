DROP TABLE IF EXISTS orden_detalle;
DROP TABLE IF EXISTS ordenes;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS categorias;

CREATE TABLE categorias (
  categoria_id SERIAL PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(255)
);

CREATE TABLE productos (
  producto_id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  categoria_id INT REFERENCES categorias(categoria_id),
  stock INT NOT NULL DEFAULT 0
);

CREATE TABLE clientes (
  cliente_id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  ciudad VARCHAR(50),
  pais VARCHAR(50)
);

CREATE TABLE ordenes (
  orden_id SERIAL PRIMARY KEY,
  cliente_id INT NOT NULL REFERENCES clientes(cliente_id),
  fecha DATE NOT NULL,
  estado VARCHAR(20) NOT NULL DEFAULT 'Pendiente',
  total DECIMAL(10,2) NOT NULL
);

CREATE TABLE orden_detalle (
  orden_id INT NOT NULL REFERENCES ordenes(orden_id),
  producto_id INT NOT NULL REFERENCES productos(producto_id),
  cantidad INT NOT NULL,
  precio_unitario DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (orden_id, producto_id)
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