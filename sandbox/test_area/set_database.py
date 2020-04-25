from core_lib import meta

# from  test_area.model import (
#     Record, DrugInfo, DrugPrice, Sale
# )
from . import model

if __name__ == "__main__":
    meta.Base.metadata.drop_all(bind=meta.session.bind)
    meta.Base.metadata.create_all(bind=meta.session.bind)
    meta.session.commit()
