# 🌞 Monitoramento de Placas Solares - Raspberry Pi
## 📖 Sobre o Projeto
Este projeto foi desenvolvido para fornecer uma solução acessível e eficiente para o monitoramento de placas solares, utilizando uma Raspberry Pi rodando Linux.

A proposta nasceu da necessidade de acompanhar em tempo real o desempenho de sistemas fotovoltaicos sem depender de soluções caras ou complexas. Com isso, criamos um sistema capaz de capturar informações de um módulo Modbus, registrando dados essenciais como tensão (V) e corrente (A) de um voltímetro e um amperímetro.

Os dados coletados são processados e exibidos em um dashboard interativo, permitindo ao usuário visualizar gráficos de potência ao longo do tempo, filtrar informações por período e até gerar relatórios para análises detalhadas. O sistema também conta com alertas configuráveis, ajudando a identificar comportamentos anômalos no desempenho do sistema solar.

Por ser baseado em uma arquitetura de baixo custo e open-source, este projeto pode ser facilmente adaptado para diferentes aplicações, incluindo monitoramento de outras fontes de energia ou dispositivos industriais.

## ✨ Funcionalidades
✔️ Monitoramento em tempo real da produção de energia solar
✔️ Armazenamento de dados em banco de dados para consultas futuras
✔️ Dashboard interativo acessível via navegador, dentro da rede local
✔️ Gráficos detalhados da potência gerada ao longo do tempo
✔️ Filtros por data para análise de períodos específicos
✔️ Emissão de relatórios para acompanhamento e auditoria
✔️ Alertas configuráveis para valores anormais de tensão ou corrente
✔️ Suporte a múltiplas Raspberry Pi, permitindo escalabilidade
✔️ Interface responsiva, compatível com dispositivos móveis
✔️ Possibilidade de integração com outros dispositivos IoT

## 🛠 Tecnologias Utilizadas
Este projeto combina diversas tecnologias para garantir desempenho, escalabilidade e facilidade de uso:

Python → Responsável pela leitura dos sensores e processamento dos dados
C++ → Utilizado para otimizar a comunicação com o módulo Modbus
SQLite/MySQL → Banco de dados para armazenamento seguro das medições
Flask/FastAPI → Framework para criação do servidor web
HTML, CSS e JavaScript → Construção do dashboard interativo
Chart.js / Plotly → Geração dos gráficos dinâmicos
Além disso, seguimos práticas recomendadas de acessibilidade e responsividade, garantindo que o sistema seja funcional em computadores, tablets e smartphones.

## 📌 Aplicações e Possibilidades
Este sistema foi projetado pensando na flexibilidade e na escalabilidade. Apesar de ter sido desenvolvido para monitoramento de placas solares, ele pode ser adaptado para diversas outras aplicações, como:

Monitoramento de baterias e sistemas de armazenamento de energia
Supervisão de máquinas e equipamentos industriais
Controle de consumo elétrico em residências ou empresas
Qualquer aplicação que exija leitura e análise de tensão e corrente
Além disso, com a possibilidade de integração com outros dispositivos IoT, este projeto pode evoluir para um sistema ainda mais robusto e automatizado.

## 🤝 Contribuições
Se você deseja contribuir com melhorias para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request! Qualquer sugestão para otimização do código, melhorias na interface do dashboard ou novas funcionalidades são bem-vindas.

Caso tenha alguma dúvida ou precise de suporte, entre em contato através da aba de discussões do repositório.

