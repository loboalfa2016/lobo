from flask import Blueprint, send_file
from io import BytesIO
from reportlab.pdfgen import canvas
from flask_login import login_required
from models import Usuario, Entrenamiento, Actividad


pdf_bp = Blueprint('pdf', __name__, url_prefix='/pdf')


@pdf_bp.route('/historial/<int:id_miembro>')
@login_required
def historial_entrenamientos(id_miembro):
    miembro = Usuario.query.get_or_404(id_miembro)
    entrenamientos = Entrenamiento.query.filter_by(id_entrenador=miembro.id_usuario).all()

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, f"Historial de entrenamientos: {miembro.nombre} {miembro.apellido}")

    y = 760
    for e in entrenamientos:
        actividad = Actividad.query.get(e.id_actividad)
        p.drawString(100, y, f"{e.fecha} - {actividad.nombre_actividad}")
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True,
                     download_name='historial_entrenamientos.pdf',
                     mimetype='application/pdf')
