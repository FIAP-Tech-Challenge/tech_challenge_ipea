import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide', page_title='Petróleo - Ipea', page_icon=':oil_drum:')

st.title("DASHBOARD PREÇO DO PETRÓLEO BRENT :shopping_trolley:")

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

df.index = df.index.strftime('%d/%m/%Y')
df['Preço'] = df['Preço'].apply(formatar_valor)

st.markdown("<h1 style='text-align: center; color: red;'>Tech Challange - Fase 4</h1>", unsafe_allow_html=True)

st.image('data/brent.jpg',width = 700)

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
             
Os problemas geopolíticos são um fator importante a considerar. As tensões no Oriente Médio afetam especialmente o Brent, reduzindo sua oferta. Quando a oferta de um bem diminui, os preços tendem a subir.
             
Outro fator é a valorização do dólar no mercado internacional, que encarece o preço do combustível pelo câmbio, diminuindo a demanda.
Cada vez mais investidores escolhem investir no Brent devido à sua elevada liquidez, sendo mais rentável do que ações, proporcionando benefícios com a oscilação dos preços e alto retorno financeiro.''')

with tab2:
    st.markdown("<h2 style='text-align: left; color: orange;'>Análise Exploratória<h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write(''' A base de dados que estamos utilizando está disponível no site do IPEA - Instituto de Pesquisa Econômica Aplicada, e as informações provêm da "Energy Information Administration (EIA)" do Departamento de Energia dos Estados Unidos.''')
        st.write('''A tabela fornecida contém duas colunas: uma com as datas e outra com os preços do petróleo bruto. Ao analisarmos essa base, foi possível constatar que ela pode se trata de uma série temporal, o que permite aplicar alguns dos modelos de "Machine Learning" que estudamos. ''')

    with col2:
        st.dataframe(df, width=300)
        st.markdown(f'A tabela possui :red[{df.shape[0]}] linhas e :red[{df.shape[1]}] colunas')
    st.divider()
    st.markdown("<h2 style='text-align: left; color: orange;'>Evolutivo das médias dos valores anual<h2>", unsafe_allow_html=True)
