import minimalmodbus

def iniciarmodbus():
    global instr
    instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)

    instr.serial.baudrate = 9600
    instr.serial.timeout = 1
    instr.mode = minimalmodbus.MODE_RTU
    instr.serial.parity = minimalmodbus.serial.PARITY_NONE
    instr.serial.bytesize = 8   
    instr.serial.stopbits = 1
    instr.debug = False

from flask import Flask, render_template, jsonify
app = Flask(__name__)

valores = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atualizar_valores')
def atualizar_valores():
    global instr, valores, resposta
    try:
        resposta = instr.read_registers(0, 8, functioncode=4)
        if (resposta[7] == 65535):
            alerta = "baixa tensao"
        elif (resposta[6] == "true"):
            alerta = "alta tensao"
        else:
            alerta = None
            
        valores = {
            'tensao': float(resposta[0]/100),
            'corrente': float(resposta[1]/200),
            'potencia': float(resposta[2]/20),
            'alerta': alerta
        }

    except Exception as e:
        print("Error reading input registers: " , e)

    return jsonify(valores)


if __name__ == '__main__':
    iniciarmodbus()
    app.run(host="0.0.0.0")