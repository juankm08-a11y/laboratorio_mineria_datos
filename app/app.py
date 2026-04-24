import streamlit as st 
import joblib
import pandas as pd 

st.title("Predicciones de Minería de Datos")

opcion = st.selectbox("Seleccione modelo", ["Dólar","Glucosa","Energía"])

st.info("Ingrese los datos para la predicción")

st.markdown("""

<style>
.main {
    background-color:#F8FAFC;
}
h1 {
    color:#1E3A8A;
    text-align:center;
}
.stButton > button {
    background-color:#2563EB;
    color:white;
    border-radius:8px;
    padding:10px
}
.stButton > button:hover {
    background-color:#1D4ED8;
}

[data-testid="stNumberInput"] input {
    border-radius:6px;
}
            
[data-testid="stAlert"] {
    border-radius:10px;
}
</style>
""",unsafe_allow_html=True)
if opcion == "Dólar":
    model = joblib.load("models/modelo_dolar.pkl")

    with st.container():
        dia = st.number_input("Día",min_value=1,step=1)
        inflacion = st.number_input("Inflación",format="%.4f")
        tasa = st.number_input("Tasa interés",format="%.2f")

    if st.button("Predecir Dólar"):
        data = pd.DataFrame(
            [[dia,inflacion,tasa]],
            columns=["Dia","Inflacion","Tasa_interes"]
        )
        pred = model.predict(data)
        st.success(f"Precio dólar: {pred[0]:.2f}")


elif opcion == "Glucosa":
    model = joblib.load("models/modelo_glucosa.pkl")

    with st.container():
        edad = st.number_input("Edad",min_value=1,step=1)
        imc = st.number_input("IMC",format="%.2f")
        actividad = st.number_input("Actividad física",min_value=0,step=1)

    if st.button("Predecir Glucosa"):

        if edad == 0 and imc == 0 and actividad == 0:
            st.warning("Por favor ingrese valores válidos")
        else: 
            data = pd.DataFrame(
                [[edad,imc,actividad]],
                columns=["Edad","IMC","Actividad_Fisica"]
            )
            pred = model.predict(data)
            st.success(f"Nivel glucosa: {pred[0]:.2f}")

else:
    model = joblib.load("models/modelo_energia.pkl")

    with st.container():
        temp = st.number_input("Temperatura",format="%.2f")
        hora = st.number_input("Hora",min_value=0,step=1)
        dia = st.number_input("Día semana",min_value=1,step=1)

    if st.button("Predecir Energía"):

        if temp == 0 and hora == 0 and dia == 0:
            st.warning("Por favor ingrese valores válidos")
        else:
            data = pd.DataFrame(
                [[temp,hora,dia]],
                columns=["Temperatura","Hora","Dia_Semana"]
            )
            pred = model.predict(data)
            st.success(f"Consumo energía: {pred[0]:.2f}")

