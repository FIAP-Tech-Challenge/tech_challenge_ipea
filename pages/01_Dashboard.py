import streamlit as st
import streamlit.components.v1 as components

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://app.powerbi.com/view?r=eyJrIjoiMTMyMDNjYTItMDViYy00NTAwLTgwMjItMGExYzVmYjRlODdmIiwidCI6IjIzNjU0OGVlLTQ3YmYtNDEzNy1iZWFhLTA2OWMzOTdhMzA0ZCJ9");
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
st.markdown("<h2 style='text-align: left; color: orange;'>Dashboard<h2>", unsafe_allow_html=True)
   
components.iframe("https://app.powerbi.com/view?r=eyJrIjoiMmM0ODIyZDgtNmYzNy00YzcwLThkY2EtZTMwNTQ3YmJmYjVlIiwidCI6IjIzNjU0OGVlLTQ3YmYtNDEzNy1iZWFhLTA2OWMzOTdhMzA0ZCJ9", height=750)