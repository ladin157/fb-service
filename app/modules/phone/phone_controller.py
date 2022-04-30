from app.modules.common.controller import Controller
from utils.google_place import search_place, search_phone


class PhoneController(Controller):

    def create(self, data):
        pass

    def get(self):
        pass

    def get_by_id(self, object_id):
        pass

    def update(self, object_id, data):
        pass

    def delete(self, object_id):
        pass

    def search_phone_number(self, args):
        # search in database

        # if not --> search using Google API
        pass
