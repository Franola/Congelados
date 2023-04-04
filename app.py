from flask import Flask, render_template, request
import agregar_pedido

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/agrPedido', methods=['POST'])
def agrPedido():
    cliente = str(request.form['cliente'])
    cantidad = int(request.form['cantCongelados'])
    Pedido = [[str(request.form['pedido']), str(request.form['cantidad'])]]
    for i in range(cantidad-1):
        Pedido.append([str(request.form['pedido'+str(i+2)]), str(request.form['cantidad'+str(i+2)])])

    output = agregar_pedido.agregarPedido(nombreCliente=cliente, pedido=Pedido)
    return render_template('index.html', resultado=output)

if __name__ == '__main__':
    app.run(debug=True)