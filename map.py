import tkinter as tk

# Samucão, aqui a gente tem um plano cartesianinho pra você como Classe


class PlanoCartesianoApp:
  # aqui a gente inicia o plano cartesiano com o master, a largura, a altura e o tamanho da celula
  # noss função __init__ é o construtor da classe, ele é chamado quando a classe é instanciada
    def __init__(self, master, largura, altura, tamanho_celula):
        self.master = master
        master.title("Plano Cartesiano")

        self.canvas = tk.Canvas(master, width=largura, height=altura)
        self.canvas.pack()

        self.largura = largura
        self.altura = altura
        self.tamanho_celula = tamanho_celula

        self.linhas = altura // tamanho_celula
        self.colunas = largura // tamanho_celula

        # aqui a gnt cria nossas linhas horizontais samuca
        for linha in range(self.linhas + 1):
            y = linha * tamanho_celula
            self.canvas.create_line(0, y, largura, y, fill="black")

        # linhas verticais
        for coluna in range(self.colunas + 1):
            x = coluna * tamanho_celula
            self.canvas.create_line(x, 0, x, altura, fill="black")

        self.pontos = [[0] * self.colunas for _ in range(self.linhas)]
        # aqui a gente cria um evento de clique no botão esquerdo do mouse pra adicionar um ponto
        self.canvas.bind("<Button-1>", self.adicionar_ponto)
    # aqui a gente adiciona um ponto no plano cartesiano

    def adicionar_ponto(self, event):
        x = event.x
        y = event.y

        # Convertendo as coordenadas para o sistema de grade
        linha = y // self.tamanho_celula
        coluna = x // self.tamanho_celula
        # O ponto é uma tupla com a coluna e a linha vamos ter que modelar desse jeito
        ponto = (coluna, linha)
        if self.pontos[linha][coluna] == 0:
            self.pontos[linha][coluna] = 1
            print("Novo ponto adicionado:", ponto)


root = tk.Tk()
largura = 400
altura = 400
tamanho_celula = 20  # Tamanho da célula
app = PlanoCartesianoApp(root, largura, altura, tamanho_celula)
root.mainloop()
