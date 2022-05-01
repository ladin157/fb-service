from flask_testing import TestCase

from app.app import db
from app.modules.phone.phone import Phone
from app.modules.user.user import User
from manage import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('settings.config.TestConfig')
        # app.config.from_object('settings.config.DevelopmentConfig')
        return app

    def _add_dummy_data(self):
        admin_user = User()
        admin_user.email = 'admin@gmail.com'
        admin_user.password_hash = 'pbkdf2:sha256:260000$J7YQTLgwW7mP2IQU$30a63bf2a86a34b221ab9d9d1d1e53d063ea0165aada7442a35471b2761d4ffb'
        admin_user.firstname = 'Noi'
        admin_user.lastname = 'Nguyen'
        admin_user.admin = True
        user = User()
        user.email = 'test@gmail.com'
        user.password_hash = 'pbkdf2:sha256:260000$J7YQTLgwW7mP2IQU$30a63bf2a86a34b221ab9d9d1d1e53d063ea0165aada7442a35471b2761d4ffb'
        user.firstname = 'Test'
        user.lastname = 'Test'
        user.admin = False
        db.session.add(admin_user)
        db.session.add(user)
        phone1 = Phone()
        phone1.address = 'Museum of Contemporary Art Australi'
        phone1.phone = '(02) 9245 2400'
        phone2 = Phone()
        phone2.address = 'Computer History Museum Mountain View'
        phone2.phone = '(650) 810-1010'
        db.session.add(phone1)
        db.session.add(phone2)
        db.session.commit()

    def setUp(self):
        db.create_all()
        db.session.commit()
        try:
            self._add_dummy_data()
        except Exception as e:
            pass


    def tearDown(self):
        db.session.remove()
        db.drop_all()
