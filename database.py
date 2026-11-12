import mysql.connector
from mysql.connector import Error

# -------------------------------------------- #
# -------- Conectar o database ao APP -------- #
def conectar():
    try:
        conexao = mysql.connector.connect(
        host="localhost",          # Endereço
        user="root",               # Usuário
        password="senai",          # Senha
        database="estodolist"      # Databasecriado
        )

        # Operador que vai manipular seu banco de dados (conexão)
        cursor = conexao.cursor(dictionary=True) # Devolve no formato Dict
        # retorna duas informações: conexão e cursor
        return conexao, cursor
    
    except Error as erro:
        print("ERRO! Falha ao se conectar com o banco de dados: {erro}")
        return None, None

# -------------------------------------- #
# -------- Funçã inserir tarefa -------- #
def inserir_tarefa(nome_tarefa,descricao, categoria, data_prazo, prioridade):
    conexao, cursor = conectar() # se conectar com BD

    # Verificar se a conexão funcionou
    if conexao is None:
        return False

    try:
        # %s SQL parametrizado para evitar SQL injection
        sql = "INSERT INTO tarefa (nomeTarefa,descricao,categoria,dataPrazo,prioridade) VALUES (%s, %s, %s, %s, %s)"
        # Executa o SQL parametrizado e passa os parâmetros da função
        cursor.execute(sql,(nome_tarefa,descricao,categoria,data_prazo,prioridade))
        # confirma as alterações
        conexao.commit()    
        # Retornar TRU para função principsl
        return True
    
    except Error as erro:
        print(f"ERRO! Falha ao inserir a tarefa: {erro}")
        return False
    finally:
        cursor.close()
        conexao.close()

# ------------------------------------------------------------------------- #
# -------- Retornar todas as tarefas cadastradas de Banco de Dados -------- #
def consultar_tarefas():
    # Chama função conectar
    conexao, cursor = conectar()
    #Verificar se a conexão falhou
    if conexao is None:
        return [] # Lista Vazia
    try: # Tenta executar o comando SQL
        # Selecione todas as colunas da(origem) tabela tarefa;
        sql = """
              SELECT
                idTarefa AS idtarefa,
                dataPrazo AS data_prazo,
                nomeTarefa AS nome_tarefa,
                status,
                descricao,
                categoria,
                prioridade
              FROM tarefa;
              """
        # Executa o comando da variável SQL
        cursor.execute(sql)
        # Buscar todas as linhas da consulta executada
        tarefas = cursor.fetchall()

        # Retorna para progrmação principal as tarefas
        return tarefas # Lista de Dicionários 


    except Error as erro: # se der erro
        print(f"ERRO! Falha ao listar as tarefas: {erro}")
        return [] # Retorna lista vazia em caso de error

    finally: # Executa sempre dando certo ou não
        cursor.close() # Encerra o cursor
        conexao.close() # Encerra a conexão

# -------------------------------------------------------------------- #
# -------- Essa função marca como concluída a tarefa indicada -------- #
def concluir_tarefa(idtarefa):
    conexao, cursor = conectar()

    if conexao is None:
        return False

    try:
        sql = "UPDATE tarefa SET status = 'Concluida' WHERE idTarefa = %s"
        cursor.execute(sql,(idtarefa,))
        conexao.commit() # Confirma a alteração nos dados
        return True


    except Error as erro:
        print(f"ERRO! Falha ao listar as tarefas: {erro}")
        return False # Retorna lista vazia em caso de error
    finally:
        cursor.close()
        conexao.close()

# --------------------------------------------------------------------- #
# ---------- Essa função ira editar as informações da tarefa ---------- #
def alterar_tarefa(idtarefa, nome_tarefa, descricao, categoria, data_prazo, prioridade):
    conexao, cursor = conectar()

    if conexao is None:
        return False

    try:
        sql = """ 
        UPDATE tarefa
        SET 
        nomeTarefa = %s, 
        descricao = %s, 
        categoria = %s, 
        dataPrazo = %s, 
        prioridade = %s 
        WHERE idTarefa = %s;
        """
        cursor.execute(sql,(nome_tarefa, descricao, categoria, data_prazo, prioridade, idtarefa))
        conexao.commit() # Confirma a alteração nos dados
        return True


    except Error as erro:
        print(f"ERRO! Falha ao editar a tarefa: {erro}")
        return False # Retorna lista vazia em caso de error
    finally:
        cursor.close()
        conexao.close()

# ---------------------------------------------------- #
# ------------------ Apagar tarefa ------------------- #
def apagar_tarefa(idtarefa):
    conexao, cursor = conectar()

    if conexao is None:
        return False

    try:
        sql = "DELETE FROM tarefa WHERE idTarefa = %s"

        cursor.execute(sql, (idtarefa,))
        conexao.commit()

        return True

    except Error as erro:
        print(f"ERRO! Falha ao excluir a tarefa: {erro}")
        return False

    finally:
        cursor.close()
        conexao.close()