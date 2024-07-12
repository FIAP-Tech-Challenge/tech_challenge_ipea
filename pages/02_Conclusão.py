
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

st.markdown("<h1 style='text-align: center; font-size:28px;'>Tech Challange - Fase 4</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: left; color: orange;'>Conclusão<h2>", unsafe_allow_html=True)
st.write('''  Podemos concluir que o petróleo Brent é uma referência crucial no mercado global de petróleo, influenciando diretamente os preços dos derivados como gasolina e diesel, e, por extensão, impactando os custos de transporte e o preço de mercadorias em todo o mundo. Originário do Mar do Norte e nomeado a partir de uma política interna da Shell, o petróleo Brent ganhou relevância desde o início de sua produção em 1976, apesar de sua qualidade inferior em comparação a outros tipos de petróleo. Sua proximidade ao mar e, consequentemente, menores custos de transporte contribuíram para sua adoção como padrão de referência.

A determinação dos preços do petróleo Brent é complexa, envolvendo não apenas custos de produção e transporte, mas também fatores geopolíticos e econômicos globais. A pandemia da COVID-19 exemplificou como uma crise de saúde que impactou em 2020 a demanda por petróleo, afetando a produção e a logística mundial. Conflitos geopolíticos, como os envolvendo a Rússia, também demonstram como a oferta de petróleo pode ser volátil, levando a aumentos abruptos nos preços devido a sanções e interrupções no fornecimento visto no gráfico em 2011.

A lei da oferta e demanda permanece um princípio fundamental para entender a dinâmica dos preços do petróleo. A crise econômica de 2008, por exemplo, ilustrou como uma recessão pode reduzir a demanda por energia e, consequentemente, baixar os preços do petróleo Brent. Em última análise, o equilíbrio do mercado é alcançado quando a oferta se ajusta à demanda, estabilizando os preços.

Dado o papel essencial do petróleo Brent como benchmark no mercado global, suas flutuações de preço refletem uma interseção complexa de fatores econômicos, políticos e sociais. Neste cenário a implementação do Machine Learning em nossa análise, através do modelo Prophet (biblioteca da empresa Meta que desenvolveu o Facebook) demonstrou ser uma ferramenta poderosa para prever séries temporais no contexto do mercado de petróleo. A alta precisão alcançada sugere que este modelo pode ser de grande utilidade para analistas e investidores, permitindo antecipar variações de preço e tomar decisões mais informadas. Com base nos resultados apresentados, acreditamos que o preço tende a estabilizar na faixa dos US&dollar; 80,00 o barril nos próximos 365 dias.

Destacamos que atualmente o cenário dos preços no ano de 2024 está em alta, portanto a estimativa de US&dollar; 80,00 o barril pode ser superada, visto que o modelo Prophet não leva em consideração fatores externos como conflitos geopolíticos, como as guerras Rússia x Ucrânia e Israel x Palestina, portanto a tendência é favorável aos investimentos para valorização do petróleo, uma vez que a demanda pela oferta e procura pode ser elevada. O fator de risco é a instabilidade política e econômica global, como a eleição nos EUA e a utilização cada vez mais de energias "limpas", conceito que a população mundial está incorporando ao seu modo de vida.''')   
st.markdown("<h2 style='text-align: left; color: orange;'>Grupo 17<h2>", unsafe_allow_html=True)
st.markdown("José Faria- RM 353111 <br> Marcelo Sampaio – RM 352734 <br> Micheli Souza – RM 352969 <br> Rafael Inoue – RM 352735",unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color: orange;'>Referências<h2>", unsafe_allow_html=True)
st.markdown("<a href='http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'>Site do Ipea</a>",unsafe_allow_html=True)
st.markdown("<a href='https://www.ibp.org.br/observatorio-do-setor/analises/covid-19-e-os-impactos-sobre-o-mercado-de-petroleo/#:~:text=Na%20base%20de%20qualquer%20atividade,mercado%20de%20petr%C3%B3leo%20em%202020'>Site do Ibp</a>",unsafe_allow_html=True)
st.markdown("<a href='https://www.cnnbrasil.com.br/economia/mercado/entenda-por-que-o-preco-do-petroleo-disparou-com-a-guerra-entre-ucrania-e-russia/'>Site da Cnn</a>",unsafe_allow_html=True)
