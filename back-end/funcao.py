from conexao import conector

def criar_tabela():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER
        )
            """) 
            conexao.commit()
        except Exception as erro:
            print("Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()

 
def cadastar_produtos(nome, categoria, preco, quantidade):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade)  VALUES (%s, %s, %s, %s)", 
                (nome, categoria, preco, quantidade)
            )

            conexao.commit()
        except Exception as erro:
            print(f"Erro ao cadastrar o produto {erro}")
        finally:
            cursor.close()
            conexao.commit()



def listar_produtos():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM Produtos ORDER BY id"
                )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os produtos {erro}")
            return []
        finally:
            cursor.close()
            conexao.commit()


def atualizar_produto(id, novo_preco, nova_quantidade):
    conexao, cursor = conector() 
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET preco = %s, quantidade = %s WHERE id = %s",
                (novo_preco, nova_quantidade, id)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print("Produto atualizado com sucesso!")
            else:
                print("Nenhum produto encontrado com esse ID.")
        except Exception as erro:
            print(f"Erro ao tentar atualizar produto: {erro}")
        finally:
            cursor.close()
            conexao.close() 


def deletar_produto(id):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s",
                (id,)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print("Produto removido com sucesso!")
            else:
                print("Nenhum Produto foi encontrado em nosso estoque")
        except Exception as erro:
            print(f"Erro ao tentar deletar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()
deletar_produto(1)
def buscar_produto(id):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos WHERE id = %s",
                (id,)
            )
            return cursor.fetchone()
        finally:
            cursor.close()
            conexao.close()

