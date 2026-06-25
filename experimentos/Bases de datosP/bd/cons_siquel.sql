SELECT nombre, ciudad FROM clientes
WHERE pais NOT IN ('España');

SELECT nombre, precio FROM productos
WHERE precio > 20;

SELECT orden_id, estado FROM ordenes
WHERE estado = 'Pendiente';