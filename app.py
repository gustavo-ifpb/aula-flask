# Importar biblioteca psycopg2
import psycopg2
import psycopg2.extras

# Criar uma conexão com o banco de dados
try:
    conn = psycopg2.connect('dbname=radija user=guga password=gugasv host=127.0.0.1')

    # Criar um cursor para manipular o banco de dados
    # cur = conn.cursor()

    # INSERT: Executar as queries do banco de dados
    # cur.execute("INSERT INTO ator (nome, data_nasc, bio) VALUES ('Tim Allen', '1953-06-13', 'Timothy Alan Dick[1] (born June 13, 1953), known professionally as Tim Allen, is an American actor and comedian.')")
    # conn.commit()

    # Result as dict
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # SELECT
    # cur.execute("SELECT * FROM discente")
    cur.execute("SELECT * FROM money")

    # Fetch all
    result = cur.fetchall()
    print(result[0]['type'], result[0]['value'])

    # for discente in result:
    #     print(f'Nome: {discente[1]} ({discente[0]})')
    
    # Fechar a conexão com o banco
    conn.close()
except psycopg2.OperationalError as connError:
    print('Não foi possível se conectar ao banco de dados. Verifique os dados de conexão.')    