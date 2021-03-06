from sqlalchemy import Column, Date, Integer, Numeric, Text
from sqlalchemy.dialects.postgresql import ARRAY, DATERANGE

from core_lib import meta
from core_lib import utils

from sqlalchemy import Table, Column, ForeignKey, MetaData

metadata = MetaData()


def reflect_table(table: str) -> Table:
    """
    https://docs.sqlalchemy.org/en/13/core/reflection.html#overriding-reflected-columns
    reflect one table from existing database schema within database
    :arg tablename
    """
    return Table(table, metadata, autoload=True, autoload_with=meta.engine)


# products = reflect_table("products")
# order_details = reflect_table("order_details")
# orders = reflect_table("orders")

# reflect all tables at once
# metadata.reflect(
#     bind=meta.engine
# )
# https://docs.sqlalchemy.org/en/13/core/reflection.html#reflecting-all-tables-at-once
metadata.reflect(bind=meta.engine, only=["products", "orders", "order_details"])
products = metadata.tables["products"]
orders = metadata.tables["orders"]
order_details = metadata.tables["order_details"]
