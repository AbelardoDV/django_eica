SELECT  
	productos_comprados.id,
	productos_comprados.nombre,
	productos_comprados.unidad,
	productos_comprados.cantidad__sum as cantidad_comprada,
	productos_vendidos.cantidad as cantidad_vendida,
	productos_comprados.cantidad__sum - productos_vendidos.cantidad as saldo_restante,
	ROUND((100*productos_vendidos.cantidad/productos_comprados.cantidad__sum) ::numeric,2) as porcentaje_consumo
FROM productos_comprados 
LEFT JOIN productos_vendidos 
	ON productos_vendidos.id = productos_comprados.id