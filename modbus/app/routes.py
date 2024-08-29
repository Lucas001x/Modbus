from flask import render_template, jsonify, request
from app import app, db
from app.models import moduloDC
from app.modbus import ler_modbus
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atualizar_valores')
def atualizar_valores():
    valores = ler_modbus()
    if valores:
        novo_valor = moduloDC(
            id=1,
            tensao=valores['tensao'],
            corrente=valores['corrente'],
            potencia=valores['potencia'],
            alerta=valores['alerta']
        )
        db.session.add(novo_valor)
        db.session.commit()

    return jsonify(valores) if valores else jsonify({'error': 'Erro ao ler os valores'})

@app.route('/templates/dados_historicos.html') 
def dados_historico():
    return render_template('dados_historicos.html')

@app.route('/consumo_diario')
def consumo_diario():
    # Substitua isso pela lógica real para calcular o consumo diário
    hoje = datetime.now().date()
    consumo = db.session.query(db.func.sum(moduloDC.potencia)).filter(db.func.date(moduloDC.registro) == hoje).scalar()
    consumo_diario = consumo if consumo else 0
    return jsonify({'consumo_diario': consumo_diario})

@app.route('/consumo_periodo', methods=['POST'])
def consumo_periodo():
    data_inicio = request.json.get('data_inicio')
    data_fim = request.json.get('data_fim')
    
    # Convertendo strings para objetos datetime
    data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
    data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
    
    consumo = db.session.query(db.func.sum(moduloDC.potencia)).filter(moduloDC.registro.between(data_inicio, data_fim)).scalar()
    consumo_periodo = consumo if consumo else 0
    return jsonify({'consumo_periodo': consumo_periodo})
