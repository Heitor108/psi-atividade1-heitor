from flask import Flask, render_template
from models import usuarios, livros, resenhas, buscar_livro, resenhas_do_livro, buscar_livros

app = Flask(__name__)
app.secret_key = 'segredo'

@app.route('/')
def index():
    return render_template('index.html', livros=livros)

@app.route('/livro/<int:livro_id>')
def livro(livro_id):
    return render_template('livro.html', livro_id=livro_id, livros=livros, resenhas=resenhas)