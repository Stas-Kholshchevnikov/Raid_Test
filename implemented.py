from config_db import db
from dao.frameworkmodel import FrameworkModelDAO
from service.frameworkmodel import FrameworkModelService

frameworkmodel_dao = FrameworkModelDAO(db.session)
frameworkmodel_service = FrameworkModelService(frameworkmodel_dao)
