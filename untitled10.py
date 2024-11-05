# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ANxMVyiZYPhA8hC2cqhGPCoPLnXcH1ah
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
[theme]
backgroundColor = "#F0F0F0"

st.sidebar.title("Steam Verde")
st.sidebar.header("Bienvenido a Steam Verde ")
st.sidebar.image("OIP.jpg")
st.sidebar.text_input("Ingresa El Nombre del Juego que buscas ")
st.title("Steam Verde")
st.write("Galeria De Juegos")

#Juego_1
st.title("Forza Horizon 4")
st.image("Horizon.jpg")
st.write("Especificaciones")
st.write( "SO: Windows 10 versión 15063.0 o superior")
st.write("Procesador: Intel i7-3820 @ 3.6Ghz")
st.write("Memoria: 8 GB de RAM")
st.write("Gráficos: NVidia GTX 970 o NVidia GTX 1060 3GB o AMD R9 290x o AMD RX 470")
st.write("Almacenamiento: 100 GB de espacio disponible")
st.button("Descargar aqui")

#Juego_2
st.title("GTA V")
st.image("gtav.jpg")
st.write("Especificaciones")
st.write( "Windows 10 64 Bit, Windows 8.1 64 Bit, Windows 8 64 Bit, Windows 7 64 Bit Service Pack 1")
st.write("Procesador: Intel i7-3820 @ 3.6Ghz")
st.write("Memoria: 8 GB de RAM")
st.write("NVIDIA GTX 660 2GB / AMD HD7870 2GB")
st.write("72 GB available space")
st.button("Descargar aca!")











