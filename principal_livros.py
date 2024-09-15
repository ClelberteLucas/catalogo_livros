import tkinter as tk
from tkinter import ttk
import def_livros as def_livros

class PrincipalDB:
    def __init__(self, win):
        self.objBD = def_livros.AppBD()
        # Componentes
        self.lbCodigo=tk.Label(win, text='Codigo: ')
        self.lblData = tk.Label(win, text='Data de Registro: ')
        self.lblNome=tk.Label(win, text='Titulo: ')
        self.lblAutor=tk.Label(win, text='Autor(A): ')
        self.lblEdicao = tk.Label(win, text='Edição: ')

        self.txtCodigo=tk.Entry(bd=3)
        self.txtNome=tk.Entry()
        self.txtAutor=tk.Entry()
        self.txtData = tk.Entry()
        self.txtEdicao = tk.Entry()
        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fcadastrarProduto)
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)
        self.btnBuscar=tk.Button(win, text='Buscar', command=self.fBuscarProduto)


        self.dadosColunas = ("Codigo", "Data de Registro", "Titulo", "Autor", "Edicao")
        self.treeLivros = ttk.Treeview(win, columns=self.dadosColunas, selectmode='browse')
        self.verscrlbar = ttk.Scrollbar(win, orient='vertical', command=self.treeLivros.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.treeLivros.configure(yscrollcommand=self.verscrlbar.set)
        self.treeLivros.heading("Codigo", text="Código")
        self.treeLivros.heading("Data de Registro", text="Data de Registro")
        self.treeLivros.heading("Titulo", text="Titulo")
        self.treeLivros.heading("Autor", text="Autor(A)")
        self.treeLivros.heading("Edicao", text="Edição")

        self.treeLivros.column("Codigo", minwidth=0, width=100)
        self.treeLivros.column("Data de Registro", minwidth=0, width=100)
        self.treeLivros.column("Titulo", minwidth=0, width=100)
        self.treeLivros.column("Autor", minwidth=0, width=100)

        self.treeLivros.column("Edicao", minwidth=0, width=100)

        self.treeLivros.pack(padx=10, pady=10)
        self.treeLivros.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        #Posicionamento dos componentes na janela
        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lblData.place(x=100, y=100)
        self.txtData.place(x=250, y=100)

        self.lblNome.place(x=100, y=150)
        self.txtNome.place(x=250, y=150)

        self.lblAutor.place(x=400, y=50)
        self.txtAutor.place(x=550, y=50)

        self.lblEdicao.place(x=400, y=100)
        self.txtEdicao.place(x=550, y=100)


        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)
        self.btnBuscar.place(x=500, y=200)

        self.treeLivros.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)
        self.carregarDadosIniciais()

    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeLivros.selection():
            item = self.treeLivros.item(selection)
            codigo, data, titulo, edicao, autor = item["values"] [0:5]
            self.txtCodigo.insert(0, codigo)
            self.txtData.insert(0, data)
            self.txtNome.insert(0, titulo)
            self.txtEdicao.insert(0, edicao)
            self.txtAutor.insert(0, autor)

    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registro = self.objBD.selecionarDados()
            print("***************** dados disponiveis no BD *******************")
            for item in registro:
                codigo=item[0]
                data=item[1]
                titulo=item[2]
                autor=item[3]
                edicao = item[4]
                print("código = ", codigo)
                print("Data = ", data)
                print("Titulo = ", titulo)
                print("Autor = ", autor)
                print("Edicao = ", edicao, "\n")

                self.treeLivros.insert('', 'end', iid=self.iid, values=(codigo, data, titulo, autor, edicao))
                self.iid = self.iid + 1
                self.id = self.id + 1
                print("Dados da base")
        except:
            print('Ainda não existem dados para carregar')


    def fLerCampos(self):
        try:
            print("******************** dados disponiveis *********************")
            codigo = int(self.txtCodigo.get())
            print('Codigo', codigo)
            data = self.txtData.get()
            print('Data', data)
            titulo = self.txtNome.get()
            print('Titulo', titulo)
            edicao = self.txtEdicao.get()
            print('Edição', edicao)
            autor = self.txtAutor.get()
            print('Autor', autor)
            print("Leitura os dados com sucesso")

        except:
            print('Não foi possivel ler os dados')
        return codigo, data, titulo, edicao, autor

    def fcadastrarProduto(self):
        try:
            print("****************** dados disponiveis **************************")
            codigo, data, titulo, edicao, autor = self.fLerCampos()
            self.objBD.inserirDados(codigo, data, titulo, edicao, autor)
            self.treeLivros.insert('', 'end', iid=self.iid, values=(codigo, data, titulo, edicao, autor))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print('Produto cadastrado com sucesso')
        except:
            print("Não foi possivel fazer o cadastro")


    def fAtualizarProduto(self):
        try:
          print("****************** dados disponiveis ********************")
          codigo, data, titulo, edicao, autor = self.fLerCampos()
          self.objBD.atualizarDados(codigo, data, titulo, edicao, autor)
          # Rcarregar dados na tela
          self.treeLivros.delete(*self.treeLivros.get_children())
          self.carregarDadosIniciais()
          self.fLimparTela()
          print('O produto foi atualizado com sucesso')
        except:
            print('Não foi possivel fazer a atualização')


    def fExcluirProduto(self):
        try:
            print("**************** dados disponiveis *******************&")
            codigo, data, titulo, edicao, autor = self.fLerCampos()
            self.objBD.excluirDados(codigo)
            # Recarregar dados na tela
            self.treeLivros.delete(*self.treeLivros.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print('O produto foi excluido com sucesso')
        except:
            print('Não foi possivel fazer a exclusão do produto')


    def fLimparTela(self):
        try:
            print("**************** dados disponiveis ********************")
            self.txtCodigo.delete(0, tk.END)
            self.txtData.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtAutor.delete(0, tk.END)
            self.txtEdicao.delete(0, tk.END)
            print('Campos limpos')
        except:
            print('Não foi possivel limpar os campos')

    def fBuscarProduto(self):
        try:
            self.treeLivros.delete(*self.treeLivros.get_children())
            print("**************** dados disponiveis *******************")
            livros = self.objBD.buscarDados(self.txtCodigo.get())
            self.treeLivros.insert('', 'end', iid=self.iid, values=livros)
            self.iid = self.iid + 1
            self.id = self.id + 1

        except Exception as e:
            print(e)

janela = tk.Tk()
principal = PrincipalDB(janela)
janela.title('Bem vindo ao Gerenciador de Biblioteca')
janela.geometry("820x600+10+10")
janela.mainloop()