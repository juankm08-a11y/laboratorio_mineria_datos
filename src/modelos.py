from sklearn.linear_model import LinearRegression

def entrenar_modelo(x,y):
    model = LinearRegression()
    model.fit(x,y)
    return model 