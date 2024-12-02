from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ListaSpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    elemento = db.Column(db.String(100), nullable=False)