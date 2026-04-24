import pandas as pd 
import joblib

from src.limpieza_dolar import limpiar_dolar
from src.limpieza_glucosa import limpiar_glucosa
from src.limpieza_energia import limpiar_energia
from src.modelos import entrenar_modelo

print("Seleccione dataset:")
print("1. Dólar")
print("2. Glucosa")
print("3. Energía")

opcion = input("Ingrese opción: ")

if opcion == "1":
    df = pd.read_csv("data/raw/dolar_data.csv")

    df = limpiar_dolar(df)

    df.to_csv("data/processed/dolar_data_limpio.csv",index=False)

    x = df[["Dia","Inflacion","Tasa_interes"]]
    y = df["Precio_Dolar"]

    model = entrenar_modelo(x,y)

    joblib.dump(model,"models/modelo_dolar.pkl")

    print("Modelo dólar listo")

elif opcion == "2":
    df = pd.read_csv("data/raw/glucosa_data.csv")

    df = limpiar_glucosa(df)

    df.to_csv("data/processed/glucosa_data_limpio.csv",index=False)
    
    x = df[["Edad","IMC","Actividad_Fisica"]]
    y = df["Nivel_Glucosa"]

    model = entrenar_modelo(x,y)

    joblib.dump(model,"models/modelo_glucosa.pkl")

    print("Modelo glucosa listo")

elif opcion == "3":
    df = pd.read_csv("data/raw/energia_data.csv")

    df = limpiar_glucosa(df)

    df.to_csv("data/processed/energia_data_limpio.csv",index=False)
    
    x = df[["Temperatura","Hora","Dia_Semana"]]
    y = df["Consumo_Energia"]

    model = entrenar_modelo(x,y)

    joblib.dump(model,"models/modelo_energia.pkl")

    print("Modelo energia listo")

else:
    print("Opción inválida")