import os
from flask import Flask, current_app
from dotenv import load_dotenv

def create_app():
    # Cargar las variables de entorno del archivo .env
    load_dotenv()
    
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )
    
    from . import db

    db.init_app(app)

    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route('/hola')
    def hola():
        return 'Chanchito Feliz'

    @app.route('/show-config')
    def show_config():
        return {
            'DATABASE_HOST': current_app.config['DATABASE_HOST'],
            'DATABASE_USER': current_app.config['DATABASE_USER'],
            'DATABASE_PASSWORD': current_app.config['DATABASE_PASSWORD'],
            'DATABASE': current_app.config['DATABASE']
        }

    return app

