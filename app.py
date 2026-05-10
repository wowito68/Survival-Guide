from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reglas')
def reglas():
    return render_template('reglas.html')

@app.route('/notas')
def notas():
    return render_template('notas.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/tiempo')
def tiempo():
    return render_template('tiempo.html')

if __name__ == '__main__':
    app.run(debug=True)
