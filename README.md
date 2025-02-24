# 🌞 Monitoramento de Placas Solares - Raspberry Pi
## 📖 Sobre o Projeto
Este projeto foi desenvolvido para fornecer uma solução acessível e eficiente para o monitoramento de placas solares, utilizando uma Raspberry Pi rodando Linux.

A proposta nasceu da necessidade de acompanhar em tempo real o desempenho de sistemas fotovoltaicos sem depender de soluções caras ou complexas. Com isso, criamos um sistema capaz de capturar informações de um módulo Modbus, registrando dados essenciais como tensão (V) e corrente (A) de um voltímetro e um amperímetro.

Os dados coletados são processados e exibidos em um dashboard interativo, permitindo ao usuário visualizar gráficos de potência ao longo do tempo, filtrar informações por período e até gerar relatórios para análises detalhadas. O sistema também conta com alertas configuráveis, ajudando a identificar comportamentos anômalos no desempenho do sistema solar.

Por ser baseado em uma arquitetura de baixo custo e open-source, este projeto pode ser facilmente adaptado para diferentes aplicações, incluindo monitoramento de outras fontes de energia ou dispositivos industriais.

## ✨ Funcionalidades
✔️ Monitoramento em tempo real da produção de energia solar <br>
✔️ Armazenamento de dados em banco de dados para consultas futuras <br>
✔️ Dashboard interativo acessível via navegador, dentro da rede local <br>
✔️ Gráficos detalhados da potência gerada ao longo do tempo <br>
✔️ Filtros por data para análise de períodos específicos<br>
✔️ Emissão de relatórios para acompanhamento e auditoria<br>
✔️ Alertas configuráveis para valores anormais de tensão ou corrente<br>
✔️ Suporte a múltiplas Raspberry Pi, permitindo escalabilidade<br>
✔️ Interface responsiva, compatível com dispositivos móveis<br>
✔️ Possibilidade de integração com outros dispositivos IoT<br>

## 🛠 Tecnologias Utilizadas
Este projeto combina diversas tecnologias para garantir desempenho, escalabilidade e facilidade de uso:<br>

Python → Responsável pela leitura dos sensores e processamento dos dados<br>
C++ → Utilizado para otimizar a comunicação com o módulo Modbus<br>
SQLite/MySQL → Banco de dados para armazenamento seguro das medições<br>
Flask/FastAPI → Framework para criação do servidor web<br>
HTML, CSS e JavaScript → Construção do dashboard interativo<br>
Chart.js / Plotly → Geração dos gráficos dinâmicos<br>
Além disso, seguimos práticas recomendadas de acessibilidade e responsividade, garantindo que o sistema seja funcional em computadores, tablets e smartphones.<br>

## 📌 Aplicações e Possibilidades
Este sistema foi projetado pensando na flexibilidade e na escalabilidade. Apesar de ter sido desenvolvido para monitoramento de placas solares, ele pode ser adaptado para diversas outras aplicações, como:<br>

Monitoramento de baterias e sistemas de armazenamento de energia<br>
Supervisão de máquinas e equipamentos industriais<br>
Controle de consumo elétrico em residências ou empresas<br>
Qualquer aplicação que exija leitura e análise de tensão e corrente<br>
Além disso, com a possibilidade de integração com outros dispositivos IoT, este projeto pode evoluir para um sistema ainda mais robusto e automatizado.<br>

## 🤝 Contribuições
Se você deseja contribuir com melhorias para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request! Qualquer sugestão para otimização do código, melhorias na interface do dashboard ou novas funcionalidades são bem-vindas.<br>

Caso tenha alguma dúvida ou precise de suporte, entre em contato através da aba de discussões do repositório.<br>

