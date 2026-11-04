from flask import Blueprint

bp_medicos = Blueprint("medicos", __name__)

from . import routes  # noqa: E402,F401
