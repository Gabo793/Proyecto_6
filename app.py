#Se importa librerias necesarias 
import streamlit as st
import pandas as pd
import plotly_express as px

#Se importa el DataFrame necesario
car_data = pd.read_csv("C:/Users/dicop/Desktop/Data/Data/Data/Data_Scientist/Sprint_6/Proyecto 6/vehicles_us.csv")

#Titulo de la pagina web
st.header("Comparacion de vehiculos usados por kilometraje")
st.header("Proyecto 6") 

#Creacion del boton para construir el histograma
hist_button = st.button("Construir histograma")
hist_scat = st.button("Construir un diagrama de dispersion")

#Creacion del boton de verificacion 
build_hist = st.checkbox("Construir un histograma")
build_scat = st.checkbox("Construir un diagrama de dispersion")


#Configuracion del boton "Construir histograma"
if hist_button:
    
    #Mensaje al presionar el boton
    st.write("Creacion de un histograma para el conjunto de datos de anuncio de ventas de coche") 
    
    #Crear un histograma
    fig = px.histogram(car_data, x = "odometer")
    
    #Se muestra un grafico plotly interactivo
    st.plotly_chart(fig, use_conteiner_width=True)
    
    
#Configuracion del boton "Construir un diagrama de dispersion"
elif hist_scat:
    
    #Mensaje al presionar el boton
    st.write("Creacion de un diagrama de dispersion para el conjunto de datos de anuncio de ventas de coche") 
    
    #Crear un diagrama de dispersion
    fig_2 = px.scatter(car_data, x = "odometer", y = "price")
    
    #Se muestra un grafico plotly interactivo
    st.plotly_chart(fig_2, use_conteiner_width=True)
    
    
#Configuracion de la casilla "Construir un histograma"    
elif build_hist:
    
    #Mensaje al presionar el boton
    st.write("Creacion de un diagrama de dispersion para el conjunto de datos de anuncio de ventas de coche") 
    
    #Crear un histograma
    fig_3 = px.histogram(car_data, x = "odometer")
    
    #Se muestra un grafico plotly interactivo
    st.plotly_chart(fig_3, use_conteiner_width=True)
    
#Configuracion de la casilla "Construir un diagrama de dispersion"    
elif build_scat:
    
    #Mensaje al presionar el boton
    st.write("Creacion de un diagrama de dispersion para el conjunto de datos de anuncio de ventas de coche") 
    
    #Crear un diagrama de dispersion
    fig_4 = px.scatter(car_data, x = "odometer", y = "price")
    
    #Se muestra un grafico plotly interactivo
    st.plotly_chart(fig_4, use_conteiner_width=True)
    




    



