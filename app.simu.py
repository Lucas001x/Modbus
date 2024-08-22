from flask import Flask, render_template, jsonify
app = Flask(__name__)

valores = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atualizar_valores')
def atualizar_valores():
    global valores, resposta
    try:
        resposta = {200, 200, 10, 0, 0, 0, 65535, 0}
        if (resposta[7] == 65535):
            alerta = "baixa tensao"
        elif (resposta[6] == 65535):
            alerta = "alta tensao"
        else:
            alerta = None
            
        valores = {
            'tensao': float(resposta[0]/100),
            'corrente': float(resposta[1]/200),
            'potencia': float(resposta[2]/10),
            'alerta': alerta
        }

    except Exception as e:
        print("Error reading input registers: " , e)

    return jsonify(valores)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")