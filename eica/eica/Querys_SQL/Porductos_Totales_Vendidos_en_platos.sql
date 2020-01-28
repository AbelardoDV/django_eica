SELECT id_producto_padre, SUM(cantidad) FROM producto_hijo_compra GROUP BY id_producto_padre;

SELECT
boleta_venta_restaurante.id AS "id_boleta_restaurante",
plato_hijo_venta.id AS "id_plato_hijo_venta",
producto_plato.id_plato_padre,
plato_padre.nombre,
producto_plato.id_producto_padre,
producto_plato.cantidad,
producto_padre.nombre,
producto_padre.unidad
FROM plato_hijo_venta 
INNER JOIN plato_padre ON plato_hijo_venta.id_plato_padre=plato_padre.id
INNER JOIN producto_plato ON producto_plato.id_plato_padre = plato_padre.id
INNER JOIN producto_padre ON producto_padre.id = producto_plato.id_producto_padre
INNER JOIN boleta_venta_restaurante ON boleta_venta_restaurante.id = plato_hijo_venta.id_boleta_venta_restaurante



