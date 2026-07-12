-- ============================================
-- CONSULTAS: ver todas las tablas de siquel
-- ============================================

-- 1. Todos los clientes
SELECT * FROM clientes;

-- 2. Todos los productos
SELECT * FROM productos;

-- 3. Todas las categorias
SELECT * FROM categorias;

-- 4. Todas las ordenes
SELECT * FROM ordenes;

-- 5. Todo el detalle de ordenes
SELECT * FROM orden_detalle;

-- ============================================
-- CONSULTAS CON JOIN (datos relacionados)
-- ============================================

-- 6. Ordenes con nombre del cliente
-- SELECT o.orden_id, c.nombre AS cliente, o.fecha, o.estado, o.total
-- FROM ordenes o
-- JOIN clientes c ON o.cliente_id = c.cliente_id;

-- 7. Productos con su categoria
-- SELECT p.nombre AS producto, p.precio, p.stock, cat.nombre AS categoria
-- FROM productos p
-- JOIN categorias cat ON p.categoria_id = cat.categoria_id;

-- 8. Detalle de ordenes con nombre de producto y cliente
-- SELECT o.orden_id, c.nombre AS cliente, p.nombre AS producto,
--        d.cantidad, d.precio_unitario
-- FROM orden_detalle d
-- JOIN ordenes o ON d.orden_id = o.orden_id
-- JOIN clientes c ON o.cliente_id = c.cliente_id
-- JOIN productos p ON d.producto_id = p.producto_id;