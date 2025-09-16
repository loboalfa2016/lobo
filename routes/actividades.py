from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Actividad


actividades_bp = Blueprint('actividades', __name__, url_prefix='/actividades')


@actividades_bp.route('/')
@login_required
def lista():
    actividades = Actividad.query.all()
    return render_template('actividades/lista.html', actividades=actividades)


@actividades_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        actividad = Actividad(nombre_actividad=nombre)
        db.session.add(actividad)
        db.session.commit()
        return redirect(url_for('actividades.lista'))
    return render_template('actividades/crear.html')
