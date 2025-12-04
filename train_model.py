import pandas as pd
import numpy as np
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor



url = "https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv"
df = pd.read_csv(url)
columnas_utiles = [
    "Manufacturer", "Model", "Type", "Origin",
    "MPG.city", "MPG.highway", "Horsepower", "Weight", "EngineSize"
]
df = df.dropna(subset=['Price'])
df = df.drop(columns=["Make"])
df = df[columnas_utiles + ["Price"]]

#st.title("Modelo predictivo de precios de automóviles")
#st.write("Este modelo se entrena automáticamente cada vez que se ejecuta la app.")

y = df["Price"]
X = df.drop(columns=["Price"])

caracteristicas_numericas = X.select_dtypes(include=['int64', 'float64']).columns
caracteristicas_categoricas = X.select_dtypes(include=['object']).columns


transformacion_numerica = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),  
    ('scaler', StandardScaler())
])

transformacion_categorica = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')), 
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', transformacion_numerica, caracteristicas_numericas),
        ('cat', transformacion_categorica, caracteristicas_categoricas)
    ]
)

# Aqui se entrena el modeo
modelo = RandomForestRegressor(n_estimators=350, random_state=42, max_depth=10)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', modelo)
])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

metricas = {
    "mae": mae,
    "rmse": rmse,
    "r2": r2
}

with open("metricas.json", "w") as f:
    json.dump(metricas, f)

pipeline.fit(X, y)

joblib.dump(pipeline, "model_cars.pkl")
print("Modelo entrenado y metricas guardadas")