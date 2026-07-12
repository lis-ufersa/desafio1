#letra b

import pandas as pd 
import plotly.express as px 
import streamlit as st

 #letra c

st.set_page_config(
     page_title = 'DashVacina', 
     layout='wide')

#letra d

df = pd.read_csv('vacinacao.csv')

df.head()

#letra e

st.title("DASHVACINA: Um Dashboard sobre os Dados de Vacinação")

#letra a

df.info()

df['date'] = pd.to_datetime(df['date'])

df.info()

#vamos criar uma lista para facilitar a limpeza usando for

colunas_numericas = ['total_vaccinations', 'people_fully_vaccinated', 'daily_vaccinations']

for col in colunas_numericas:
  df[col] = pd.to_numeric(df[col], errors='coerce')

df.info()

#letra b

df['location'].unique() 

#letra b

#Ajustando o conteúdo da coluna location

#removendo espaços em branco:
df['location'] = df['location'].str.strip()

#padronizando o conteúdo para maiúsculo
df['location'] = df['location'].str.upper()

#mudando todos os valores de BRAZIL para BRASIL
df['location'] = df['location'].str.replace('BRAZIL', 'BRASIL')

df['location'].unique() 

#letra a

fig1 = px.line(df, x = 'date', y = 'total_vaccinations',                
               color = 'location',                
               title = 'Total de pessoas vacinadas por data e paísSegundo a OMS') 
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Total de pessoas vacinadas') 
fig1.show()

#letra b

df_filtro1 = df.query('location == "BRASIL" or location == "INDIA" or location == "UNITED STATES"') 
fig2 = px.pie(df_filtro1, values = 'people_fully_vaccinated', 
              names = 'location', title = 'Dados comparativos de pessoas totalmente vacinadas') 
fig2.show()

#letra c

df_filtro2 = df.query('location == "ASIA" or location == "CHINA"') 
fig3 = px.histogram(df_filtro2, x = 'date', y = 'daily_vaccinations', 
                    color = 'location', title = 'Dados comparativos de pessoas diariamente vacinadas', 
                    barmode = 'group') 
fig3.update_layout(xaxis_title = 'Data', yaxis_title = 'Total') 
fig3.show()

#letra a

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
