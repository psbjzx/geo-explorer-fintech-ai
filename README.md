# 🌍 Geo-Explorer: FinTech, Data & AI Sec Edition

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![MCP](https://img.shields.io/badge/Protocol-MCP%20Server-purple)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
![DIO](https://img.shields.io/badge/Desafio-DIO%20%26%20IBM%20Bob-orange)

## 📌 O Que é o Geo-Explorer?

O **Geo-Explorer** é uma solução completa de exploração de trilhas de aprendizagem técnica desenvolvida com o apoio do **IBM Bob**. A aplicação permite consultar planos de estudo estruturados, receber desafios práticos de código calibrados por nível de senioridade e emitir certificados fictícios autenticados.

Além da interface de linha de comando (CLI), o projeto implementa um **Servidor MCP (Model Context Protocol)**, permitindo que agentes de Inteligência Artificial e assistentes de código acessem os recursos do Geo-Explorer diretamente como ferramentas (*Tools*).

---

## 📂 Estrutura do Projeto

```text
geo-explorer-fintech-ai/
├── data/
│   └── trilhas.json          # Base de dados com trilhas, módulos, desafios e dicas
├── src/
│   ├── __init__.py
│   ├── commands.py           # Regras de negócio (Trilha, Desafio, Certificado e Catálogo)
│   ├── cli.py                # Interface de Linha de Comando (CLI)
│   └── mcp_server.py         # Servidor MCP para integração com Agentes de IA
├── tests/
│   └── test_commands.py      # Testes unitários automatizados
├── docs/
│   └── arquitetura.md        # Documentação técnica da arquitetura
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação principal
