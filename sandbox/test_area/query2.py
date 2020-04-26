"""
1. Order Subtotals
For each order, calculate a subtotal for each Order (identified by OrderID).
This is a simple query using GROUP BY to aggregate data for each order.

SELECT "OrderID", round(SUM("UnitPrice"*"Quantity"*(1-"Discount"))::Numeric,2) as total
	FROM public.order_details as od
	GROUP BY "OrderID"
	ORDER BY "OrderID";
"""

from sqlalchemy.sql.expression import literal, func
from sqlalchemy import cast, Numeric
from core_lib import meta
from core_lib import utils

from test_area import model

od = model.order_details
summation = func.sum(od.c.UnitPrice * od.c.Quantity * (1 - od.c.Discount))
rounding = func.round(cast(summation, Numeric(10, 2)), 2)
query = (
    meta.session.query(od.c.OrderID, rounding.label("total"))
    .group_by(literal(1))
    .order_by(literal(1))
    .limit(10)
)
utils.print_table(query)
