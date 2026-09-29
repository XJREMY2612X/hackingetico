from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<namePython>')
def user(namePython):
    # Corregido a user2.html para que coincida con tu carpeta
    return render_template('user2.html', nameHtml=namePython) 

@app.route('/info/<name>/<age>')
def info(name, age):
    # Corregido a info2.html para que coincida con tu carpeta
    return render_template('info2.html', nameHtml=name, ageHtml=age) 

if __name__ == '__main__':
    app.run(debug=True)