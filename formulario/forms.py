# Importando LIBs que serão utilizadas
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from formulario import mysql

# Classe do formulário de cadastro utilizado na página web
class FormCadastro(FlaskForm):
    username = StringField("Nome de Usuário", validators=[DataRequired()]) # Campo de Usuário
    email = StringField("E-mail", validators=[DataRequired(), Email("Endereço de E-mail Inválido.")]) # Campo de E-mail
    password = PasswordField("Senha", validators=[DataRequired(), Length(8, 20)]) # Campo de Senha
    confirm_password = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo('password')]) # Campo de Confirmação de Senha
    submit_button = SubmitField("Enviar") # Botão de enviar
    
# Funções de validação, elas não deixam que usuários únicos sejam criados, fazendo consultas no Banco de dados
    def validate_email(self, email):
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts')
        usuario_email = cursor.fetchall()
        cursor.close()
        for x in usuario_email:
            if x[2] == email.data:
                raise ValidationError('E-mail já cadastrado.')
            else:
                pass
            
    def validate_username(self, username):
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts')
        usuario_username = cursor.fetchall()
        cursor.close()
        for x in usuario_username:
            if x[1] == username.data:
                raise ValidationError('Nome de Usuário já cadastrado.')
            else:
                pass
            
            
        
    
