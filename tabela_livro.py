import psycopg2
try:
    conn = psycopg2.connect(dbname="postgres", user="postgres", host="localhost", password="cruzeiro")
    print("Conexão realizada com sucesso")
    cur = conn.cursor()

    comando = '''CREATE TABLE Livros ( 
                        codigo INTEGER NOT NULL,
                        data DATE NOT NULL,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        edicao TEXT NOT NULL,
                        PRIMARY KEY(codigo)
                        );'''
    cur.execute(comando)
    conn.commit()
    print("Tabela livros criada com sucesso")
    cur.close()
except:
    print("Tabela livros criada com erro")


