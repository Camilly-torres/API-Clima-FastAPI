======================================================================
ETAPA 1.1
======================================================================
[ Cliente (Navegador/User) ]
│
│ 1. Faz requisição HTTP GET para http://127.0.0
▼
[ Servidor Uvicorn ]
│
│ 2. Recebe a requisição e encaminha para o App FastAPI
▼
[ App FastAPI ]
│
│ 3. Identifica a rota "/status" e o método "GET"
▼
[ Função Python Local ] ──► 4. Executa e retorna um Dicionário nativo
│
▼
[ App FastAPI ] ──► 5. Converte o Dicionário automaticamente em JSON
│
▼
[ Cliente (Navegador/User) ] ◄── 6. Recebe o JSON com Status 200 OK

IMPORTAR o módulo FastAPI de dentro do pacote fastapi

CRIAR uma variável chamada 'app' que recebe a instância do FastAPI()

CRIAR um decorador do tipo GET mapeando o caminho "/status"
DECLARAR uma função logo abaixo do decorador chamada 'verificar_status'
RETORNAR um dicionário contendo a chave "status" com o valor "operacional"

📖 Conceitos-Chave da Parte
1.1Para construir essa engrenagem, você precisa entender três pilares:
A) Instanciação (app = FastAPI())O que é: É o coração do seu projeto. Quando você instancia essa classe, você está criando o objeto principal da sua aplicação web. É ele quem vai centralizar todas as rotas, configurações de segurança e inicializações que o seu sistema precisa para existir.
B) Decoradores de Rota (Operações de Caminho)O que é: No Python, decoradores são aquelas palavras que começam com @ e ficam em cima de uma função. No FastAPI, eles servem para dizer ao servidor: "Quando um usuário acessar o endereço X usando o método HTTP Y, execute a função que está logo aqui embaixo".Os termos técnicos: O FastAPI chama isso de Path Operation (Operação de Caminho). O "Caminho" é a URL (ex: /status) e a "Operação" é o verbo HTTP usado (ex: GET para buscar dados, POST para criar).
C) O Servidor ASGI (Uvicorn)O que é: O FastAPI por si só é apenas o código da aplicação, ele não sabe escutar a internet sozinho. O Uvicorn é o servidor de alta performance que serve de "porteiro". Ele fica escutando uma porta do seu computador (geralmente a 8000). Quando chega uma requisição da internet, o Uvicorn traduz essa requisição e entrega para o seu código FastAPI processar.

======================================================================
ETAPA 1.2
======================================================================
[ Cliente (Navegador ou Docs) ]
               │
               │ 1. Faz requisição HTTP GET para /clima ou /cidades
               ▼
      [ Servidor Uvicorn ]
               │
               │ 2. Encaminha a requisição para o App FastAPI
               ▼
        [ App FastAPI ]
               │
               │ 3. Identifica a rota e executa a função correspondente
               ▼
  [ BANCO_MEMORIA (Lista Global) ] ──► 4. Lê os dicionários salvos na memória
               │
               ▼
        [ App FastAPI ] ──► 5. Filtra/Estrutura os dados e valida contra o ClimaSchema
               │
               ▼
[ Cliente (Navegador ou Docs) ] ◄── 6. Recebe o JSON formatado com Status 200 OK


No bloco de IMPORTS (topo do arquivo):
    IMPORTAR a classe BaseModel de dentro do módulo pydantic

No meio do arquivo (abaixo de app = FastAPI()):
    CRIAR uma classe chamada 'ClimaSchema' que herda de BaseModel:
        DEFINIR 'id' como número inteiro (int)
        DEFINIR 'cidade' como texto (str)
        DEFINIR 'temperatura' como número decimal (float)
        DEFINIR 'velocidade_vento' como número decimal (float)
        DEFINIR 'condicao_clima' como texto (str)

    CRIAR uma variável global chamada 'BANCO_MEMORIA' que é uma LISTA ([])
    DENTRO dessa lista, coloque 2 ou 3 dicionários manuais. Exemplo de estrutura de 1 item:
        { "id": 1, "cidade": "São Paulo", "temperatura": 22.5, "velocidade_vento": 12.3, "condicao_clima": "Céu Limpo" }

No final do arquivo (abaixo das rotas antigas):
    CRIAR um decorador do tipo GET mapeando o caminho "/clima"
    DECLARAR a função 'listar_todos_os_climas' logo abaixo:
        RETORNAR a variável 'BANCO_MEMORIA'

    CRIAR um decorador do tipo GET mapeando o caminho "/cidades"
    DECLARAR a função 'listar_cidades_cadastradas' logo abaixo:
        CRIAR uma lista vazia chamada 'lista_cidades'
        PARA CADA 'registro' dentro de 'BANCO_MEMORIA':
            ADICIONAR o valor da chave 'cidade' para dentro de 'lista_cidades'
        RETORNAR a 'lista_cidades'


💡 Dicas e Conceitos para te ajudar a programar
1. Como uma classe herda de outra em Python?Para fazer o seu ClimaSchema herdar de BaseModel, você coloca o nome da classe pai entre parênteses logo após o nome da sua classe.
Dica visual: class MinhaClasse(ClassePai):
2. Como funciona a tipagem (Type Hints) no Pydantic?Dentro da classe, você não usa o sinal de igual (=) para definir as variáveis comuns, você usa dois pontos (:) para dizer o tipo dela.Dica visual: nome_do_campo: tipo_de_dado
3. Evitando cidades duplicadas na rota /cidades (Opcional, mas elegante)Se o seu banco de memória tiver três registros de "São Paulo", a sua rota /cidades vai retornar ["São Paulo", "São Paulo", "São Paulo"].Dica de Python: Antes de adicionar a cidade na lista usando o .append(), você pode usar um if para checar se ela já não está lá dentro, ou então pesquisar sobre a estrutura set() do Python, que remove duplicadas automaticamente.
🔍 Onde olhar na Documentação Oficial do FastAPI?
Para ver a sintaxe exata de como escrever esses passos, consulte as seguintes páginas do site oficial: Sintaxe do Pydantic: No menu esquerdo, vá em Tutorial - User Guide > Request Body. Olhe apenas as primeiras linhas do exemplo técnico. Elas mostram exatamente como importar o BaseModel e como declarar os campos com : e seus respectivos tipos.
Retornando Listas: No menu esquerdo, vá em Tutorial - User Guide > Response Model - Return Type. Lá você verá exemplos de funções retornando listas de dados comuns e como o FastAPI lida com isso.

======================================================================
ETAPA 1.3
======================================================================
[ Cliente (Navegador ou Docs) ]
               │
               │ 1. Faz requisição HTTP GET para /clima/São Paulo
               ▼
      [ Servidor Uvicorn ]
               │
               │ 2. Encaminha a requisição e o texto "São Paulo" para o app
               ▼
        [ App FastAPI ]
               │
               │ 3. Identifica a rota e injeta o texto na função como argumento
               ▼
  [ BANCO_MEMORIA (Lista Global) ] ──► 4. Varre a lista procurando a chave "cidade"
               │
    ┌──────────┴──────────┐
    │                     │
[ Encontrou? SIM ]    [ Encontrou? NÃO ]
    │                     │
    ▼                     ▼
Retorna o dicionário   Dispara HTTPException
da cidade (Status 200) com Status 404 (Not Found)


No bloco de IMPORTS (topo do arquivo):
    Adicionar a classe HTTPException ao lado do FastAPI (ex: from fastapi import FastAPI, HTTPException)

No final do arquivo (abaixo das rotas antigas):
    CRIAR um decorador do tipo GET mapeando o caminho "/clima/{cidade}"
    
    DECLARAR a função 'buscar_clima_por_cidade' que recebe o argumento 'cidade' (do tipo str):
        
        PARA CADA 'registro' dentro de 'BANCO_MEMORIA':
            
            SE o valor de registro["cidade"] convertido para MINÚSCULO for IGUAL ao argumento 'cidade' convertido para MINÚSCULO:
                RETORNAR o 'registro' atual
                
        SE o loop terminar e não encontrar nada:
            DISPARAR (raise) um erro HTTPException com o status_code=404 e detail="Cidade não encontrada"

💡 Dicas e Conceitos para te ajudar a programar
1. Como colocar variáveis na rota do FastAPI?Quando você usa chaves dentro do texto do decorador (ex: "/clima/{cidade}"), você está dizendo ao FastAPI que aquela parte do endereço é dinâmica. Para capturar esse valor, a sua função Python logo abaixo precisa receber um parâmetro com o exato mesmo nome e sua tipagem.Dica visual: def minha_funcao(cidade: str):
2. Por que converter para minúsculo (.lower())?Se o usuário digitar /clima/são paulo (tudo minúsculo) e no seu banco estiver "São Paulo" (com maiúsculas), o Python dirá que são textos diferentes. Usar o método .lower() do Python nos dois lados da comparação faz com que a busca ignore letras maiúsculas ou minúsculas.Dica de Python: texto.lower()
3. O que é a HTTPException?Em APIs, não podemos apenas retornar um texto comum como "Erro" se algo der errado. Precisamos responder usando os padrões da internet (Códigos HTTP). A HTTPException serve para interromper o código na hora e enviar um código de erro oficial para o navegador (o código 404 é o padrão mundial para "Não Encontrado").
🔍 Onde olhar na Documentação Oficial do FastAPI?
Para ver a sintaxe exata de como estruturar essa rota, consulte o site oficial:No menu esquerdo, vá em Tutorial - User Guide > Path Parameters (Parâmetros de Caminho).Lá você verá o exemplo exato de como colocar o {item_id} na rota e como recebê-lo na função.
Para ver como disparar o erro 404 corretamente, vá em Tutorial - User Guide > Handling Errors (Tratamento de Erros) e veja as primeiras duas linhas de exemplo de como usar o raise HTTPException.

======================================================================
ETAPA 1.4
======================================================================
[ Cliente (Swagger/Docs) ] ──► 1. Envia dados novos via HTTP POST /clima
               │
               ▼
        [ App FastAPI ] ──► 2. Recebe o JSON e valida contra o 'ClimaSchema'
               │
    ┌──────────┴──────────┐
[ Dados Inválidos? ]  [ Dados Válidos? ]
    │                     │
    ▼                     ▼
Retorna Erro 422      3. Executa a função 'adicionar_clima'
(Automatico)          4. Converte o schema em dicionário comum
                      5. Dá um .append() na lista 'BANCO_MEMORIA'
                      6. Retorna o item criado com Status 201 (Created)

======================================================================
1. ROTA POST (Adicionar registro)
======================================================================
CRIAR um decorador do tipo POST mapeando o caminho "/clima" e definindo status_code=201

DECLARAR a função 'adicionar_clima' que recebe um parâmetro chamado 'novo_clima' (do tipo ClimaSchema):
    CONVERTER o objeto 'novo_clima' em um dicionário comum do Python (usando o método .model_dump())
    ADICIONAR esse novo dicionário para dentro da lista 'BANCO_MEMORIA' usando .append()
    RETORNAR o dicionário que acabou de ser adicionado

======================================================================
2. ROTA PUT (Atualizar registro por ID)
======================================================================
CRIAR um decorador do tipo PUT mapeando o caminho "/clima/{clima_id}"

DECLARAR a função 'atualizar_clima' que recebe 'clima_id' (int) e 'clima_atualizado' (ClimaSchema):
    PARA CADA 'registro' dentro de 'BANCO_MEMORIA':
        SE o registro["id"] for IGUAL ao 'clima_id' recebido:
            ATUALIZAR as chaves do 'registro' com os novos valores de 'clima_atualizado.model_dump()'
            RETORNAR o 'registro' atualizado
            
    SE o loop terminar e não encontrar o ID:
        DISPARAR erro HTTPException 404 "Registro não encontrado"

======================================================================
3. ROTA DELETE (Remover registro por ID)
======================================================================
CRIAR um decorador do tipo DELETE mapeando o caminho "/clima/{clima_id}"

DECLARAR a função 'deletar_clima' que recebe 'clima_id' (int):
    PARA CADA 'registro' dentro de 'BANCO_MEMORIA':
        SE o registro["id"] for IGUAL ao 'clima_id' recebido:
            REMOVER o 'registro' de dentro da lista 'BANCO_MEMORIA' (usando o método .remove())
            RETORNAR um dicionário de sucesso (Ex: {"mensagem": "Removido com sucesso"})
            
    SE o loop terminar e não encontrar o ID:
        DISPARAR erro HTTPException 404 "Registro não encontrado"

💡 Dicas e Conceitos para te ajudar a programar
1. Como o FastAPI sabe o que validar no POST?Repare que na função do POST, você vai declarar novo_clima: ClimaSchema. Só de fazer isso, o FastAPI entende que o usuário é obrigado a enviar um corpo de requisição (JSON) contendo exatamente os campos do Pydantic. Se o usuário esquecer um campo ou enviar o tipo errado, o FastAPI barra a requisição sozinho antes de entrar na sua função!
2. O que é o .model_dump()?O novo_clima chega na sua função como um objeto especial do Pydantic. Para conseguir salvá-lo na nossa lista atual (que é feita de dicionários comuns do Python), nós precisamos convertê-lo. O método .model_dump() faz exatamente isso: transforma o objeto Pydantic em um dicionário {} comum do Python.
3. Mudando o Status de Sucesso do POST (Status 201)Por padrão, toda rota do FastAPI retorna o status 200 OK quando dá certo. Mas na internet, a regra para criação de registros novos é retornar o status 201 Created. Você pode configurar isso direto no decorador.Dica visual: @app.post("/caminho", status_code=201)
🔍 Onde olhar na Documentação Oficial do FastAPI?
Para fazer o POST: Vá em Tutorial - User Guide > Request Body. Veja como a função recebe o modelo e como ela usa os dados.
Para mudar o status para 201: Vá em Tutorial - User Guide > Response Status Code. Lá mostra exatamente como colocar o status_code=201 dentro do decorador @app.post.