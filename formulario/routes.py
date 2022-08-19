from flask import  render_template, url_for, request, flash, redirect
from formulario import app, mysql
from formulario.forms import FormCadastro 
import bcrypt

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    form_cadastro = FormCadastro()
    
    if form_cadastro.validate_on_submit() and "submit_button" in request.form:
        # Definindo Informações do Usuário
        global username
        username = form_cadastro.username.data
        email = form_cadastro.email.data
        pw = form_cadastro.password.data
        
        # Criptografando senha do usuário
        pw = bytes(pw, 'utf-8')
        salt = bcrypt.gensalt(8)
        senha_crypt = bcrypt.hashpw(pw, salt)
        
        # Fazendo conexão com o MySQL e cadastrando usuário no banco de dados.
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO accounts VALUES (NULL, % s ,% s ,% s)', (username, email, senha_crypt))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('home'))
    
    return render_template("cadastro.html", form_cadastro=form_cadastro)

@app.route('/home')
def home():
    return render_template('home.html', username=username)