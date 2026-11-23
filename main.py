from __future__ import annotations

import argparse
from pathlib import Path

from tarefa import GerenciadorTarefas


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Gerenciador simples de tarefas")
    subcomandos = parser.add_subparsers(dest="comando", required=True)

    adicionar = subcomandos.add_parser("adicionar", help="Adicionar uma tarefa")
    adicionar.add_argument("descricao", help="Descricao da tarefa")

    subcomandos.add_parser("listar", help="Listar tarefas")

    concluir = subcomandos.add_parser("concluir", help="Concluir uma tarefa")
    concluir.add_argument("id", type=int, help="ID da tarefa")

    remover = subcomandos.add_parser("remover", help="Remover uma tarefa")
    remover.add_argument("id", type=int, help="ID da tarefa")

    return parser


def main() -> None:
    args = construir_parser().parse_args()
    gerenciador = GerenciadorTarefas(Path("tarefas.json"))

    if args.comando == "adicionar":
        tarefa = gerenciador.adicionar(args.descricao)
        print(f"Tarefa adicionada: [{tarefa.id}] {tarefa.descricao}")
    elif args.comando == "listar":
        tarefas = gerenciador.listar()
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        for tarefa in tarefas:
            status = "Concluida" if tarefa.concluida else "Pendente"
            print(f"[{tarefa.id}] {tarefa.descricao} - {status}")
    elif args.comando == "concluir":
        if gerenciador.concluir(args.id):
            print(f"Tarefa {args.id} concluida.")
        else:
            print(f"Tarefa {args.id} nao encontrada.")
    elif args.comando == "remover":
        if gerenciador.remover(args.id):
            print(f"Tarefa {args.id} removida.")
        else:
            print(f"Tarefa {args.id} nao encontrada.")


if __name__ == "__main__":
    main()
