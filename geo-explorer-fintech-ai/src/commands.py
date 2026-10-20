import json
import hashlib
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "trilhas.json"


def carregar_dados() -> dict:
    """Carrega a base de dados JSON contendo as trilhas."""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def listar_trilhas() -> str:
    """Evolução: Lista todo o catálogo de trilhas disponíveis no sistema."""
    dados = carregar_dados()
    linhas = [
        "============================================================",
        "       🌍 CATÁLOGO DE TRILHAS - GEO-EXPLORER EDITION        ",
        "============================================================"
    ]
    for chave, info in dados.items():
        linhas.append(f"🔹 [{chave.upper()}] {info['nome']} ({info['carga_horaria']}h)")
    linhas.append("============================================================")
    return "\n".join(linhas)


def consultar_trilha(tecnologia: str) -> str:
    """Comando Principal 1: Apresenta o plano de estudos da tecnologia escolhida."""
    dados = carregar_dados()
    tech_key = tecnologia.lower().strip()

    if tech_key not in dados:
        opcoes = ", ".join(dados.keys())
        raise ValueError(f"Tecnologia '{tecnologia}' não encontrada. Opções válidas: {opcoes}")

    trilha = dados[tech_key]
    modulos_str = "\n   ".join(trilha["modulos"])
    return (
        f"📚 TRILHA DE APRENDIZAGEM: {trilha['nome']}\n"
        f"⏱️ Carga Horária Estimada: {trilha['carga_horaria']} horas\n"
        f"📋 Plano de Estudos (Módulos):\n   {modulos_str}"
    )


def gerar_desafio(tecnologia: str, nivel: str, exibir_dica: bool = False) -> str:
    """Comando Principal 2: Gera um desafio de código conforme tecnologia e nível."""
    dados = carregar_dados()
    tech_key = tecnologia.lower().strip()
    nivel_key = nivel.lower().strip()

    if tech_key not in dados:
        opcoes = ", ".join(dados.keys())
        raise ValueError(f"Tecnologia '{tecnologia}' não encontrada. Opções válidas: {opcoes}")

    desafios = dados[tech_key]["desafios"]
    if nivel_key not in desafios:
        niveis = ", ".join(desafios.keys())
        raise ValueError(f"Nível '{nivel}' inválido. Escolha entre: {niveis}")

    desafio = desafios[nivel_key]
    resposta = (
        f"💻 DESAFIO TÉCNICO [{dados[tech_key]['nome']}]\n"
        f"🎯 Nível: {nivel_key.capitalize()} | Título: {desafio['titulo']}\n"
        f"📝 Enunciado: {desafio['descricao']}"
    )
    if exibir_dica:
        resposta += f"\n💡 Dica do Mentor: {desafio['dica']}"
    return resposta


def emitir_certificado(nome_usuario: str, tecnologia: str) -> str:
    """Comando Principal 3: Cria um certificado fictício com hash SHA-256."""
    if not nome_usuario or not nome_usuario.strip():
        raise ValueError("O nome da pessoa usuária não pode estar vazio.")

    dados = carregar_dados()
    tech_key = tecnologia.lower().strip()

    if tech_key not in dados:
        opcoes = ", ".join(dados.keys())
        raise ValueError(f"Tecnologia '{tecnologia}' não encontrada. Opções válidas: {opcoes}")

    trilha = dados[tech_key]
    data_emissao = datetime.now().strftime("%d/%m/%Y")
    hash_input = f"{nome_usuario.strip().upper()}-{tech_key}-{data_emissao}".encode("utf-8")
    hash_curto = hashlib.sha256(hash_input).hexdigest()[:10].upper()
    codigo_validacao = f"GEO-{tech_key[:3].upper()}-{hash_curto}"

    return (
        "╔══════════════════════════════════════════════════════════════╗\n"
        "║                  CERTIFICADO DE CONCLUSÃO                    ║\n"
        "║              GEO-EXPLORER: FINTECH & AI EDITION              ║\n"
        "╠══════════════════════════════════════════════════════════════╣\n"
        f"  Certificamos que: {nome_usuario.strip().upper()}\n"
        f"  Concluiu a trilha: {trilha['nome']}\n"
        f"  Carga Horária: {trilha['carga_horaria']} horas\n"
        f"  Data de Emissão: {data_emissao}\n"
        f"  Hash de Autenticidade: {codigo_validacao}\n"
        "╚══════════════════════════════════════════════════════════════╝"
    )
