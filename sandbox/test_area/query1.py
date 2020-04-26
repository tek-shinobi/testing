# inspector. Performing basic reflection
import pprint
from sqlalchemy import inspect
from core_lib.meta import engine

if __name__ == "__main__":
    inspector = inspect(engine)
    pp = pprint.PrettyPrinter(width=41, compact=True)
    print("TABLE NAMES")
    pp.pprint(inspector.get_table_names())
    print("COLUMN NAMES for products")
    for column in inspector.get_columns("products"):
        pp.pprint(column)
    print("COLUMN NAMES for order_details")
    for column in inspector.get_columns("order_details"):
        pp.pprint(column)
