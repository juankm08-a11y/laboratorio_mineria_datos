import pandas as pd 
from src.limpieza import limpiar_datos
from src.modelos import entrenar_modelo
import joblib

df = pd.read_csv("data/raw/dolar_data.csv")

df = limpiar_datos(df)

print("Datos después de limpieza:",df.shape)

df.to_csv("data/processed/dolar_data_limpio.csv",index=False)
print("Dataset limpio guardado en dataset/processed")

columnas = ["Dia","Inflacion","Tasa_interes","Precio_Dolar"]
for col in columnas:
    if col not in df.columns:
        raise ValueError(f"Falta la columna {col}")
    
x = df[["Dia","Inflacion","Tasa_interes"]]
y = df["Precio_Dolar"]

model = entrenar_modelo(x,y)

joblib.dump(model,"models/modelo_dolar.pkl")

print("Modelo entrenado y guardado correctamente")

