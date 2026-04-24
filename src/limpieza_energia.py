import pandas as pd  

def limpiar_energia(df):

    print("Datos originales:",df.shape)

    df = df.drop_duplicates()

    for col in df.columns:
        df[col] = pd.to_numeric(df[col],errors="coerce")

    print("\n Nulos por columna:")
    print(df.isnull().sum())

    if "Temperatura" in df.column:
        df["Temperatura"] = df["Temperatura"].fillna(df["Temperature"].mean())

    if "Hora" in df.columns:
        df["Hora"] = df["Hora"].fillna(df["Hora"].median())

    if "Dia_Semana" in df.columns:
        df["Dia_Semana"] = df["Dia_Semana"].fillna(df["Dia_Semana"].median())

    if "Consumo_Energia" in df.columns:
        df = df.dropna(subset=["Consumo_Energia"])

    print("\n Datos después de limpieza:",df.shape)

    return df