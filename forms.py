from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField('Matricula', [
        validators.DataRequired(message="El campo es requerido"),
        validators.number_range(min=100, max=1000, message="Ingrese un valor valido")
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3,max=10, message="Ingrese un nombre valido")
    ])
    apaterno = StringField('Apaterno', [
        validators.DataRequired(message="El campo es requerido"),
    ])
    amaterno = StringField('Amaterno', [
        validators.DataRequired(message="El campo es requerido"),
    ])
    correo = EmailField('Correo', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])
