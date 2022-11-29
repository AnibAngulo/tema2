#Anibal Jose Angulo Cardoza
#A01654684

import streamlit as st
import pandas as pd

dset_rute = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
data_WalM = pd.read_csv(dset_rute)
data_vis = data_WalM.copy()

def showDataset(data):
    return st.dataframe(data)

title = 'Visualización de datos Walmart'
desc = 'En esta WebApp se podrá visualizar datos sobre WalMart USA. Con el objetivo de visualizar y controlar los datos motrados de forma dinámica utilizando Streamlit.'
sidebar = st.sidebar

st.title('Visualización de datos Walmart')
st.header('En esta WebApp se puede visualizar y controlar datos sobre WalMart USA de manera dinámica.')
st.markdown('___')

sidebar.title('Controles')
sidebar.write('En esta sección se encuentran los controles para visualizar el dataset')

Categ= sidebar.selectbox('Categoría:', data_WalM['Category'].unique())

sidebar.markdown('___')

s_mode= sidebar.radio('Ship Mode:',data_WalM['Ship Mode'].unique())
sidebar.markdown('___')
optionals = sidebar.expander('Optional config',True)
disc_val = optionals.slider(
    'Select the Fare:',
    min_value= float(data_WalM['Discount'].min()),
    max_value= float(data_WalM['Discount'].max())

)

data_vis = data_WalM[(data_WalM['Ship Mode']==s_mode)&
    (data_WalM['Category']==Categ)&
    (data_WalM['Discount']==disc_val)
    ]
sidebar.markdown('___')

sidebar.header('Controles checkbox')
if sidebar.checkbox('Visualizar Dataset?'):
    showDataset(data_vis)

