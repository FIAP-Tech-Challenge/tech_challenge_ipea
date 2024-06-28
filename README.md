# TECH CHALLENGE IPEA

Grupo 17
José Faria- RM 
Marcelo Sampaio – RM 352734
Micheli Souza – RM 352969
Rafael PayHop – RM 352735

Link para acessar o app Streamlit: https://preco-petroleo.streamlit.app/
Link para acessar o código python: https://github.com/FIAP-Tech-Challenge/tech_challenge_ipea

_Tech Challenge é o projeto da fase que englobará os conhecimentos obtidos em todas as disciplinas da fase. Esta é uma atividade que, em princípio, deve ser desenvolvida em grupo. Importante atentar-se ao prazo de entrega, pois trata-se de uma atividade obrigatória, uma vez que sua pontuação se refere a 60% da nota final._

**O PROBLEMA:**

Você foi contratado(a) para uma consultoria, e seu trabalho envolve analisar os dados de preço do petróleo brent, que pode ser encontrado no site do ipea (http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view).
Essa base de dados histórica envolve duas colunas: data e preço (em dólares).

Um grande cliente do segmento pediu para que a consultoria desenvolvesse um dashboard interativo e que gere insights relevantes para tomada de decisão. Além disso, solicitaram que fosse desenvolvido um modelo de Machine Learning para fazer o forecasting do preço do petróleo.

**Seu objetivo é:**

1.Criar um dashboard interativo com ferramentas à sua escolha.

2.Seu dashboard deve fazer parte de um storytelling que traga insights relevantes sobre a variação do preço do petróleo, como situações geopolíticas, crises econômicas, demanda global por energia, etc. Isso pode te ajudar com seu modelo. É obrigatório que você traga pelo menos 4 insights neste desafio.

3.Criar um modelo de Machine Learning que faça a previsão do preço do petróleo diariamente(lembre-se de time series). Esse modelo deve estar contemplado em seu storytelling e deve conter o código que você trabalhou, analisando as performances do modelo.

4.Criar um plano para fazer o deploy em produção do modelo, com as ferramentas que são necessárias.

5.Faça um MVP do seu modelo em produção utilizando o Streamlit.

**CONFIGURANDO O AMBIENTE:**

1.Clonar o repositório do GitHub “git clone https://github.com/FIAP-Tech-Challenge/tech_challenge_ipea”

2.Todas as bibliotecas estarão listadas no arquivo requirements.txt para criação do ambiente virtual

3.Abrir o prompt de comando no diretório /app para criar as variáveis de ambiente: "python -m venv venv"

4.No Windows: "venv\Scripts\activate" e no Linux ou Mac: "source venv/bin/activate"

5.Instalar os pacotes: "pip install -r requirements.txt"

6.Executar o comando: "streamlit run Inicio.py"
