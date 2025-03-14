from flask import Flask, render_template, make_response
import weasyprint

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para generar y descargar el PDF
@app.route('/descargar_pdf')
def descargar_pdf():
    # Renderizar la página HTML (puedes incluir cualquier contenido dinámico en el template)
    html = render_template('index.html')

    # Convertir el HTML a PDF usando WeasyPrint
    pdf = weasyprint.HTML(string=html).write_pdf()

    # Crear una respuesta que sea un archivo descargable
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=mi_cv.pdf'
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
