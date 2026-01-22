from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    titulo="IDGS802"
    lista=['juan','karla', 'Miguel', 'Ana']
    return render_template('index.html', titulo=titulo,lista=lista)

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

@app.route('/operaBas')
def operas1():
    return render_template('operaBas.html')

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    

    return f"La suma es: {float(n1)+float(n2)}"



if __name__ == '__main__':
    app.run(debug=True)