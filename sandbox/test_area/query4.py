"""
Build a query to show the Orders list for each employee, showing destination
Country, EmployeeID. Show two new fields in the final result set. One of
them to calculate the sum of Freight sold by every employee, and the other to
calculate the sum of Freight sold by every Employee in every Country.
"""

from sqlalchemy.sql.expression import literal, func
from sqlalchemy import cast, Numeric, extract
from core_lib import meta
from core_lib import utils

from test_area import model

od = model.order_details
orders = model.orders
summation = func.sum(od.c.UnitPrice * od.c.Quantity * (1 - od.c.Discount))
rounding = func.round(cast(summation, Numeric(10, 2)), 2)
subtotal_cte = (
    meta.session.query(od.c.OrderID, rounding.label("total")).group_by(literal(1))
).cte("subtotal")
query = meta.session.query(
    orders.c.ShipCountry,
    orders.c.EmployeeID,
    func.sum(orders.c.Freight)
    .over(partition_by=orders.c.EmployeeID)
    .label("freight_by_employee"),
    func.sum(orders.c.Freight)
    .over(partition_by=[orders.c.EmployeeID, orders.c.ShipCountry])
    .label("freight_by_employee_country"),
).limit(20)
# query = (
#    meta.session.query(
#        orders.c.ShippedDate,
#        orders.c.OrderID,
#        subtotal_cte.c.total,
#        extract("year", orders.c.ShippedDate).label("year"),
#    )
#    .join(subtotal_cte, orders.c.OrderID == subtotal_cte.c.OrderID)
#    .filter(orders.c.ShippedDate >= "1996-12-24")
#    .filter(orders.c.ShippedDate <= "1997-09-30")
#    .filter(orders.c.ShippedDate.isnot(None))
#    .order_by(orders.c.ShippedDate)
#    .limit(10)
# )
utils.print_table(query)
