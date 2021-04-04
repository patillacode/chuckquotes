import logging

from flask import Blueprint, jsonify
from .chucklib.quotes import quote_chuck_norris

logger = logging.getLogger(__name__)
bp = Blueprint('api', __name__)


@bp.route('/api', methods=('GET',))
def api():
    return jsonify({'quote': quote_chuck_norris()})
