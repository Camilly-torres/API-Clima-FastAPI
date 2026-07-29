# 🌦️ API Clima - FastAPI

Projeto desenvolvido para estudo de desenvolvimento de APIs REST utilizando **FastAPI**, consumo de APIs externas e manipulação de dados em Python.

A aplicação realiza a consulta de dados meteorológicos utilizando a API pública **Open-Meteo**, processa essas informações e disponibiliza os resultados através de endpoints REST.

---

## 🚀 Objetivos do projeto

Este projeto foi criado com o objetivo de praticar:

- Desenvolvimento de APIs REST
- FastAPI
- Consumo de APIs externas
- ETL (Extract, Transform, Load)
- Organização de projetos Python
- Versionamento com Git e GitHub

Além disso, o projeto continuará evoluindo com novas funcionalidades conforme meus estudos.

---

## 🛠 Tecnologias

- Python
- FastAPI
- Pydantic
- Uvicorn
- Requests
- Open-Meteo API

---

## 📂 Estrutura atual

```
api-clima-fastapi/
│
├── api.py
├── main.py
├── README.md
├── ETAPA1.md
└── ...
```

---

## 🔄 Fluxo da aplicação

```
Cliente
    │
    ▼
FastAPI
    │
    ▼
ETL
    │
    ▼
Open-Meteo
    │
    ▼
Dados tratados
    │
    ▼
Resposta JSON
```

---

## 📌 Funcionalidades

- Consulta de clima
- Consulta por cidade
- Listagem de cidades
- Cadastro de registros
- Atualização de registros
- Documentação automática utilizando Swagger

---

## 📖 Processo de aprendizado

Durante o desenvolvimento deste projeto, cada funcionalidade é planejada utilizando:

- Fluxogramas
- Pseudocódigo
- Documentação oficial do FastAPI
- Estudos incrementais por etapas

A pasta/documento `ETAPA1.md` registra esse processo de aprendizado, reunindo anotações, conceitos e planejamento antes da implementação do código.
```

---

## 📈 Próximas etapas

- [ ] Finalizar endpoint DELETE
- [ ] PostgreSQL
- [ ] SQLAlchemy
- [ ] Docker
- [ ] Testes automatizados
- [ ] Deploy
- [ ] CI/CD

---

## 📚 Motivação

Este projeto faz parte do meu processo de aprendizado em desenvolvimento back-end utilizando Python.

O objetivo é evoluí-lo gradativamente para acompanhar minha evolução técnica e servir como portfólio.