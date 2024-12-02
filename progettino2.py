from flask import Flask, render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy #
from models import db, ListaSpesa

#creo un app flask
app = Flask(__name__)

# Configura il database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  


# Route principale
@app.route('/')
def home():
    elementi = ListaSpesa.query.all()  
    return render_template('index.html', elementi=elementi)


# Route per aggiungere un nuovo elemento alla lista
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    nuovo_elemento = request.form['elemento'] 
    elemento = ListaSpesa(elemento=nuovo_elemento)
    db.session.add(elemento)  
    db.session.commit() 
    return redirect('/')


# Route per rimuovere un elemento dalla lista (identificato dal suo ID)
@app.route('/rimuovi/<int:id>', methods=['POST'])
def rimuovi(id):
    elemento = ListaSpesa.query.get_or_404(id)  
    db.session.delete(elemento)  
    db.session.commit()  
    return redirect('/')


# Route per svuotare l'intera lista della spesa
@app.route('/svuota', methods=['POST'])
def svuota():
    ListaSpesa.query.delete() 
    db.session.commit() 
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)