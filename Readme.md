# Ejericio por parte de la beca de Samsung Innovation Campus

# ¿Qué hace el código del proyecto?

Este código crea una aplicación con **Streamlit** que:

### ✔ Carga un dataset de automóviles  
Datos reales con precios, marca, motor, peso, etc.

### ✔ Preprocesa los datos  
- Imputación de valores faltantes  
- Escalado estandarizado  
- Codificación One-Hot para texto  
- Selección de columnas relevantes  

### ✔ Entrena automáticamente un modelo  
Usa un **RandomForestRegressor** para predecir el precio de un auto.

### ✔ Evalúa su desempeño  
Muestra métricas como:
- MAE  
- RMSE  
- R²  

### ✔ Permite hacer predicciones  
El usuario ingresa características del carro y el modelo predice su precio.

Todo esto corre dentro del entorno virtual, para garantizar que Streamlit, scikit-learn y pandas funcionen sin errores.

---


## Uso del entorno virtual y ejecución de la aplicación

Este documento explica cómo crear, activar, ejecutar, detener y desactivar un entorno virtual en Python, así como cómo correr la aplicación.

---

## 1. Crear el entorno virtual (venv)

Si aún no existe un entorno virtual, créalo con:

```
python -m venv venv
```

Esto generará una carpeta llamada `venv` que contiene Python y todas las dependencias aisladas del sistema.

---

## 2. Activar el entorno virtual

### En Windows:
```
venv\Scripts\activate
```

### En macOS / Linux:

```
source venv/bin/activate
```

Cuando está activo, verás algo como:

```
(venv) C:\ruta\del\proyecto>
```


---

## 3. Instalar dependencias

Con el entorno activo, ejecuta:

```
pip install -r requirements.txt
```


---

## 4. Ejecutar la aplicación

### Aplicación con Streamlit:

```
streamlit run app.py
```


(O reemplaza `app.py` por el archivo correspondiente.)

---

## 5. Detener la aplicación

Si la aplicación está ejecutándose en la terminal, deténla con:

```bash
CTRL + C
```

---

## 6. Desactivar el entorno virtual

Para salir del entorno virtual:

```bash
deactivate
```


---

## 7. (Opcional) Eliminar el entorno virtual

### Windows:

```
rmdir /s /q venv
```


### macOS / Linux:

```
rm -r venv
```

---

## Resumen rápido

| Acción | Comando |
|--------|---------|
| Crear venv | `python -m venv venv` |
| Activar venv | `venv\Scripts\activate` |
| Instalar dependencias | `pip install -r requirements.txt` |
| Ejecutar app | `streamlit run app.py` |
| Detener app | `CTRL + C` |
| Desactivar venv | `deactivate` |

