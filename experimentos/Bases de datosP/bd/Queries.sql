/*
SELECT nombre, ciudad FROM clientes
WHERE pais NOT IN ('España');

SELECT nombre, precio FROM productos
WHERE precio > 20;

SELECT orden_id, estado FROM ordenes
WHERE estado = 'Pendiente';
*/

/*MISMA CONSULTA, DIFERENTES FORMAS DE ESCRIBIRLA*/
/* /////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Consulta legacy (ya no se usa) */
SELECT c.nombre, p.nombre, od.cantidad 
FROM ordenes o, productos p, clientes c, orden_detalle od
WHERE o.cliente_id = c.cliente_id
AND o.orden_id = od.orden_id
AND od.producto_id = p.producto_id;

/*consulta con JOIN */
SELECT c.nombre, p.nombre, od.cantidad
FROM clientes c
JOIN ordenes o ON c.cliente_id = o.cliente_id               
JOIN orden_detalle od ON o.orden_id = od.orden_id
JOIN productos p ON od.producto_id = p.producto_id;
/* /////////////////////////////////////////////////////////////////////////////////////////////////// */

-- Corregido: la sintaxis correcta es usar el punto para acceder a la columna "cantidad" desde el alias "od",
-- no "od cantidad". También se cierra la sentencia con punto y coma.
SELECT c.nombre, o.fecha, od.precio_unitario, od.cantidad, (od.precio_unitario * od.cantidad) AS total, o.estado
FROM clientes c
JOIN ordenes o ON c.cliente_id = o.cliente_id
JOIN orden_detalle od ON o.orden_id = od.orden_id
WHERE o.estado = 'Enviado';

/*EXPERIMENTO*/
/* El error estaba en usar NOT IN con una subconsulta sobre la misma tabla ordenes.
   Esa forma es innecesaria y además puede fallar si hay valores NULL en orden_id.
   Lo correcto aquí es filtrar directamente por el estado de la orden. */
SELECT c.nombre, o.fecha, od.precio_unitario, od.cantidad
FROM clientes c
JOIN ordenes o ON c.cliente_id = o.cliente_id
JOIN orden_detalle od ON o.orden_id = od.orden_id
WHERE o.estado = 'Enviado';
/*EXPERIMENTO*/