from flask import Blueprint

bp_citas = Blueprint("citas", __name__)

from . import routes  # noqa: E402,F401

