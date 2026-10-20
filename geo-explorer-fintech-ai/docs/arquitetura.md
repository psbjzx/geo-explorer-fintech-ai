# Arquitetura Técnica do Geo-Explorer

## Visão Geral
O projeto adota uma arquitetura desacoplada em camadas para garantir que a mesma regra de negócio atenda tanto usuários humanos (via CLI) quanto agentes de Inteligência Artificial (via Servidor MCP).

## Fluxo de Componentes
1. **`data/trilhas.json`**: Camada de persistência leve contendo o catálogo de trilhas, módulos, desafios categorizados por senioridade e dicas técnicas.
2. **`src/commands.py`**: Camada de domínio (Core). Contém funções puras, validações de entrada e geração de hash criptográfico (`SHA-256`) para autenticação dos certificados.
3. **`src/cli.py`**: Interface de linha de comando construída com `argparse`.
4. **`src/mcp_server.py`**: Servidor compatível com o **Model Context Protocol (MCP)** usando `FastMCP`, permitindo que assistentes como o **IBM Bob** invoquem as funções do projeto como ferramentas (*Tools*).
5. **`tests/test_commands.py`**: Suíte de testes unitários com `unittest` garantindo cobertura de caminhos felizes e tratamento de exceções.
