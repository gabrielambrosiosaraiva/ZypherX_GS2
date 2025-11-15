from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Carrega os modelos treinados
modelo_classificacao = joblib.load("modelo_classificacao_gs2.pkl")
modelo_regressao = joblib.load("modelo_regressao_salario.pkl")

@app.get("/")
def root():
    return {"status": "OK", "message": "API da ZYPHERX rodando"}

@app.post("/classificar")
def classificar(dados: dict):
    df = pd.DataFrame([dados])
    pred = modelo_classificacao.predict(df)[0]
    prob = modelo_classificacao.predict_proba(df)[0]

    return {
        "previsao": pred,
        "probabilidades": {
            classe: float(p)
            for classe, p in zip(modelo_classificacao.classes_, prob)
        }
    }

@app.post("/prever_salario")
def prever_salario(dados: dict):
    df = pd.DataFrame([dados])
    pred = modelo_regressao.predict(df)[0]

    return {
        "salario_estimado": float(pred)
    }