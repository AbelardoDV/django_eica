CREATE VIEW transacciones_reporte AS
WITH acumulado AS (

	SELECT id_producto_padre,SUM(cantidad) as suma_transaccion FROM producto_hijo_transaccion GROUP BY id_producto_padre

) SELECT 
DISTINCT ON (acumulado.id_producto_padre) acumulado.id_producto_padre , 
acumulado.suma_transaccion,
producto_hijo_transaccion.fecha_transaccion,
producto_hijo_transaccion.cantidad as ultima_cantidad
FROM acumulado
	INNER JOIN producto_hijo_transaccion 
	ON producto_hijo_transaccion.id_producto_padre = acumulado.id_producto_padre
		GROUP BY 
		acumulado.id_producto_padre , 
		acumulado.suma_transaccion,
		producto_hijo_transaccion.fecha_transaccion,
		producto_hijo_transaccion.cantidad
		ORDER BY acumulado.id_producto_padre , producto_hijo_transaccion.fecha_transaccion DESC