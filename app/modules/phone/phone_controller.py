from flask_restx import marshal

from app import db
from app.modules.common.controller import Controller
from app.modules.phone.phone import Phone
from app.modules.phone.phone_dto import PhoneDto
from utils.google_place import search_place, search_phone
from utils.response import send_error, send_result


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

    def _search_from_db(self, address: str):
        try:
            phone = Phone.query.filter_by(address=address.strip()).first().phone
            return phone
        except Exception as e:
            print(e.__str__())
            return None

    def search_phone_number(self, args):
        """
        Search phone number.

        :param args: The list of params to handle.

        :return:
        """
        if not isinstance(args, dict):
            return send_error(message='Could not parse the params')
        if not 'address' in args:
            return send_error("The address must be included in the arguments.")
        address = args['address']
        # search in database
        phone_number = self._search_from_db(address=address)
        if phone_number is None or str(phone_number).strip().__eq__(''):
            place_id = search_place(place=address)
            if place_id is not None:
                phone_number = search_phone(place_id=place_id)
                if phone_number is not None:
                    phone = Phone()
                    phone.address = address
                    phone.phone = phone_number
                    db.session.add(phone)
                    db.session.commit()
                    data = {'formatted_phone_number': phone_number}
                    return send_result(data=data, message='Success')
                else:
                    return send_result(message="Could not find the phone number by using your address.")
        else:
            data = {'formatted_phone_number': phone_number}
            return send_result(data=data, message='Success')