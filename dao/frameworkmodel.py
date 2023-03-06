from dao.models.framework_model import FrameworkModel


class FrameworkModelDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(FrameworkModel).all()

    def get_items_for_lang_name(self, search_lang):
        return self.session.query(FrameworkModel).filter(FrameworkModel.language.ilike(f"%{search_lang}%")).all()
