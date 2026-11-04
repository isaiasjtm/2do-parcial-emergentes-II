# MediControl

Sistema monolítico modular para gestión de médicos, pacientes y citas médicas.
**Stack:** Flask · SQLAlchemy · Flask-Migrate · SQLite · Bootstrap 5.

## Instalación

```bash
python -m venv venv
venv\Scripts\activate          # Windows   (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
```

## Migrnes

```bash
set FLASK_APP=run.py           # Linux/Mac: export FLASK_APP=run.py
flask db init
flask db migrate -m "Migracion inicial"
flask db upgrade
```

## Datos de prueba y ejecución

```bash
python seed.py
python run.py
```

Abrir http://127.0.0.1:5000

## Estructura

```
medicontrol/
├── app/
│   ├── __init__.py        # create_app() (Application Factory)
│   ├── extensions.py      # db, migrate
│   ├── models.py          # Medico, Paciente, Cita
│   ├── medicos/           # bp_medicos   -> /medicos
│   ├── pacientes/         # bp_pacientes -> /pacientes
│   ├── citas/             # bp_citas     -> /citas
│   └── templates/         # base.html + plantillas hijas
├── config.py
├── run.py
├── seed.py
└── requirements.txt
```
