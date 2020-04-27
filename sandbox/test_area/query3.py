"""
1. Order Subtotal, year, orderID, shippedDate
For each order, calculate a subtotal for each Order (identified by OrderID).
This is a simple query using GROUP BY to aggregate data for each order.
Then Do a join with Orders table and get the shipped date. You need to create a report with
only year, subtotal, orderID and shippeddate for orders shipped between 1996-12-24 and
1997-09-30

WITH CTE AS (
	SELECT "OrderID", round(SUM("UnitPrice"*"Quantity"*(1-"Discount"))::Numeric,2) as total
	FROM public.order_details as od
	GROUP BY "OrderID"
	)
SELECT ords."ShippedDate", ords."OrderID", cte.total, EXTRACT(YEAR FROM ords."ShippedDate")
	FROM public.orders ords
	INNER JOIN CTE
	ON ords."OrderID"=CTE."OrderID"
	WHERE ords."ShippedDate" >= '1996-12-24'
	AND ords."ShippedDate" <= '1997-09-30'
	AND ORDS."ShippedDate" IS NOT NULL
	ORDER BY ords."ShippedDate"
"""

from sqlalchemy.sql.expression import literal, func
from sqlalchemy import cast, Numeric, extract
from core_lib import meta
from core_lib import utils

from test_area import model

print("all good")

od = model.order_details
orders = model.orders
summation = func.sum(od.c.UnitPrice * od.c.Quantity * (1 - od.c.Discount))
rounding = func.round(cast(summation, Numeric(10, 2)), 2)
subtotal_cte = (
    meta.session.query(od.c.OrderID, rounding.label("total")).group_by(literal(1))
).cte("subtotal")
query = (
    meta.session.query(
        orders.c.ShippedDate,
        orders.c.OrderID,
        subtotal_cte.c.total,
        extract("year", orders.c.ShippedDate).label("year"),
    )
    .join(subtotal_cte, orders.c.OrderID == subtotal_cte.c.OrderID)
    .filter(orders.c.ShippedDate >= "1996-12-24")
    .filter(orders.c.ShippedDate <= "1997-09-30")
    .filter(orders.c.ShippedDate.isnot(None))
    .order_by(orders.c.ShippedDate)
    .limit(10)
)
utils.print_table(query)
