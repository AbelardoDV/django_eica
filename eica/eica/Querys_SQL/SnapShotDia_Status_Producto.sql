WITH vendidos AS (
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
			WHERE boleta_venta_restaurante.valido = True AND
				  boleta_venta_restaurante.fecha_venta <  (SELECT CURRENT_DATE - INTERVAL'0 DAY')
	GROUP BY producto_padre.nombre,producto_padre.unidad,producto_padre.id
	
), comprados AS(
SELECT
		"producto_padre"."id",
		"producto_padre"."nombre", 
		"producto_padre"."unidad", 
		SUM("producto_hijo_compra"."cantidad") AS "cantidad__sum" 
	FROM "producto_hijo_compra" 
		INNER JOIN "boleta_compra" ON ("producto_hijo_compra"."id_boleta_compra" = "boleta_compra"."id") 
		LEFT OUTER JOIN "producto_padre" ON ("producto_hijo_compra"."id_producto_padre" = "producto_padre"."id") 
			WHERE 
				"boleta_compra"."valido" = True AND boleta_compra.fecha_compra	<  (SELECT CURRENT_DATE - INTERVAL'0 DAY')
		GROUP BY "producto_padre"."nombre", "producto_padre"."unidad","producto_padre"."id"
),transacciones as (


WITH acumulado AS (

	SELECT 
		id_producto_padre,
		SUM(cantidad) as suma_transaccion 
	FROM producto_hijo_transaccion 
	WHERE fecha_transaccion <  (SELECT CURRENT_DATE - INTERVAL'0 DAY')
		GROUP BY id_producto_padre

) SELECT 
DISTINCT ON (acumulado.id_producto_padre) acumulado.id_producto_padre , 
acumulado.suma_transaccion,
producto_hijo_transaccion.fecha_transaccion,
producto_hijo_transaccion.cantidad as ultima_cantidad
FROM acumulado
	INNER JOIN producto_hijo_transaccion 
	ON producto_hijo_transaccion.id_producto_padre = acumulado.id_producto_padre
		WHERE producto_hijo_transaccion.fecha_transaccion <  (SELECT CURRENT_DATE - INTERVAL'0 DAY')
		GROUP BY 
			acumulado.id_producto_padre , 
			acumulado.suma_transaccion,
			producto_hijo_transaccion.fecha_transaccion,
			producto_hijo_transaccion.cantidad
		ORDER BY acumulado.id_producto_padre , producto_hijo_transaccion.fecha_transaccion DESC

)
SELECT  
	comprados.id,
	comprados.nombre,
	comprados.unidad,
	comprados.cantidad__sum as cantidad_comprada,
	coalesce(vendidos.cantidad,0) as cantidad_vendida,
	comprados.cantidad__sum - coalesce(vendidos.cantidad,0) as saldo_restante,
	coalesce(ROUND((100*vendidos.cantidad/comprados.cantidad__sum) ::numeric,2),0) as porcentaje_consumo,
	comprados.cantidad__sum-coalesce(transacciones.suma_transaccion,0) as cantidad_almacen,
	transacciones.ultima_cantidad,
	transacciones.fecha_transaccion,
	comprados.cantidad__sum - coalesce(vendidos.cantidad,0)  - (comprados.cantidad__sum-coalesce(transacciones.suma_transaccion,0)) as deficit
FROM comprados 
LEFT JOIN vendidos 
	ON vendidos.id = comprados.id
LEFT JOIN transacciones
	ON transacciones.id_producto_padre = comprados.id
GROUP BY comprados.id,
comprados.nombre,
comprados.unidad,
cantidad_comprada,
cantidad_vendida,
saldo_restante,
porcentaje_consumo,
cantidad_almacen,
transacciones.ultima_cantidad,
transacciones.fecha_transaccion,
deficit 
	ORDER BY comprados.id