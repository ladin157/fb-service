from flask_restx import Resource
from werkzeug.datastructures import FileStorage

from app.modules.auth.decorator import token_required
from app.modules.uploader.uploader_controler import UploaderController
from app.modules.uploader.uploader_dto import UploaderDto

api = UploaderDto.api

image_upload = api.parser()
image_upload.add_argument('user_info', type=str, required=True,
                          help='The unique information of the user (it can be ID, email or phone number).')
image_upload.add_argument('image', location='files',
                          type=FileStorage, required=True, help='The image file using for counting.')
image_upload.add_argument('original_image', location='files',
                          type = FileStorage, required=False, help='The original image file using for retraining.')
image_upload.add_argument('pipe_type', type=str, required=False,
                          help = 'The type of the pattern for counting (`general, rectangle, square, oval, circle, vform`)\n'
                                 '`general` for general types (when user does not determine the type of the pipes),\n'
                                 '`rectangle` for the rectangular pipes,\n'
                                 '`square` for square pipes,\n'
                                 '`oval` for oval pipes,\n'
                                 '`circle` for circular pipes,\n'
                                 '`vform` for V-forming pipe.')

json_upload = api.parser()
json_upload.add_argument('user_info', type=str, required=True,
                         help='The unique information of the user (it can be ID, email or phone number).')
json_upload.add_argument('filename', type=str, required=True, help='The filename (with extension) to update. It should be the name of original image in when upload image. Eg. `Image.jpg`')
json_upload.add_argument('json_text', type=str, required = True,
                         help = 'The text (in json format) to upload.\n'
                                'Eg. ``')


@api.route('/image')
class UploadImage(Resource):
    @token_required
    @api.expect(image_upload)
    def post(self):
        '''
        Upload image to count.
        -------------
        :return:
        '''
        # return "Hello world"
        args = image_upload.parse_args()
        controller = UploaderController()
        return controller.upload_image(args=args)


@api.route('/json')
class UploadJson(Resource):
    @token_required
    @api.expect(json_upload)
    def post(self):
        '''
        Upload json after user's verification
        :return:
        '''
        args = json_upload.parse_args()
        controller = UploaderController()
        return controller.upload_json(args=args)
