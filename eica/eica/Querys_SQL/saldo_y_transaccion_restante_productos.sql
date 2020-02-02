SELECT  
	productos_comprados.id,
	productos_comprados.nombre,
	productos_comprados.unidad,
	productos_comprados.cantidad__sum as cantidad_comprada,
	coalesce(productos_vendidos.cantidad,0) as cantidad_vendida,
	productos_comprados.cantidad__sum - coalesce(productos_vendidos.cantidad,0) as saldo_restante,
	coalesce(ROUND((100*productos_vendidos.cantidad/productos_comprados.cantidad__sum) ::numeric,2),0) as porcentaje_consumo,
	productos_comprados.cantidad__sum-coalesce(transacciones_reporte.suma_transaccion,0) as cantidad_almacen,
	transacciones_reporte.ultima_cantidad,
	transacciones_reporte.fecha_transaccion,
	productos_comprados.cantidad__sum - coalesce(productos_vendidos.cantidad,0)  - (productos_comprados.cantidad__sum-coalesce(transacciones_reporte.suma_transaccion,0)) as deficit
FROM productos_comprados 
LEFT JOIN productos_vendidos 
	ON productos_vendidos.id = productos_comprados.id
LEFT JOIN transacciones_reporte
	ON transacciones_reporte.id_producto_padre = productos_comprados.id
GROUP BY productos_comprados.id,
productos_comprados.nombre,
productos_comprados.unidad,
cantidad_comprada,
cantidad_vendida,
saldo_restante,
porcentaje_consumo,
cantidad_almacen,
transacciones_reporte.ultima_cantidad,
transacciones_reporte.fecha_transaccion,
deficit