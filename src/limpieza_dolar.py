import pandas as pd 

def limpiar_dolar(df):

    print("Datos originales:",df.shape)

    df = df.drop_duplicates()

    for col in df.columns:
        df[col] = pd.to_numeric(df[col],errors="coerce")

    print("\n Nulos por columna:")
    print(df.isnull().sum())

    if "Inflacion" in df.columns: 
        df["Inflacion"] = df["Inflacion"].fillna(df["Inflacion"].mean())

    if "Tasa_interes" in df.columns:
        df["Tasa_interes"] = df["Tasa_interes"].fillna(df["Tasa_interes"].mean())

    if "Dia" in df.columns:
        df["Dia"] = df["Dia"].ffill()

    if "Precio_Dolar" in df.columns:
        df = df.dropna(subset=["Precio_Dolar"])

    if "Nivel_Glucosa" in df.columns:
        df = df.dropna(subset=["Nivel_Glucosa"])

    if "Consumo Energia" in df.columns:
        df = df.dropna(subset=["Nivel_Glucosa"])

    print("\n Datos después de limpieza: ",df.shape)

    return df