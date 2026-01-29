from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import math

import forms

app = Flask(__name__)

# Seguridad y Clave secreta
app.secret_key = 'Clave secreta'
csrf = CSRFProtect()

@app.route('/')
def index():
    titulo="IDGS802"
    lista=['juan','karla', 'Miguel', 'Ana']
    return render_template('index.html', titulo=titulo,lista=lista)

@app.route('/usuarios', methods = ['GET', 'POST'])
def usuarios():
    mat = 0
    nom = ''
    apa = ''
    ama = ''
    email = ''

    usuarios_class=forms.UserForm(request.form)
    
    if request.method == 'POST' and usuarios_class.validate():
        # De esta forma obtenemos los datos desde el html
        mat = usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.apaterno.data
        ama = usuarios_class.amaterno.data
        email = usuarios_class.correo.data
        
        mensaje = 'Bienvenido'.format(nom)
        flash(mensaje)

    return render_template('usuarios.html', form=usuarios_class, mat=mat, nom=nom, apa=apa, ama=ama, email=email)

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')

@app.route('/hola')
def hola():
    return "Hola amiwitzi"

@app.route('/user/<string:user>')
def user(user):
    return f"Hola {user}"

@app.route('/numero/<float:numer>')
def num(numer):
    return "Numero: {numer}".format(numer)

@app.route('/user/<float:d>/<string:name>')
def username(id, name):
    return "Id: {} nombre: {}".format(id,name)

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return "la suma  es {}".format(n1+n2)

@app.route('/default/<string:name>')
def fuc2(param="juan"):
    return f"<h1> Hola {param} </h1>"


@app.route('/operas')
def operas():
    return '''
    <from>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="name">Paterno:</label>
    <input type="text" id="name" name="name" required>
    </form>
    '''

@app.route('/operaBas', methods=["GET","POST"])
def operas1():
    n1=0
    n2=0
    res=0

    if request.method == "POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        res=float(n1)+float(n2)

    return render_template('operaBas.html' , n1=n1,n2=n2,res=res)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    

    return f"La suma es: {float(n1)+float(n2)}"

@app.route("/alumnos")
def alumnos():

    return render_template("alumnos.html")

@app.route("/distancia", methods=["GET", "POST"])
def distancia():

    d1 = float(request.form.get("d1"))
    d2 = float(request.form.get("d2"))
    d3 = float(request.form.get("d3"))
    d4 = float(request.form.get("d4"))
    res = 0
    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    
    if request.method == "POST":

        res = math.sqrt((d3 - d1) ** 2 + (d4 - d2) ** 2)

    return render_template("distancia.html", d1=d1,d2=d2,d3=d3,d4=d4,res=res)



# Cinepolis
class Personas:
    def __init__(self):
        self.historial = []
    
    def calcularTotal(self, boletos, tarjeta):
        if boletos <= 0:
            return 0 
        
        if boletos <= 2:
            cost = 12 * boletos
        elif boletos <= 5:
            cost = 12 * boletos * 0.90
        else:
            cost = 12 * boletos * 0.85
        
        if tarjeta == "si":
            cost *= 0.90 
        
        return round(cost, 2)

personas = Personas()

@app.route('/cinepolis', methods=['GET', 'POST'])
def cinepolis():
    mensaje = None
    nombre = ""
    cantidad_compradores = 0
    tarjeta = "no"
    cantidad_boletos = 0
    total = 0

    if request.method == "POST":
        nombre = request.form.get('nombre', "").strip()
        tarjeta = request.form.get('tarjeta', "no")

        try:
            cantidad_compradores = int(request.form.get('cantidad_compradores', 0))
            cantidad_boletos = int(request.form.get('cantidad_boletos', 0))
        except ValueError:
            mensaje = "Por favor, ingrese valores numéricos válidos."
            return render_template('cinepolis.html', mensaje=mensaje)

        if cantidad_compradores <= 0:
            mensaje = "Debe haber al menos un comprador."
        elif cantidad_boletos <= 0:
            mensaje = "Debe comprar al menos un boleto."
        else:
            max_boletos = cantidad_compradores * 7
            if cantidad_boletos > max_boletos:
                mensaje = f"Has excedido el número máximo de boletos permitidos ({max_boletos})."
            else:
                total = personas.calcularTotal(cantidad_boletos, tarjeta)
                personas.historial.append((nombre, total))

    return render_template(
        'cinepolis.html',
        mensaje=mensaje,
        nombre=nombre,
        tipo='error',
        cantidad_compradores=cantidad_compradores,
        tarjeta=tarjeta,
        cantidad_boletos=cantidad_boletos,
        total=total
    )

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)

#pip freezer > requiremet.txt