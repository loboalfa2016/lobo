from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Usuario, Rol


usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')


@usuarios_bp.route('/')
@login_required
def lista():
    usuarios = Usuario.query.all()
    return render_template('usuarios/lista.html', usuarios=usuarios)


@usuarios_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    roles = Rol.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password = request.form['password']
        id_rol = int(request.form['id_rol'])
        usuario = Usuario(nombre=nombre, apellido=apellido, email=email, id_rol=id_rol)
        usuario.set_password(password)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('usuarios.lista'))
    return render_template('usuarios/crear.html', roles=roles)
