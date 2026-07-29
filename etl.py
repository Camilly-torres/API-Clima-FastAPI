from datetime import datetime
import pandas as pd
import requests
from sqlalchemy import create_engine


def ExtrairDadosClimaticos():
    cidades = {
        "São Paulo": {"lat": -23.55, "lon": -46.63},
        "Rio de Janeiro": {"lat": -22.90, "lon": -43.17}
        }

    lista_final = []

    for nome_cidade, coordenadas in cidades.items():
        texto_url = f"https://open-meteo.com{coordenadas['lat']}&longitude={coordenadas['lon']}&current_weather=true"

        
        try:
            response = requests.get(texto_url, timeout=10)
            response.raise_for_status()  
            dados_brutos = response.json()

            
            dados_clima = dados_brutos["current_weather"]
            dados_clima["Nome_cidade"] = nome_cidade
            lista_final.append(dados_clima)

        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao extrair dados de {nome_cidade}: {e}")
            continue  

    
    if not lista_final:
        print("⚠️ Nenhum dado foi extraído.")
        return pd.DataFrame()

    df_final = pd.DataFrame(lista_final)
    return df_final


def TransformarDadosClimatico(df_bruto):
    if df_bruto.empty:
        return df_bruto

   
    df_bruto.rename(
        columns={
            "temperature": "temperatura",
            "windspeed": "velocidade_vento",
            "weathercode": "codigo_clima",
            "time": "data_hora",
            "Nome_cidade": "cidade",  
        },
        inplace=True,
    )

    
    df_bruto["data_hora"] = pd.to_datetime(df_bruto["data_hora"])

    dicionario_clima = {
        0: "Céu Limpo",
        1: "Parcialmente Nublado",
        2: "Nublado",
        3: "Encoberto",
        61: "Chuva Leve",
        63: "Chuva Moderada",
    }

    
    df_bruto["condicao_clima"] = df_bruto["codigo_clima"].map(dicionario_clima)
  
    df_bruto["condicao_clima"].fillna("Outros", inplace=True)

    df_bruto["processado_em"] = datetime.now()

    
    lista_arrumada = [
        "cidade",
        "temperatura",
        "velocidade_vento",
        "condicao_clima",
        "data_hora",
        "processado_em",
    ]
    return df_bruto[lista_arrumada]


def carregar_dados(df):
    if df.empty:
        print("⚠️ DataFrame vazio. Carga cancelada.")
        return

   
    USER = "postgres"
    PASSWORD = "sua_senha_aqui"
    HOST = "localhost"
    PORT = "5432"
    DB_NAME = "meu_banco_etl"

    engine = create_engine(
        f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    )

    try:

        df.to_sql("historico_clima", engine, if_exists="append", index=False)
        print("🚀 Dados carregados com sucesso no PostgreSQL!")
    except Exception as e:
        print(f"❌ Erro ao carregar dados no banco: {e}")


if __name__ == "__main__":
    df_bruto = ExtrairDadosClimaticos()
    df_tratado = TransformarDadosClimatico(df_bruto)
    carregar_dados(df_tratado)
