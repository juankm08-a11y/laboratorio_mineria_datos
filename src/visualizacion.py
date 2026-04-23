import seaborn as sns 
import matplotlib.pyplot as plt 

def graficar_relaciones(df,x_cols,y_col):
    for col in x_cols:
        sns.scatterplot(x=df[col],y=df[col])
        plt.title(f"{col} vs {y_col}")
        plt.show()