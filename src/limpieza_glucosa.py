import pandas as pd 

def limpiar_glucosa(df):

    print("Datos originales:",df.shape)

    df = df.drop_duplicates()

    for col in df.columns:
        df[col] = pd.to_numeric(df[col],errors="coerce")

    print("\n Nulos por columna:")
    print(df.isnull().sum())

    if "Edad" in df.columns:
        df["Edad"] = df["Edad"].fillna(df["Edad"].mean())

    if "Actividad_Fisica" in df.columns:
        df["Actividad_Fisica"] = df["Actividad_Fisica"].fillna(df["Actividad_Fisica"])

    if "Nivel_Glucosa" in df.columns:
        df = df.dropna(subset=["Nivel_Glucosa"])

    print("\n Datos después de limpieza:",df.shape)

    return df 