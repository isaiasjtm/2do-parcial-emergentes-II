from datetime import datetime

from flask import render_template, request, redirect, url_for, flash

from . import bp_citas
from ..extensions import db
from ..models import Cita, Medico, Paciente


def _parsear(form):
    fecha = datetime.strptime(form["fecha"], "%Y-%m-%d").date()
    hora = datetime.strptime(form["hora"], "%H:%M").time()
    return fecha, hora, int(form["medico_id"]), int(form["paciente_id"])


def _hay_choque(fecha, hora, medico_id, excluir_id=None):
    q = Cita.query.filter_by(fecha=fecha, hora=hora, medico_id=medico_id)
    if excluir_id:
        q = q.filter(Cita.id != excluir_id)
    return q.first() is not None


@bp_citas.route("/")
def listar():
    citas = Cita.query.order_by(Cita.fecha, Cita.hora).all()
    return render_template("citas/lista.html", citas=citas)


@bp_citas.route("/nueva", methods=["GET", "POST"])
def crear():
    medicos = Medico.query.order_by(Medico.nombre).all()
    pacientes = Paciente.query.order_by(Paciente.nombre).all()
    if request.method == "POST":
        try:
            fecha, hora, medico_id, paciente_id = _parsear(request.form)
        except (ValueError, KeyError):
            flash("Datos inválidos. Revisa el formulario.", "danger")
            return render_template("citas/form.html", cita=None, medicos=medicos, pacientes=pacientes)
        if _hay_choque(fecha, hora, medico_id):
            flash("El médico ya tiene una cita en esa fecha y hora.", "danger")
            return render_template("citas/form.html", cita=None, medicos=medicos, pacientes=pacientes)
        db.session.add(Cita(fecha=fecha, hora=hora, medico_id=medico_id, paciente_id=paciente_id))
        db.session.commit()
        flash("Cita programada correctamente.", "success")
        return redirect(url_for("citas.listar"))
    return render_template("citas/form.html", cita=None, medicos=medicos, pacientes=pacientes)


@bp_citas.route("/<int:id>/editar", methods=["GET", "POST"])
def editar(id):
    cita = db.get_or_404(Cita, id)
    medicos = Medico.query.order_by(Medico.nombre).all()
    pacientes = Paciente.query.order_by(Paciente.nombre).all()
    if request.method == "POST":
        try:
            fecha, hora, medico_id, paciente_id = _parsear(request.form)
        except (ValueError, KeyError):
            flash("Datos inválidos. Revisa el formulario.", "danger")
            return render_template("citas/form.html", cita=cita, medicos=medicos, pacientes=pacientes)
        if _hay_choque(fecha, hora, medico_id, excluir_id=cita.id):
            flash("El médico ya tiene una cita en esa fecha y hora.", "danger")
            return render_template("citas/form.html", cita=cita, medicos=medicos, pacientes=pacientes)
        cita.fecha, cita.hora = fecha, hora
        cita.medico_id, cita.paciente_id = medico_id, paciente_id
        db.session.commit()
        flash("Cita actualizada correctamente.", "success")
        return redirect(url_for("citas.listar"))
    return render_template("citas/form.html", cita=cita, medicos=medicos, pacientes=pacientes)


@bp_citas.route("/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    cita = db.get_or_404(Cita, id)
    db.session.delete(cita)
    db.session.commit()
    flash("Cita cancelada.", "warning")
    return redirect(url_for("citas.listar"))
