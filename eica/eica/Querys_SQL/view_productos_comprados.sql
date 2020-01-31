CREATE VIEW productos_comprados
AS
SELECT
"producto_padre"."id",
"producto_padre"."nombre", 
"producto_padre"."unidad", 
SUM("producto_hijo_compra"."cantidad") AS "cantidad__sum" 
FROM "producto_hijo_compra" 
INNER JOIN "boleta_compra" 
ON ("producto_hijo_compra"."id_boleta_compra" = "boleta_compra"."id") 
LEFT OUTER JOIN "producto_padre" 
ON ("producto_hijo_compra"."id_producto_padre" = "producto_padre"."id") 
WHERE "boleta_compra"."valido" = True GROUP BY "producto_padre"."nombre", "producto_padre"."unidad","producto_padre"."id";