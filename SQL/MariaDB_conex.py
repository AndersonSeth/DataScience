import mariadb
import sys

try:
    conn = mariadb.connect(
        user="adm",
        password='123456789',
        host='mariadb-188929-0.cloudclusters.net',
        port=10081,
        database='Viagens'
    )
    print("Conexão bem sucedida!")
except mariadb.Error as e:
    print(f'Erro de conexao com a plataforma MariaDB: {e}')
    sys.exit(1)

cur = conn.cursor()

# criando_tabela_usuarios_query = """
# CREATE TABLE IF NOT EXISTS usuarios (
#     id INT,
#     nome VARCHAR(225) NOT NULL COMMENT 'Nome de ususario',
#     email VARCHAR(100) NOT NULL UNIQUE COMMENT 'EMAIL DO USUARIO',
#     endereco VARCHAR(50) NOT NULL COMMENT 'ENDEREÇO DO USUARIO',
#     data_Nascimento DATE NOT NULL COMMENT ' DATA DE NASCIMENTO DO USUARIO');

# """
# criando_tabela_destinos_query = """
# CREATE TABLE IF NOT EXISTS destinos (
#     id INT,
#     nome VARCHAR(225) NOT NULL UNIQUE COMMENT 'Nome do Destino',
#     descricao VARCHAR(225) NOT NULL COMMENT 'Descrição do destino');

# """

criando_tabela_reservas_query = """
CREATE TABLE IF NOT EXISTS reservas (
    id INT COMMENT 'Identificador único da reserva',
    id_usuario INT COMMENT 'referencia ao ID do usuario que fez a reserva',
    id_destino INT COMMENT 'referencia ao ID do destino da reserva',
    data DATE COMMENT 'Data da reserva',
    status VARCHAR(225) DEFAULT 'penente' COMMENT 'Status da reserva(confirmada, pendente, cancelada, etc.)'
    );

"""

try:
    cur.execute(criando_tabela_reservas_query)
    print("Tabela 'Reservas' Criada com Sucesso!")
except mariadb.Error as e:
    print(f'Erro ao criar a tabela: {e}')
    sys.exit(1)