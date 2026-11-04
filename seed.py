"""Carga datos de prueba. Uso:  python seed.py"""
from datetime import date, time, timedelta

from app import create_app
from app.extensions import db
from app.models import Medico, Paciente, Cita
#isaias: esto carga datos a  la base de datos

app = create_app()

with app.app_context():
    if Medico.query.count() > 0:
        print("La base de datos ya tiene datos. Nada que hacer.")
        raise SystemExit

    medicos = [
        Medico(nombre="Dr. Carlos Mendoza", especialidad="Cardiología"),
        Medico(nombre="Dra. Lucía Fernández", especialidad="Pediatría"),
        Medico(nombre="Dr. Andrés Quispe", especialidad="Traumatología"),
        Medico(nombre="Dra. Marcela Rojas", especialidad="Dermatología"),
    ]
    pacientes = [
        Paciente(nombre="Isaías Torrez", telefono="71234567"),
        Paciente(nombre="María Condori", telefono="72345678"),
        Paciente(nombre="Juan Mamani", telefono="73456789"),
        Paciente(nombre="Ana Gutiérrez", telefono="74567890"),
        Paciente(nombre="Pedro Choque", telefono="75678901"),
    ]
    db.session.add_all(medicos + pacientes)
    db.session.commit()

    hoy = date.today()
    citas = [
        Cita(fecha=hoy + timedelta(days=1), hora=time(8, 30), medico_id=medicos[0].id, paciente_id=pacientes[0].id),
        Cita(fecha=hoy + timedelta(days=1), hora=time(9, 0), medico_id=medicos[1].id, paciente_id=pacientes[1].id),
        Cita(fecha=hoy + timedelta(days=2), hora=time(10, 15), medico_id=medicos[2].id, paciente_id=pacientes[2].id),
        Cita(fecha=hoy + timedelta(days=3), hora=time(11, 0), medico_id=medicos[3].id, paciente_id=pacientes[3].id),
        Cita(fecha=hoy + timedelta(days=3), hora=time(15, 30), medico_id=medicos[0].id, paciente_id=pacientes[4].id),
        Cita(fecha=hoy + timedelta(days=4), hora=time(16, 0), medico_id=medicos[1].id, paciente_id=pacientes[0].id),
    ]
    db.session.add_all(citas)
    db.session.commit()
    print(f"Datos cargados: {len(medicos)} médicos, {len(pacientes)} pacientes, {len(citas)} citas.")
