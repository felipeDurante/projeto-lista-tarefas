# Lista de Tarefas em Python

Projeto didatico de linha de comando para aprender Python com arquivos,
classes, JSON, argumentos de terminal e testes automatizados.

## Como executar

```powershell
cd projeto-lista-tarefas
python main.py adicionar "Estudar Python"
python main.py listar
python main.py concluir 1
python main.py remover 1
```

## Como testar

```powershell
python -m unittest discover -s tests -v
```

## Comandos

- `adicionar "descricao"` adiciona uma tarefa.
- `listar` mostra todas as tarefas.
- `concluir ID` marca uma tarefa como concluida.
- `remover ID` remove uma tarefa.
