import argparse
import sys
from src.commands import listar_trilhas, consultar_trilha, gerar_desafio, emitir_certificado


def main():
    parser = argparse.ArgumentParser(
        description="Geo-Explorer CLI - Plataforma de Trilhas, Desafios e Certificados"
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    # Comando Extra: listar
    subparsers.add_parser("listar", help="Lista todas as trilhas disponíveis no catálogo")

    # Comando 1: trilha
    p_trilha = subparsers.add_parser("trilha", help="Exibe o plano de estudos de uma tecnologia")
    p_trilha.add_argument("--tech", required=True, help="Tecnologia (dados, python, devsecops, ia_generativa)")

    # Comando 2: desafio
    p_desafio = subparsers.add_parser("desafio", help="Gera um desafio prático de código")
    p_desafio.add_argument("--tech", required=True, help="Tecnologia escolhida")
    p_desafio.add_argument("--nivel", required=True, help="Nível (iniciante, intermediario, avancado)")
    p_desafio.add_argument("--dica", action="store_true", help="Exibe uma dica técnica para resolver o desafio")

    # Comando 3: certificado
    p_cert = subparsers.add_parser("certificado", help="Emite um certificado fictício de conclusão")
    p_cert.add_argument("--nome", required=True, help="Nome completo para o certificado")
    p_cert.add_argument("--tech", required=True, help="Tecnologia concluída")

    args = parser.parse_args()

    try:
        if args.comando == "listar":
            print(listar_trilhas())
        elif args.comando == "trilha":
            print(consultar_trilha(args.tech))
        elif args.comando == "desafio":
            print(gerar_desafio(args.tech, args.nivel, args.dica))
        elif args.comando == "certificado":
            print(emitir_certificado(args.nome, args.tech))
    except ValueError as err:
        print(f"❌ Erro de Validação: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
