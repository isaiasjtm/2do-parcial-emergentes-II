from flask import Blueprint

bp_pacientes = Blueprint("pacientes", __name__)

from . import routes  # noqa: E402,F401
