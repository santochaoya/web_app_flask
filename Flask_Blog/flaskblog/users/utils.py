import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import app, mail


def save_picture(form_picture):
    '''Save uploaded image file and return its filename'''
    # random the image filename to avoid to collide
    random_hex = secrets.token_hex(8)

    # return the filename and extension of uploaded file
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_filename)

    # resize the image
    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)
    return picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Passowrd Reset Request',
                  sender='chaoya_d@126.com',
                  recipients=[user.email])
    msg.body = f'''
    To reset your password, please visit the link below:
{url_for('reset_password', token=token, _external=True)}

    If you did not make this request, please ignore this email and no changes will be made.

    Kind regards,
    XimeCraft
    '''
    mail.send(msg)