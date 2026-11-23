from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Tarefa:
    id: int
    descricao: str
    concluida: bool = False


class GerenciadorTarefas:
    def __init__(self, arquivo: Path) -> None:
        self.arquivo = arquivo
        self.tarefas = self._carregar()

    def _carregar(self) -> list[Tarefa]:
        if not self.arquivo.exists():
            return []

        dados = json.loads(self.arquivo.read_text(encoding="utf-8"))
        return [Tarefa(**item) for item in dados]

    def _salvar(self) -> None:
        dados = [asdict(tarefa) for tarefa in self.tarefas]
        self.arquivo.write_text(
            json.dumps(dados, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def adicionar(self, descricao: str) -> Tarefa:
        descricao = descricao.strip()
        if not descricao:
            raise ValueError("A descricao nao pode estar vazia.")

        novo_id = max((tarefa.id for tarefa in self.tarefas), default=0) + 1
        tarefa = Tarefa(id=novo_id, descricao=descricao)
        self.tarefas.append(tarefa)
        self._salvar()
        return tarefa

    def listar(self) -> list[Tarefa]:
        return list(self.tarefas)

    def concluir(self, tarefa_id: int) -> bool:
        for tarefa in self.tarefas:
            if tarefa.id == tarefa_id:
                tarefa.concluida = True
                self._salvar()
                return True
        return False

    def remover(self, tarefa_id: int) -> bool:
        for indice, tarefa in enumerate(self.tarefas):
            if tarefa.id == tarefa_id:
                del self.tarefas[indice]
                self._salvar()
                return True
        return False
