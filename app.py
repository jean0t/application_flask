# -*- coding: utf-8 -*-
from flask import Flask, request

from config import app_config, app_active

config = app_config[app_active]

from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):
    app = Flask(__name__, template_folder="templates")

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")

    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route("/")
    def index():
        return "Hello World!"
    
    @app.route("/login/")
    def login():
        return "Tela de login"
    
    @app.route("/recovery-password/")
    def recovery_password():
        return "Tela de recuperar senha"
    
    @app.route("/profile", methods=["POST"])
    def create_profile():
        username = request.form["username"]
        password = request.form["password"]

        return "Perfil criado"
    
    @app.route("/profile/<int:id>", methods=["PUT"])
    def edit_total_profile(id):
        username = request.form["username"]
        password = request.form["password"]

        return f"Editado usuário cujo ID é {id}"
    

    return app
