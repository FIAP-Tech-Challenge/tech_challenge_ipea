
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
st.write('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras a dictum ligula, ut pulvinar eros. Cras eu leo lacus. Sed rutrum rutrum pretium. Nulla dictum vehicula leo eget scelerisque. Curabitur in massa turpis. Fusce euismod pharetra venenatis. Fusce ut mauris lacinia, aliquet lorem id, hendrerit orci. Sed vitae risus nec dolor interdum molestie. Sed malesuada ornare volutpat. In quis aliquam ipsum, vel porta risus.
Maecenas aliquet odio lacus, et imperdiet lacus rhoncus nec. Maecenas in tempor odio. Quisque at eros orci. In vitae velit at tortor porta luctus in tincidunt nunc. Fusce ut varius metus, efficitur tempus nisl. Mauris sed purus eu erat maximus semper ac at arcu. Proin ullamcorper laoreet tincidunt. Proin justo mauris, finibus id cursus quis, ullamcorper quis tortor. In venenatis euismod leo. Morbi laoreet ligula diam, ac tempus purus ullamcorper eu. Curabitur non sem est. Proin in nibh leo.
Vivamus sed faucibus orci. Donec blandit finibus tempus. In posuere non nibh at maximus. Nullam dignissim enim et risus tincidunt venenatis sed sed lectus. Vivamus sit amet lacinia nisi, quis bibendum lacus. Morbi sed gravida ipsum. Proin accumsan accumsan sapien et dapibus. Sed at dui id justo lacinia blandit eu ac metus. Nunc quis imperdiet dolor, nec finibus sapien. Nullam eu varius enim. Morbi nec augue erat. Nulla facilisi. Cras auctor, est sed euismod hendrerit, enim nulla venenatis justo, eget tempor massa augue non ex.
Mauris orci nisl, laoreet non quam et, pharetra malesuada ligula. Morbi tincidunt tristique arcu, quis luctus ligula volutpat dignissim. Aliquam a imperdiet dolor. Phasellus vitae neque sed leo lacinia tempus. Vivamus maximus nibh sed cursus tincidunt. Nulla purus orci, ullamcorper vitae dui sit amet, dignissim tincidunt urna. Sed et urna rhoncus, convallis enim sit amet, facilisis ipsum.
Cras tempus purus vehicula arcu sodales, mollis euismod enim vulputate. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam nec dolor quis ante finibus auctor vitae quis libero. Phasellus consequat sed tellus a tristique. Nulla volutpat, felis nec lobortis ornare, turpis libero hendrerit lacus, eu venenatis risus ipsum eget magna. Nulla nisl risus, commodo et urna ut, tincidunt imperdiet mauris. Pellentesque nec est lacus. Pellentesque vel hendrerit leo, vel volutpat massa. Phasellus at tempus diam.''')
   
st.markdown("<h2 style='text-align: left; color: orange;'>Grupo 17<h2>", unsafe_allow_html=True)
st.markdown("José Faria- RM <br> Marcelo Sampaio – RM 352734 <br> Micheli Souza – RM 352969 <br> Rafael Inoue – RM 352735",unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color: orange;'>Referências<h2>", unsafe_allow_html=True)
st.markdown("<a href='http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'>Site do Ipea</a>",unsafe_allow_html=True)
st.markdown("<a href='https://www.ibp.org.br/observatorio-do-setor/analises/covid-19-e-os-impactos-sobre-o-mercado-de-petroleo/#:~:text=Na%20base%20de%20qualquer%20atividade,mercado%20de%20petr%C3%B3leo%20em%202020'>Site do Ibp</a>",unsafe_allow_html=True)
st.markdown("<a href='https://www.cnnbrasil.com.br/economia/mercado/entenda-por-que-o-preco-do-petroleo-disparou-com-a-guerra-entre-ucrania-e-russia/'>Site da Cnn</a>",unsafe_allow_html=True)
