import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet 
import matplotlib.pyplot as plt
import numpy as np

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1516199423456-1f1e91b06f25?q=80&w=2049&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: 120%;
background-position: left;
background-repeat: no-repeat
}
</style>
"""

st.set_page_config(layout='wide', page_title='Petróleo - Ipea', page_icon=':oil_drum:')

st.markdown("<h1 style='text-align: center; color: white;'>Estudo de caso: Preço Petróleo Brent</h1>", unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)

def formatar_valor(valor):
    return 'US$ {:.2f}'.format(valor).replace(".",",")

caminho_do_arquivo = 'data/dados_ipea.csv'
df = pd.read_csv(caminho_do_arquivo,sep = ';', index_col="Data", parse_dates=[0]) # Leitura do csv para Dataframe
#Importacao e tratamento da base
df_raw = df
df = df.rename(columns={"Preço - petróleo bruto - Brent (FOB) - US$ - Energy Information Administration (EIA) - EIA366_PBRENT366":"Preço"}) #Renomeando as colunas
df = df.drop("Unnamed: 2", axis=1) #Excluindo colunas que não fazem parte do Dataframe
df.index.name = 'Data'
#df.index = pd.to_datetime(df.index) #transformando a coluna de data para o formato datetime
df.fillna(method='ffill', axis=0, inplace=True)
df['Preço'] = df['Preço'].str.replace(',','.').astype(float)
df_machine = df.copy()

df.index = df.index.strftime('%d/%m/%Y')
df['Preço'] = df['Preço'].apply(formatar_valor)

df_prophet = df_machine.reset_index()
df_prophet = df_prophet[['Data', 'Preço']]
df_prophet = df_prophet.rename(columns={'Data': 'ds', 'Preço': 'y'})

# instanciando o modelo
m = Prophet()
# realizando o treinamento
m.fit(df_prophet)
future = m.make_future_dataframe(periods = 365)
# previsão do modelo
forecast = m.predict(future)
figure = m.plot(forecast, xlabel = 'Data', ylabel = 'Preço', include_legend=True, uncertainty=True)
plt.title('Previsão de Preço do Petróleo')

# definindo uma data de corte de acordo com
data_fim = '2016-11-27'
# definindo os dados de treino, antes da data de corte
train = df_prophet.loc[df_prophet['ds'] <= data_fim]
# definindo os dados de teste posterior a data de corte
test = df_prophet.loc[df_prophet['ds'] > data_fim]

# fazendo previsões com os dados de teste e treino
test_forecast = m.predict(test)
train_forecast = m.predict(train)
# olhando os resultados das previsões com os dados de teste e treino
test_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(7)
train_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(7)

# configurando a área de plotagem
f, ax = plt.subplots(figsize=(14,5))
# alterando a altura
f.set_figheight(5)
# alterando a largura
f.set_figwidth(15)
# plotando o gráfico com dados de teste
test.plot(kind='line',x='ds', y='y', color='red', label='Test', ax=ax)
# plotando o gráfico com dados de teste
train.plot(kind='line',x='ds', y='y', color='blue', label='Train', ax=ax)
# plotando o gráfico com os dados previstos
test_forecast.plot(kind='line',x='ds',y='yhat', color='orange',label='Forecast Test', ax=ax)
train_forecast.plot(kind='line',x='ds',y='yhat', color='purple',label='Forecast Train', ax=ax)
# definindo o título
plt.title('Dados de Treino e Teste vs Previsões')
plt.xlabel('Data')
plt.ylabel('Preço') 

# criando a função MAPE
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

mape = mean_absolute_percentage_error(test['y'],test_forecast['yhat'])
print("MAPE",round(mape,4))

caminho_do_arquivo2 = 'data/owid-energy-data.csv'
dados_energia = pd.read_csv(caminho_do_arquivo2) # Leitura do csv para Dataframe
df_oil_consumo = dados_energia[['country', 'year', 'oil_consumption']]
df_oil_consumo.dropna(inplace=True)
df_oil_consumo = df_oil_consumo.reset_index(drop=True)
df_oil_mundo = df_oil_consumo.query('country == "World"')
df_oil_mundo.drop('country', axis=1, inplace=True)
df_oil_mundo.reset_index(drop=True, inplace=True)
df_oil_mundo['year'] = pd.to_datetime(df_oil_mundo['year'],format='%Y')
df_oil_mundo = df_oil_mundo.set_index('year')
#st.dataframe(df_oil_mundo)
fig = px.line(df_oil_mundo,y=df_oil_mundo['oil_consumption'], title= 'Consumo de energia mundial produzida por petróleo (GWh)',
              labels={"year": "Ano", "oil_consumption": "Consumo de energia (GWh)"})
fig.update_layout(
    title_font_size=20, title_x=0.25 
)

st.markdown("<h1 style='text-align: center; font-size:28px;'>Tech Challange - Fase 4</h1>", unsafe_allow_html=True)

tab1, tab2= st.tabs(['Introdução', 'Base de Dados'])

with tab1:  
    st.markdown("<h2 style='text-align: left; color: orange;'>Qual é a proposta?<h2>", unsafe_allow_html=True)
    st.write('''Como conclusão desta etapa, foi sugerido um projeto para análise dos dados de preço do petróleo Brent. Esta entrega incluirá a criação de um dashboard interativo para gerar insights, bem como um modelo de Machine Learning para previsão dos preços.''')
    st.markdown("<h2 style='text-align: left; color: orange;'>Afinal o que é o 'Petróleo Brent'?<h2>", unsafe_allow_html=True)
    st.write('''O nome "Brent" para o petróleo foi estabelecido por uma política interna da Shell. A empresa costumava nomear seus campos de produção com nomes de aves, e o campo de petróleo Brent recebeu esse nome inspirado no "Pacific Brent Goose" tratando-se de um ganso. Localizado no Mar do Norte, perto da costa da Escócia. Com a produção de petróleo nesse campo começando no ano de 1976 o barril de petróleo do tipo Brent tornou-se uma referência global para o preço do petróleo bruto.''')
    st.markdown("<h2 style='text-align: left; color: orange;'>Determinação dos preços<h2>", unsafe_allow_html=True)
    st.write('''A cotação do petróleo Brent serve como referência para os mercados europeu e asiático.             
Essa cotação nos impacta diretamente, influenciando os preços de seus derivados, como óleo diesel e gasolina, o que, por sua vez, afeta os custos de transporte e o preço de todas as mercadorias.           
Os preços do petróleo dependem principalmente dos custos de produção e transporte.          
Como o petróleo Brent é extraído próximo ao mar, os custos de transporte são significativamente mais baixos.
Embora o Brent tenha uma qualidade inferior, ele se tornou um padrão de referência devido às exportações mais confiáveis, resultando em preços mais elevados.           
Os problemas geopolíticos, crises econômicas e demanda global por energia são fatores importantes a considerar na variação do preço e vamos explorar 4 insights relevantes durante o período explorado: 

    1. Impacto da pandemia do coronavírus na produção global de petróleo
             
A propagação da COVID-19, causada pelo coronavírus SARS-CoV-2, foi o principal impacto nas economias globais recentemente. Originada na China, a pandemia se espalhou por todos os continentes, resultando em milhares de mortes ao redor do mundo e desafiando autoridades de saúde globalmente.
Inicialmente, a China foi o epicentro da doença, tendo sofrido o maior impacto. Medidas como o prolongamento do feriado de ano novo e o isolamento de Wuhan reduziram significativamente a atividade produtiva e a demanda, afetando não apenas a economia chinesa, mas também globalmente, dado o peso econômico do país.
A rápida disseminação na Europa e nas Américas levou muitos países a adotarem políticas de isolamento social para conter o surto, resultando no cancelamento de conferências internacionais e grandes eventos, como as Olimpíadas de Tóquio, que foram adiadas para 2021.
    Na indústria, houve atrasos na entrega de FPSO’s devido à interrupção nos estaleiros próximos ao epicentro inicial da doença, especialmente na China, afetando projetos globais, incluindo os da Petrobras.
O impacto na demanda global de petróleo foi significativo, com a estimativa de uma queda na demanda anual pela primeira vez desde 2009, conforme previsto pela Agência Internacional de Energia (IEA). A demanda chinesa por petróleo e derivados diminuiu, afetando diretamente o mercado brasileiro, especialmente nos setores industrial, de transportes e turismo, que enfrentaram cancelamentos de voos e paralisações na produção.
Esses eventos culminaram em projeções de redução na demanda global por petróleo para 2020, variando de uma leve retração a uma queda significativa, que dependeram da eficácia das medidas de controle da doença.

    2. Impacto da guerra causa aumento de preços

Conflitos envolvendo países importantes no mercado de petróleo, como a Rússia, geram apreensão devido ao risco de retaliação com a redução da oferta de combustível. Como o petróleo é uma commodity, seu preço depende da oferta e demanda globais, e qualquer interrupção na oferta pode aumentar os preços.
Sanções contra a Rússia afetaram a logística e compra de seu petróleo, com refinarias e bancos evitando negócios. A ameaça de ataques no Mar Negro também dificulta transações. Embora as sanções não tenham atingido diretamente a produção e exportação, elas sufocam a economia russa, e Putin pode retaliar segurando o petróleo.
O banco JPMorgan alertou que um corte nas exportações russas poderia elevar o preço do barril para US$ 150, mas isso também prejudicaria a economia russa, já que petróleo e gás natural representaram 43% da receita anual do governo entre 2011 e 2020.
   
     3. Lei da Oferta e Demanda
             
Para que seja possível entender a relação do preço de um determinado item com o consumo do mesmo, voltamos na clássica teoria da economia, criada por Adam Smith: 
"O preço de mercado de uma mercadoria específica é regulado pela proporção entre a quantidade que é efetivamente colocada no mercado (oferta) e a demanda daqueles que estão dispostos a pagar o preço natural da mercadoria, ou seja, o valor total da renda fundiária, do trabalho e do lucro que devem ser pagos para levá-la ao mercado."          
Basicamente, essa teoria pode ser melhor ilustrada em três gráficos:''')

    st.image('data/OfertaDemanda.png')

    st.write('''
Lei da Demanda: Quanto menor for o preço, maior a quantidade de consumidores procurando no mercado os produtos que desejam comprar; da mesma forma, quanto maior for o preço, menor a quantidade de consumidores procurando no mercado os produtos que desejam comprar. Portanto, a curva da procura/demanda representada graficamente é uma curva negativa, ou seja, decrescente.
  
Lei da Oferta: Quanto maior for o preço de determinado produto, mais os vendedores estarão dispostos a vender seu produto, pois assim irão obter mais lucros. Por outro lado, quanto menor for o preço de determinado produto em um mercado, menos os vendedores estarão dispostos a ofertar esse produto. Portanto, a curva da oferta representada graficamente é uma curva positiva, ou seja, crescente.

Equilibrio de Mercado: Equilíbrio é uma situação na qual o preço atingiu o nível em que a quantidade ofertada é igual a quantidade demandada. Assim, em teoria, o próprio mercado, naturalmente, tende a estabilizar os preços dos produtos por causa da lei da oferta e da demanda. O ponto do gráfico onde a curva da oferta e a curva da procura se cruzam é chamado de ponto de equilíbrio. Ele indica o preço que o produto precisa ter para que sua oferta no mercado seja igual à sua procura.
         
    4. Crise econômica em 2008
        
Para ilustrar esse cenário utilizamos o Dataset do <a href="https://github.com/owid/energy-data">Our World in Data</a> mantido pelo autor Pablo Rosado, que trás diversos dados acerca da matriz energética mundial, destacando os tipos de energia, o consumo e producao de energia por país, entre outros. Como o nosso foco está voltado para o preco do petróleo Brent, resolvemos explorar o consumo de energia em todo o mundo gerado exclusivamente pelo petróleo.''', unsafe_allow_html=True)

    st.plotly_chart(fig, theme="streamlit",use_container_width = True)

    st.write('''Vale destacar em 2008, a demanda por consumo de energia originada do petróleo foi impactada, pois houve uma recessão no setor industrial. 
A crise econômica de 2008 foi uma crise financeira global que afetou a economia mundial. Esta crise foi caracterizada por uma queda na liquidez, no acesso a crédito bancário. Foi desencadeada pelo mercado imobiliário dos EUA e teve um impacto significativo na economia global, levando a uma recessão global. 
Foi a pior crise financeira desde a Grande Depressão de 1929 e foi causada por uma combinação de fatores políticos, e afetou diretamente o setor de energia, porque se a demanda por consumo foi menor, consequentemente como já visto anteriormente, o preco do petróleo Brent também reduziu.''')

with tab2:
    st.markdown("<h2 style='text-align: left; color: orange;'>Análise Exploratória<h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write('''A base de dados que estamos utilizando está disponível no site do IPEA - Instituto de Pesquisa Econômica Aplicada, e as informações provêm da "Energy Information Administration (EIA)" do Departamento de Energia dos Estados Unidos.''')
        st.write('''A tabela fornecida contém duas colunas: uma com as datas e outra com os preços do petróleo bruto. Ao analisarmos essa base, foi possível constatar que ela pode se trata de uma série temporal, o que permite aplicar alguns dos modelos de "Machine Learning" (Aprendizado de Máquina) que estudamos. ''')

    with col2:
        st.dataframe(df, width=300)
        st.markdown(f'A tabela possui :orange[{df.shape[0]}] linhas e :orange[{df.shape[1] + 1}] colunas')

    st.divider()
    st.markdown("<h2 style='text-align: left; color: orange;'>Machine Learning", unsafe_allow_html=True)
    st.write('''Para a criarmos uma linha do tempo e uma previsão de preço do petróleo, utilizaremos a biblioteca Prophet, criado pela Meta (empresa responsável pelo Facebook), que é um modelo de previsão de séries temporais. Para o estudo utilizaremos sazionalidade diária, construiremos o método com base em um período de 365 dias para buscar valores futuros e iniciaremos trazendo um gráfico cujos pontos pretos são valores reais de nosso dataframe, enquanto a linha azul são os valores previstos. Mostraremos a seguir como chegamos a esta conclusão.
            É preciso separar a base de dados em treino e teste, para que possamos comparar os valores previstos com os valores reais e normalizá-los (separar as amostragens em uma proporção equalitária para que o aprendizado de máquina seja mais eficiente). O percentual de treino e teste é de 80% e 20%, respectivamente. ''')
    st.pyplot(fig=figure, clear_figure=None, use_container_width=True)
    st.write('''Aplicando a metodologia em uma amostragem menor, observaremos no gráfico, os valores previstos (linha verde) diante dos valores reais (linha vermelha). Nosso modelo instancia e treina para fazer a previsão de séries temporais e exibe os últimos preços junto com os intervalos de confiança associados.
             Após a execução do modelo, calculamos o erro médio percentual absoluto (MAPE) para avaliar a precisão do modelo e a métrica dos resultados. Quanto menor o valor, mais preciso é o modelo.
             Diante disso, o aprendizado da máquina é capaz de prever o preço do petróleo Brent agora em um dataframe maior, conjurando o resultado obtido no gráfico anterior.''')
    st.pyplot(fig=f, clear_figure=None, use_container_width=True)
    st.write('''O MAPE obtido é de 6,799%, o que significa que o modelo tem uma precisão de 93,201%.
             A partir disso, podemos concluir que o modelo é eficaz para prever o preço do petróleo Brent, e que a previsão é bastante precisa.''')
  
    
