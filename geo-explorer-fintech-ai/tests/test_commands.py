import unittest
from src.commands import listar_trilhas, consultar_trilha, gerar_desafio, emitir_certificado


class TestGeoExplorer(unittest.TestCase):

    def test_listar_trilhas(self):
        saida = listar_trilhas()
        self.assertIn("DADOS", saida)
        self.assertIn("DEVSECOPS", saida)

    def test_consultar_trilha_valida(self):
        saida = consultar_trilha("dados")
        self.assertIn("Star Schema", saida)
        self.assertIn("60 horas", saida)

    def test_consultar_trilha_invalida(self):
        with self.assertRaises(ValueError):
            consultar_trilha("fortran")

    def test_gerar_desafio_com_dica(self):
        saida = gerar_desafio("python", "iniciante", exibir_dica=True)
        self.assertIn("Deduplicação de Transações Bancárias", saida)
        self.assertIn("Dica do Mentor:", saida)

    def test_gerar_desafio_nivel_invalido(self):
        with self.assertRaises(ValueError):
            gerar_desafio("devsecops", "ultra_hard")

    def test_emitir_certificado_valido(self):
        saida = emitir_certificado("Paulo Sérgio", "ia_generativa")
        self.assertIn("PAULO SÉRGIO", saida)
        self.assertIn("GEO-IA_-", saida)

    def test_emitir_certificado_nome_vazio(self):
        with self.assertRaises(ValueError):
            emitir_certificado("   ", "python")


if __name__ == "__main__":
    unittest.main()
