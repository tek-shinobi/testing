from core_lib import meta
from test_area.model import Record, DrugInfo, DrugPrice, Sale

if __name__ == "__main__":
    meta.Base.metadata.drop_all(bind=meta.session.bind)
    meta.session.commit()
