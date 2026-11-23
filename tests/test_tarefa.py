import tempfile
import unittest
from pathlib import Path

from tarefa import GerenciadorTarefas


class GerenciadorTarefasTest(unittest.TestCase):
    def criar_gerenciador(self) -> GerenciadorTarefas:
        diretorio = tempfile.TemporaryDirectory()
        self.addCleanup(diretorio.cleanup)
        return GerenciadorTarefas(Path(diretorio.name) / "tarefas.json")

    def test_adicionar_e_listar(self) -> None:
        gerenciador = self.criar_gerenciador()

        tarefa = gerenciador.adicionar("Estudar Python")

        self.assertEqual(tarefa.id, 1)
        self.assertEqual(gerenciador.listar()[0].descricao, "Estudar Python")

    def test_rejeitar_descricao_vazia(self) -> None:
        gerenciador = self.criar_gerenciador()

        with self.assertRaises(ValueError):
            gerenciador.adicionar("   ")

    def test_concluir_tarefa(self) -> None:
        gerenciador = self.criar_gerenciador()
        gerenciador.adicionar("Praticar testes")

        self.assertTrue(gerenciador.concluir(1))
        self.assertTrue(gerenciador.listar()[0].concluida)

    def test_remover_tarefa(self) -> None:
        gerenciador = self.criar_gerenciador()
        gerenciador.adicionar("Excluir tarefa")

        self.assertTrue(gerenciador.remover(1))
        self.assertEqual(gerenciador.listar(), [])

    def test_carregar_tarefas_salvas(self) -> None:
        gerenciador = self.criar_gerenciador()
        gerenciador.adicionar("Persistir dados")

        novo_gerenciador = GerenciadorTarefas(gerenciador.arquivo)

        self.assertEqual(len(novo_gerenciador.listar()), 1)
