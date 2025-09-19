from flask_login import current_user
from functools import wraps
from flask import redirect, url_for


def roles_required(*roles_permitidos):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if current_user.rol.nombre_rol not in roles_permitidos:
                return redirect(url_for('auth.login'))
            return f(*args, **kwargs)
        return wrapper
    return decorator
