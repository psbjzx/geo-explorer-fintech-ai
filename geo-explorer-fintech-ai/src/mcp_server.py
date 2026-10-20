from mcp.server.fastmcp import FastMCP
from src.commands import listar_trilhas, consultar_trilha, gerar_desafio, emitir_certificado

mcp = FastMCP("Geo-Explorer-FinTech-AI")


@mcp.tool()
def catalogo_trilhas() -> str:
    """Lista todas as trilhas de aprendizagem disponíveis no Geo-Explorer."""
    return listar_trilhas()


@mcp.tool()
def obter_plano_estudos(tecnologia: str) -> str:
    """Retorna os módulos e carga horária de uma tecnologia (dados, python, devsecops, ia_generativa)."""
    return consultar_trilha(tecnologia)


@mcp.tool()
def obter_desafio_codigo(tecnologia: str, nivel: str, exibir_dica: bool = True) -> str:
    """Gera um desafio técnico para a tecnologia e nível (iniciante, intermediario, avancado)."""
    return gerar_desafio(tecnologia, nivel, exibir_dica)


@mcp.tool()
def gerar_certificado_conclusao(nome_usuario: str, tecnologia: str) -> str:
    """Emite um certificado fictício autenticado com hash para uma trilha concluída."""
    return emitir_certificado(nome_usuario, tecnologia)


if __name__ == "__main__":
    mcp.run()
