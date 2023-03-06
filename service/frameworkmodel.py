from dao.frameworkmodel import FrameworkModelDAO


class FrameworkModelService:
    def __init__(self, dao: FrameworkModelDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_item_for_lang_name(self, search_lang):
        return self.dao.get_items_for_lang_name(search_lang)
