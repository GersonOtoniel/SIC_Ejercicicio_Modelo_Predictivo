import streamlit as st
import pandas as pd
import joblib
import json



st.title("Modelo predictivo de precios de automoviles")

pipeline = joblib.load("model_cars.pkl")
with open("metricas.json") as f:
    metricas = json.load(f)

st.subheader("Desempeño del modelo")
st.write(f"Error Absoluto Medio (MAE): {metricas['mae']:.2f}")
st.write(f"Raíz del Error Cuadrático Medio (RMSE): {metricas['rmse']:.2f}")
st.write(f"Coeficiente de Determinación (R²): {metricas['r2']:.22f}")

url = "https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv"
df = pd.read_csv(url)
df = df.dropna(subset=['Price'])
df = df.drop(columns=['Make'])

st.subheader("Haga una predicción")
manufacturados = sorted(df['Manufacturer'].dropna().unique())
tipos = sorted(df['Type'].dropna().unique())
origenes = sorted(df['Origin'].dropna().unique())

manufacturer = st.selectbox("Fabricante", manufacturados)
modelo_auto = st.text_input("Modelo del automóvil", "Model X")
tipo = st.selectbox("Tipo de automóvil", tipos)
origen = st.selectbox("Origen", origenes)
mpg_city = st.slider("MPG ciudad", 10, 50, 25)
mpg_high = st.slider("MPG carretera", 15, 60, 30)
horsepower = st.slider("Caballos de fuerza", 50, 300, 150)
weight = st.slider("Peso (lbs)", 1500, 5000, 3000)
engine_size = st.slider("Tamaño de motor (L)", 1.0, 6.0, 2.5)

input_data = pd.DataFrame([{
    "Manufacturer": manufacturer,
    "Model": modelo_auto,
    "Type": tipo,
    "Origin": origen,
    "MPG.city": mpg_city,
    "MPG.highway": mpg_high,
    "Horsepower": horsepower,
    "Weight": weight,
    "EngineSize": engine_size
}])

if st.button("Predecir precio"):
    pred = pipeline.predict(input_data)[0]
    st.success(f"💲 Precio estimado: **${pred:.2f}K**")
