from sqlalchemy import Column, Date, Integer, Numeric, Text
from sqlalchemy.dialects.postgresql import ARRAY, DATERANGE

from core_lib import meta
from core_lib import utils

from sqlalchemy import Table, Column, ForeignKey, MetaData

metadata = MetaData()


def reflect_table(table: str) -> Table:
    """
    reflect table from existing database schema within database
    :arg tablename
    """
    return Table(table, metadata, autoload=True, autoload_with=meta.engine)


products = reflect_table("products")
order_details = reflect_table("order_details")
orders = reflect_table("orders")
