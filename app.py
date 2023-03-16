import flask
from Alumnos.routes import alumnos
from Maestros.routes import maestros
from flask_wtf.csrf import CSRFProtect
from model import db
from config import DevelopmentConfig

app=flask.Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()


@app.route('/',methods=['GET'])
def home():
    return flask.jsonify({'Datos':'Home'})

app.register_blueprint(alumnos)
app.register_blueprint(maestros)

if __name__=='__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8080)