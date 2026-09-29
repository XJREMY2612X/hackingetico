from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de Python en español
vulnerabilidades = [
    {"id": 1, "titulo": "Inyección SQL", "categoria": "A03 - Inyección", "severidad": "Alta"},
    {"id": 2, "titulo": "Cross-Site Scripting (XSS)", "categoria": "A03 - Inyección", "severidad": "Media"},
    {"id": 3, "titulo": "Control de Acceso Roto", "categoria": "A01 - Control de Acceso Roto", "severidad": "Alta"}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        categoria = request.form.get('categoria')
        severidad = request.form.get('severidad')
        
        nuevo_id = len(vulnerabilidades) + 1
        vulnerabilidades.append({
            "id": nuevo_id,
            "titulo": titulo,
            "categoria": categoria,
            "severidad": severidad
        })
        
        # Después de guardar, te envía automáticamente a la página de la tabla
        return redirect(url_for('ver_tabla'))
        
    return render_template('index.html')

@app.route('/vulnerabilidades')
def ver_tabla():
    return render_template('tabla.html', vulnerabilidades=vulnerabilidades)

if __name__ == '__main__':
    app.run(debug=True)