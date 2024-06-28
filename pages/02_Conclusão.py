
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

st.markdown("<h2 style='text-align: left; color: orange;'>Grupo 17<h2>", unsafe_allow_html=True)
st.markdown("José Faria- RM <br> Marcelo Sampaio – RM 352734 <br> Micheli Souza – RM 352969 <br> Rafael Inoue – RM 352735",unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color: orange;'>Referências<h2>", unsafe_allow_html=True)
st.markdown("<a href='http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'>Site do Ipea</a>",unsafe_allow_html=True)
st.markdown("<a href='https://www.ibp.org.br/observatorio-do-setor/analises/covid-19-e-os-impactos-sobre-o-mercado-de-petroleo/#:~:text=Na%20base%20de%20qualquer%20atividade,mercado%20de%20petr%C3%B3leo%20em%202020'>Site do Ibp</a>",unsafe_allow_html=True)
st.markdown("<a href='https://www.cnnbrasil.com.br/economia/mercado/entenda-por-que-o-preco-do-petroleo-disparou-com-a-guerra-entre-ucrania-e-russia/'>Site da Cnn</a>",unsafe_allow_html=True)
