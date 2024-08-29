from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados
app.config.from_object('config')

# Inicializa o banco de dados
db = SQLAlchemy(app)

from app import routes
