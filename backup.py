import tkinter as tk
import random
from collections import deque
from tkinter import PhotoImage


class PlanoCartesianoApp:
    def __init__(self, master, largura, altura, tamanho_celula):
        self.master = master
        master.title("Plano Cartesiano")

        self.canvas = tk.Canvas(master, width=largura, height=altura)
        self.canvas.pack()

        self.imagem_motoboy = tk.PhotoImage(file="./boy.ppm")

        self.largura = largura
        self.altura = altura
        self.tamanho_celula = tamanho_celula

        self.linhas = altura // tamanho_celula
        self.colunas = largura // tamanho_celula

        self.pontos = [[0] * self.colunas for _ in range(self.linhas)]

        # Adicionando o ponto do motoboy em um local aleatório
        self.motoboy_x = random.randint(0, self.colunas - 1)
        self.motoboy_y = random.randint(0, self.linhas - 1)
        self.pontos[self.motoboy_y][self.motoboy_x] = "motoboy"

        # Adicionando 3 pontos de entrega aleatórios
        self.pontos_entrega = []
        self.pontos_entregues = []
        while len(self.pontos_entrega) < 3:
            x = random.randint(0, self.colunas - 1)
            y = random.randint(0, self.linhas - 1)
            if (x, y) != (self.motoboy_x, self.motoboy_y) and (x, y) not in self.pontos_entrega:
                self.pontos_entrega.append((x, y))
                self.pontos[y][x] = "entrega"

        # Desenhando o plano cartesiano
        for linha in range(self.linhas + 1):
            y = linha * tamanho_celula
            self.canvas.create_line(0, y, largura, y, fill="black")

        for coluna in range(self.colunas + 1):
            x = coluna * tamanho_celula
            self.canvas.create_line(x, 0, x, altura, fill="black")

        # Desenhando os pontos
        for y, linha in enumerate(self.pontos):
            for x, ponto in enumerate(linha):
                if ponto == "motoboy":
                    self.canvas.create_rectangle(x * tamanho_celula, y * tamanho_celula,
                                                 (x + 1) * tamanho_celula, (y + 1) * tamanho_celula,
                                                 fill="red")
                elif ponto == "entrega":
                    self.canvas.create_rectangle(x * tamanho_celula, y * tamanho_celula,
                                                 (x + 1) * tamanho_celula, (y + 1) * tamanho_celula,
                                                 fill="blue")

        # Calculando e exibindo os caminhos        
        menor_caminho = self.encontrar_menor_caminho()
        if menor_caminho:
            self.movimentos = deque(menor_caminho)
            self.mover_motoboy()

    def encontrar_menor_caminho(self):
        menor_caminho = None
        menor_distancia = float("inf")
        for ponto_entrega in self.pontos_entrega:
            caminho = self.bfs(self.motoboy_x, self.motoboy_y, ponto_entrega[0], ponto_entrega[1])
            if caminho and len(caminho) < menor_distancia:
                menor_caminho = caminho
                menor_distancia = len(caminho)
        return menor_caminho

    def mover_motoboy(self):
        if self.movimentos:
            self.rastro() # Posição anterior antes de atualizar abaixo, pintar o rastro
            self.motoboy_x, self.motoboy_y = self.movimentos.popleft() # Atualiza a posição global do motoboy com o próximo elemento da fila
            self.atualizar_desenho()
            self.master.after(500, self.mover_motoboy)
        if len(self.movimentos) == 0:
            self.entregue()


    def atualizar_desenho(self):
        self.pontos[self.motoboy_y][self.motoboy_x] = "motoboy"  # Adicionar o motoboy ao próximo ponto
        for y, linha in enumerate(self.pontos):
            for x, ponto in enumerate(linha):
                if ponto == "motoboy":
                    self.canvas.create_rectangle(x * self.tamanho_celula, y * self.tamanho_celula,
                                                (x + 1) * self.tamanho_celula, (y + 1) * self.tamanho_celula,
                                                fill="red")   

    def rastro(self):
        for y, linha in enumerate(self.pontos):
            for x, ponto in enumerate(linha):
                if ponto == "motoboy" and ponto != "entregue":
                    self.canvas.create_rectangle(x * self.tamanho_celula, y * self.tamanho_celula,
                                                 (x + 1) * self.tamanho_celula, (y + 1) * self.tamanho_celula,
                                                 fill="gray")
                    self.pontos[self.motoboy_y][self.motoboy_x] = 0  # Remover o motoboy do ponto atual 

                    
    def entregue(self):
        for i, ponto_entrega in enumerate(self.pontos_entrega):
            x, y = ponto_entrega            
            if self.motoboy_x == x and self.motoboy_y == y:
                self.pontos_entregues.append(ponto_entrega)
                self.pontos[y][x] = "entregue"

                self.canvas.create_image((x * self.tamanho_celula) + (self.tamanho_celula // 2), 
                                        (y * self.tamanho_celula) + (self.tamanho_celula // 2), 
                                        anchor=tk.CENTER, image=self.imagem_motoboy)


                self.pontos_entrega.pop(i)
                break

        if len(self.pontos_entrega):
            menor_caminho = self.encontrar_menor_caminho()
            if menor_caminho:
                self.movimentos = deque(menor_caminho)
                self.movimentos.popleft()
                self.mover_motoboy()



    def bfs(self, x_inicial, y_inicial, x_final, y_final):
        visitado = [[False] * self.colunas for _ in range(self.linhas)]
        fila = [(x_inicial, y_inicial, [])]

        while fila:
            x, y, caminho = fila.pop(0)
            if x == x_final and y == y_final:
                return caminho + [(x, y)]

            if visitado[y][x]:
                continue
            visitado[y][x] = True

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Não permite movimento na diagonal
                novo_x, novo_y = x + dx, y + dy
                if 0 <= novo_x < self.colunas and 0 <= novo_y < self.linhas and not visitado[novo_y][novo_x]:
                    fila.append((novo_x, novo_y, caminho + [(x, y)]))

        return None


root = tk.Tk()
largura = 1024
altura = 1024
tamanho_celula = 64
app = PlanoCartesianoApp(root, largura, altura, tamanho_celula)
root.mainloop()
