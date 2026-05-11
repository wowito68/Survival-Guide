from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key_rpg'

ANSWERS = {
    'reglas': {'q1': 'a', 'q2': 'b'},
    'notas': {'q1': 'b', 'q2': 'c'},
    'skills': {'q1': 'c', 'q2': 'a'},
    'tiempo': {'q1': 'b', 'q2': 'a'}
}

LEVELS = {
    'reglas': 1,
    'notas': 2,
    'skills': 3,
    'tiempo': 4
}

@app.before_request
def require_level():
    if 'nivel' not in session:
        session['nivel'] = 1
    
    endpoint = request.endpoint
    if endpoint in LEVELS:
        if session['nivel'] < LEVELS[endpoint]:
            flash('¡Acceso denegado! Aún no tienes el nivel suficiente para entrar ahí.', 'error')
            return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', nivel=session.get('nivel', 1))

@app.route('/reglas', methods=['GET', 'POST'])
def reglas():
    if request.method == 'POST':
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        if q1 == ANSWERS['reglas']['q1'] and q2 == ANSWERS['reglas']['q2']:
            flash('¡Has superado la Cámara de las Reglas! Se ha desbloqueado el Oráculo.', 'success')
            session['nivel'] = max(session.get('nivel', 1), 2)
            return redirect(url_for('index'))
        else:
            flash('Tus respuestas son incorrectas. Revisa los textos antiguos y vuelve a intentarlo.', 'error')
    return render_template('reglas.html', completado=(session.get('nivel', 1) > 1))

@app.route('/notas', methods=['GET', 'POST'])
def notas():
    if request.method == 'POST':
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        if q1 == ANSWERS['notas']['q1'] and q2 == ANSWERS['notas']['q2']:
            flash('¡Has interpretado las predicciones del Oráculo! Nuevos Skills desbloqueados.', 'success')
            session['nivel'] = max(session.get('nivel', 1), 3)
            return redirect(url_for('index'))
        else:
            flash('Las visiones del Oráculo se nublan. Has fallado.', 'error')
    return render_template('notas.html', completado=(session.get('nivel', 1) > 2))

@app.route('/skills', methods=['GET', 'POST'])
def skills():
    if request.method == 'POST':
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        if q1 == ANSWERS['skills']['q1'] and q2 == ANSWERS['skills']['q2']:
            flash('¡Has asimilado el árbol de habilidades! Solo queda enfrentarte al Tiempo.', 'success')
            session['nivel'] = max(session.get('nivel', 1), 4)
            return redirect(url_for('index'))
        else:
            flash('No estás listo para estos conocimientos. Sigue practicando.', 'error')
    return render_template('skills.html', completado=(session.get('nivel', 1) > 3))

@app.route('/tiempo', methods=['GET', 'POST'])
def tiempo():
    if request.method == 'POST':
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        if q1 == ANSWERS['tiempo']['q1'] and q2 == ANSWERS['tiempo']['q2']:
            flash('¡ENHORABUENA! Has conquistado el Tiempo y estás listo para graduarte.', 'success')
            session['nivel'] = max(session.get('nivel', 1), 5)
            return redirect(url_for('index'))
        else:
            flash('El reloj es implacable. Has perdido la noción del tiempo. Intenta de nuevo.', 'error')
    return render_template('tiempo.html', completado=(session.get('nivel', 1) > 4))

if __name__ == '__main__':
    app.run(debug=True)
