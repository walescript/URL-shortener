import os
import requests
from PIL import Image
from io import BytesIO
from ..models import Link
from functools import wraps
from urllib.parse import urlparse
from flask import redirect, url_for, current_app
from datetime import timedelta, datetime
from flask_login import current_user, logout_user


def url_validate(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def fresh_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            # check if the session has expired
            session_timeout = timedelta(hours=5)
            expiration_time = current_user.last_seen + session_timeout
            if datetime.utcnow() > expiration_time:
                logout_user()
                return redirect(url_for('short.login', expired=True))
        return f(*args, **kwargs)
    return decorated_function


def generate_qr_code(data, filename):
    api_key = "s1VQCYNixBdcEGSspWdMYtOAWHGTmvcO8rfB9XucJzFWyFpwy7tmGgN_oMEyvlLA"
    url = f"https://api.qrcode-monkey.com/qr/custom?size=300&data={data}&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

   
        # Open the image from the response content
    img = Image.open(BytesIO(response.content))

    with current_app.app_context():
        # Save the image to a file
        image_folder = os.path.join(current_app.root_path, 'static', 'image')
        image_filename = f"qr_code_{filename}.png"
        image_path = os.path.join(image_folder, image_filename)
        img.save(image_path)

    return image_filename
