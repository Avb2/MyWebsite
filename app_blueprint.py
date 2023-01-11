from flask import render_template, Blueprint

app_blueprint = Blueprint('app_blueprint',__name__)

@app_blueprint.route('/')
@app_blueprint.route('/homepage/')
def homepage():
    return render_template('index.html')

@app_blueprint.route('/aboutme/')
def aboutme():
    return render_template('aboutme.html')

@app_blueprint.route('/contactme/')
def contactme():
    return render_template(' contactme.html')

@app_blueprint.route('/portfolio/')
def portfolio():
    return render_template('portfolio.html')
