from database import consultar_tarefas

tarefas = consultar_tarefas()
print(len(tarefas), "tarefa(s) no banco")
for tarefa in tarefas:
    print(tarefa)