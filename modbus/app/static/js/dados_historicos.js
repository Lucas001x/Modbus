document.addEventListener('DOMContentLoaded', function() {
    // Atualiza o consumo diário ao carregar a página
    atualizarConsumoDiario();

    // Lida com o envio do formulário para buscar o consumo entre datas
    document.getElementById('form_data').addEventListener('submit', function(event) {
        event.preventDefault();
        const dataInicio = document.getElementById('data_inicio').value;
        const dataFim = document.getElementById('data_fim').value;
        atualizarConsumoEntreDatas(dataInicio, dataFim);
    });
});

function atualizarConsumoDiario() {
    fetch('/consumo_diario')
        .then(response => response.json())
        .then(data => {
            document.getElementById('consumo_diario').innerText = data.consumo_diario + ' kWh';
        })
        .catch(error => console.error('Erro ao buscar consumo diário:', error));
}

function atualizarConsumoEntreDatas(dataInicio, dataFim) {
    fetch('/consumo_periodo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data_inicio: dataInicio, data_fim: dataFim })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('consumo_periodo').innerText = data.consumo_periodo + ' kWh';
    })
    .catch(error => console.error('Erro ao buscar consumo entre datas:', error));
}
