import random
import traceback
import pathlib

from flask import (
    Blueprint,
    current_app,
    render_template,
    request,
)
from .chucklib.quotes import quote_chuck_norris

bp = Blueprint('chuck', __name__)


def get_random_background(current_app):
    base_dir_path = pathlib.Path(current_app.config.get('BASEDIR'))
    chuck_image_path = base_dir_path / 'static' / 'chuckpics'
    return f'background-{random.choice(list(chuck_image_path.iterdir())).stem}'


@bp.route('/', methods=('GET',))
def index():
    try:
        return render_template(
            'index.html',
            quote=quote_chuck_norris(),
            background=get_random_background(current_app),
        )
    except Exception as err:
        current_app.logger.error(err)
        current_app.logger.error(traceback.format_exc())
        return render_template('404.html', request=request)
