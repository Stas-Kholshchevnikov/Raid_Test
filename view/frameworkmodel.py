from flask import Response
from flask_restx import Resource, Namespace
from dao.models.framework_model import FrameworkModelSchema
from implemented import frameworkmodel_service

framework_ns = Namespace('frameworks')
framework_schema = FrameworkModelSchema()
frameworks_schema = FrameworkModelSchema(many=True)


@framework_ns.route('/')
class FrameworkView(Resource):
    def get(self) -> Response:
        """
        Вывод всех записей таблицы FrameworkModel
        :return: json FrameworkModelSchema. Вывод полного списка в формате json
        """
        result = frameworkmodel_service.get_all()
        return frameworks_schema.dump(result), 200


@framework_ns.route('/<lang_name>')
class FrameworkView(Resource):
    def get(self, lang_name: str) -> Response:
        """
        Вывод списка согласно запрошенному языку программирования
        :param lang_name: часть названия языка программирования
        :return: json FrameworkModelSchema. Список результатов поиска по языку программированию в формате json
        """
        result = frameworkmodel_service.get_item_for_lang_name(str(lang_name))
        if not result:
            return "Not Found", 404
        return frameworks_schema.dump(result), 200
