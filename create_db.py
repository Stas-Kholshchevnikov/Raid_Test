from config_db import db
from dao.models.framework_model import FrameworkModel
from const import DATA_DB


def create_db():
    db.drop_all()
    db.create_all()

    for item in DATA_DB:
        framework = FrameworkModel(name=item["name"], language=item["language"])

        with db.session.begin():
            db.session.add(framework)
