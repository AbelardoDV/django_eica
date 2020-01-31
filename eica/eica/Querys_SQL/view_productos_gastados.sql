CREATE VIEW productos_vendidos
AS
SELECT
producto_padre.id,
producto_padre.nombre,
producto_padre.unidad,
SUM(plato_hijo_venta.cantidad * producto_plato.cantidad) as cantidad
FROM plato_hijo_venta 
INNER JOIN boleta_venta_restaurante ON boleta_venta_restaurante.id = plato_hijo_venta.id_boleta_venta_restaurante
INNER JOIN plato_padre ON plato_hijo_venta.id_plato_padre=plato_padre.id
INNER JOIN producto_plato ON producto_plato.id_plato_padre = plato_padre.id
INNER JOIN producto_padre ON producto_padre.id = producto_plato.id_producto_padre
WHERE boleta_venta_restaurante.valido = True
GROUP BY producto_padre.nombre,producto_padre.unidad,producto_padre.id;




