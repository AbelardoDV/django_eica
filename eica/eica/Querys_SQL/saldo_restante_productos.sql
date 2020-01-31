SELECT  
	productos_comprados.id,
	productos_comprados.nombre,
	productos_comprados.unidad,
	productos_comprados.cantidad__sum as cantidad_comprada,
	coalesce(productos_vendidos.cantidad,0) as cantidad_vendida,
	productos_comprados.cantidad__sum - coalesce(productos_vendidos.cantidad,0) as saldo_restante,
	ROUND((100*productos_vendidos.cantidad/productos_comprados.cantidad__sum) ::numeric,2) as porcentaje_consumo
FROM productos_comprados 
LEFT JOIN productos_vendidos 
	ON productos_vendidos.id = productos_comprados.id