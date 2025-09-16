from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Entrenamiento, Actividad, Usuario


entrenamientos_bp = Blueprint('entrenamientos', __name__, url_prefix='/entrenamientos')


@entrenamientos_bp.route('/')
@login_required
def lista():
    entrenamientos = Entrenamiento.query.all()
    return render_template('entrenamientos/lista.html', entrenamientos=entrenamientos)


@entrenamientos_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    if request.method == 'POST':
        id_entrenador = request.form['id_entrenador']
        id_actividad = request.form['id_actividad']
        fecha = request.form['fecha']
        entrenamiento = Entrenamiento(id_entrenador=id_entrenador, id_actividad=id_actividad, fecha=fecha)
        db.session.add(entrenamiento)
        db.session.commit()
        return redirect(url_for('entrenamientos.lista'))
    actividades = Actividad.query.all()
    entrenadores = Usuario.query.all()
    return render_template('entrenamientos/crear.html', actividades=actividades, entrenadores=entrenadores)
