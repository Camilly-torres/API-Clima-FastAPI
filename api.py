from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ClimaSchema(BaseModel):
    id : int
    cidade : str
    temperatura : float
    velocidade_vento : float
    condicao_clima : str

BANCO_MEMORIA = [{ "id": 1, 
                          "cidade": "São Paulo", 
                          "temperatura": 22.5, 
                          "velocidade_vento": 12.3, 
                          "condicao_clima": "Céu Limpo" 
                         }]

@app.get("/clima")
def listar_todos_climas():
    return BANCO_MEMORIA

@app.get("/cidades")
def listar_cidades_cadastradas():
    lista_cidades = []
    
    for registro in BANCO_MEMORIA:
        nome_cidade = registro["cidade"]
        lista_cidades.append(nome_cidade)
    
    return list(set(lista_cidades))   
         

@app.get('/status')
def verificar_status():
    dict = {
        "status" : "operacional"}
    
    return  dict

@app.get("/clima/{cidade}")
def buscar_clima_por_cidade(cidade: str):
    
    for registro in BANCO_MEMORIA:
        if registro["cidade"].lower() == cidade.lower():
            return registro
            
        
    raise HTTPException(status_code=404, detail="Cidade não encontrada")

@app.post("/clima",status_code=201)
def adicionar_clima(novo_clima:ClimaSchema):
   dicionario_clima =  novo_clima.model_dump()
   BANCO_MEMORIA.append(dicionario_clima)
   return dicionario_clima

@app.put("/clima/{clima_id}")
def atualizar_clima(clima_id:int, clima_atualizado:ClimaSchema):
    for registro in BANCO_MEMORIA:
        if registro["id"] == clima_id:
            registro.update(clima_atualizado.model_dump())
    
        return registro     
    raise HTTPException(status_code=404, detail="Registro não encontrado")
   
    
    

