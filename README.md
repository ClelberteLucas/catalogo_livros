Olá, meu nome é Clelberte.
Esse codigo é relacionado a um projeto de extensão, que foi desenvolvido na Biblioteca da escola escola Mestre Paranhos, a escola ultilizava registros manuais para gerenciar seus livros, correndo alto risco de perda de informações e controle dos livros.
Esse projeto de extensão é sem fins lucrativos, e tem como objetivo aplicar o conteúdo aprendido no curso no dia a dia das pessoas.


Esse projeto software tem o objetivo de criar uma interface GUI, utilizando a linguagem python (Biblioteca tkinter), para interagir com um banco de dados no postgreSQL, através da biblioteca Psycopg2.
o software vai servir para a gestão de livros na biblioteca escolar.
Essa aplicação serve para catálogo de livros.
Para a aplicação funcionar será necessario a instalação do POSTGRESQL, O INTERPRETADOR PYTHON e, a biblioteca TKINTER e psycopg2






-principal_livros:
 O arquivo principal_livros tem todas as configurações da janela de interação USUARIOxBANCO DE DADOS: Botões, funcões de manipulação de informações no banco de dados e o layout da janela

 A interface contem 5 campos para preencher no topo da janela:
 -Codigo: relacionado ao codigo de identiificação do livro
 -Data: relacionada a data de registro
 -Titulo: Relacionada ao titulo do livro
 -Autor(A): Relacionado ao autor(A) do livro
 -Edição: relacionada a edição do livro


A interface conta com 5 botões relacionado a funções no meio da janela:
-Buscar: serve Para buscar um registro de livros cadastrado
-Cadastrar: serve para cadastrar algum registro selecionado
-Excluir: serve para Excluir algum registro selecionado
-Atualizar: serve para Atualizar algum registro selecionado
-Limpar: serve para limpar os campos preenchidos pelo usuário

No final da janela, temos uma lista para exibir todos os registros presentes no banco de dados, usando uma *TreeviewSelect*

-def_livros:
O arquivo def_livros estão as funções utilizadas pelo sistema principal (principal_livros).

-Abrir Conexão
-Selecionard dados
-Inserir dados
-Atualizar dados
-Excluir dados
-Buscar dados

-tabela_livros:
esse é o codigo que cria a tabela para guardar as informacões inseridas no banco de dados







