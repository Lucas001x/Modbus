import minimalmodbus

instr = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instr.serial.baudrate = 9600
instr.serial.timeout = 1
instr.mode = minimalmodbus.MODE_RTU
instr.serial.parity = minimalmodbus.serial.PARITY_NONE
instr.serial.bytesize = 8   
instr.serial.stopbits = 1
instr.debug = False

def ler_modbus():
    try:
        resposta = instr.read_registers(0, 8, functioncode=4)
        if resposta[7] == 65535:
            alerta = "baixa tensao"
        elif resposta[6] == 1:  # Ajuste conforme necessário
            alerta = "alta tensao"
        else:
            alerta = "tensao estavel"
            
        valores = {
            'tensao': round(float(resposta[0]/100), 2),
            'corrente': round(float(resposta[1]/200), 2),
            'potencia': round(float(resposta[2]/20), 2),
            'alerta': alerta
        }
        return valores
    except Exception as e:
        print("Error reading input registers: ", e)
        return None
