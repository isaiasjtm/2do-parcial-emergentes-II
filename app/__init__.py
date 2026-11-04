from flask import Flask, render_template

from config import Config
from .extensions import db, migrate


def create_app(config_class=Config):
    """Application Factory de MediControl."""
    app = Flask(__name__)
    app.config.from_object(config_class)


    db.init_app(app)
    migrate.init_app(app, db)


    from . import models  


    from .medicos import bp_medicos
    from .pacientes import bp_pacientes
    from .citas import bp_citas

    app.register_blueprint(bp_medicos, url_prefix="/medicos")
    app.register_blueprint(bp_pacientes, url_prefix="/pacientes")
    app.register_blueprint(bp_citas, url_prefix="/citas")

    @app.route("/")
    def index():
        from .models import Medico, Paciente, Cita
        return render_template(
            "index.html",
            total_medicos=Medico.query.count(),
            total_pacientes=Paciente.query.count(),
            total_citas=Cita.query.count(),
        )

    return app
