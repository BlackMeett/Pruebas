# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ANxMVyiZYPhA8hC2cqhGPCoPLnXcH1ah
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.markdown("""
<style>
body {
    background-color: #000000;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Steam Verde")
st.sidebar.header("Bienvenido a Steam Verde ")
st.sidebar.image("OIP.jpg")
opcion = st.sidebar.radio("Elige una opción", ("Iniciar sesión", "Crear cuenta"))
if opcion == "Iniciar sesión":
    usuario = st.sidebar.text_input("usuario")
    contraseña = st.sidebar.text_input("Contraseña", type="password")
    boton_logeo = st.sidebar.button("Iniciar Sesiòn")
    if boton_logeo:
        
        if usuario and contraseña:
            st.sidebar.success("¡Inicio de sesión exitoso!")
        else:
            st.sidebar.error("Por favor, ingresa un usuario y una contraseña válidos.")
elif opcion == "Crear cuenta":
    Nombre = st.sidebar.text_input("Ingrese Su Nombre")
    Contraseña_2 = st.sidebar.text_input("Ingrese Su contraseña", type="password")
    confirmar_contraseña = st.sidebar.text_input("Ingresela De Nuevo", type="password")
    boton_crear_cuenta = st.sidebar.button("Crear Cuenta")
    if boton_crear_cuenta:
        if Contraseña_2 == confirmar_contraseña:
            if Nombre == Contraseña_2:
                st.sidebar_success(f"Cuenta creada para  {Nombre}")
            else:
                st.warning("Por favor, ingresa un nombre de usuario y una contraseña.")
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
if st.button("Descargar aqui"):
    st.error("¡ALERTA! Esto puede contener virus")

#Juego_2
st.title("GTA V")
st.image("gtav.jpg")
st.write("Especificaciones")
st.write( "Windows 10 64 Bit, Windows 8.1 64 Bit, Windows 8 64 Bit, Windows 7 64 Bit Service Pack 1")
st.write("Procesador: Intel i7-3820 @ 3.6Ghz")
st.write("Memoria: 8 GB de RAM")
st.write("NVIDIA GTX 660 2GB / AMD HD7870 2GB")
st.write("72 GB available space")
if st.button("Descarga aca!"):
    st.error("¡ALERTA! Esto puede contener virus")











