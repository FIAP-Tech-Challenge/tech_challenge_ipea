import streamlit as st
import pandas as pd
import plotly.express as px

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

df.index = df.index.strftime('%d/%m/%Y')
df['Preço'] = df['Preço'].apply(formatar_valor)

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
             
Os problemas geopolíticos, crises econômicas e demanda global por energia são um fatores importantes a considerar na variação do preço e vamos explorar 4 insights relevantes durante o período explorado: 

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

O banco JPMorgan alertou que um corte nas exportações russas poderia elevar o preço do barril para US$ 150, mas isso também prejudicaria a economia russa, já que petróleo e gás natural representaram 43% da receita anual do governo entre 2011 e 2020.''')

with tab2:
    st.markdown("<h2 style='text-align: left; color: orange;'>Análise Exploratória<h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write(''' A base de dados que estamos utilizando está disponível no site do IPEA - Instituto de Pesquisa Econômica Aplicada, e as informações provêm da "Energy Information Administration (EIA)" do Departamento de Energia dos Estados Unidos.''')
        st.write('''A tabela fornecida contém duas colunas: uma com as datas e outra com os preços do petróleo bruto. Ao analisarmos essa base, foi possível constatar que ela pode se trata de uma série temporal, o que permite aplicar alguns dos modelos de "Machine Learning" que estudamos. ''')

    with col2:
        st.dataframe(df, width=300)
        st.markdown(f'A tabela possui :orange[{df.shape[0]}] linhas e :orange[{df.shape[1] + 1}] colunas')
    st.divider()
    st.markdown("<h2 style='text-align: left; color: orange;'>Evolutivo das médias dos valores anual<h2>", unsafe_allow_html=True)
