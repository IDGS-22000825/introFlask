from wtforms import Form, ValidationError
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


class CineForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message="Este campo es requerido"),
        validators.Length(min=3, max=10, message="Ingrese un nombre válido")
    ])

    compradores = IntegerField('Compradores', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=100, message="Ingrese un valor válido")
    ])

    cant_boletos = IntegerField('Boletos', [
        validators.DataRequired(message="El campo es requerido")
    ])

    def validate_cant_boletos(self, field):
        if self.compradores.data:
            max_boletos = self.compradores.data * 7
            if field.data < 1 or field.data > max_boletos:
                raise ValidationError(
                    f"Máximo {max_boletos} boletos permitidos"
                )