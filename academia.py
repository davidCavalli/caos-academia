import random
import seaborn as sns


class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}
    
    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
    
    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]
    
    def pegar_halteres(self, peso):
        if peso in self.porta_halteres and self.porta_halteres[peso] != 0:
            self.porta_halteres[peso] = 0
            return peso
        return None
        # versão professor
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso
    
    def devolver_halter(self, pos, peso):
        if pos in self.porta_halteres and self.porta_halteres[pos] == 0:
            self.porta_halteres[pos] = peso
            return True
        return False
        # versão professor
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.halteres) * 100


class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo
        self.academia = academia
        self.peso = 0
    
    
    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_halteres(self.peso)
    
    
    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()
        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                if espacos:
                    pos = random.choice(espacos)
                    self.academia.devolver_halter(pos, self.peso)
                else:
                    # lidar com o caso de lista vazia, ex: mostrar mensagem ou tomar outra ação
                    # print("Não há espaços disponíveis para escolha.")
                    pass
        elif self.tipo == 2:
            if espacos:
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)
            else:
                # lidar com o caso de lista vazia, ex: mostrar mensagem ou tomar outra ação
                # print("Não há espaços disponíveis para escolha.")
                pass
        self.peso = 0


academia = Academia()
# usuarios = [Usuario(random.choice([1, 2]), academia) for _ in range(10)]
usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]
list_chaos = []
for k in range(50):
    academia.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for usuario in usuarios:
            usuario.iniciar_treino()
        for usuario in usuarios:
            usuario.finalizar_treino()
    list_chaos.append(academia.calcular_caos())
    print(f'Dia {k+1}: {academia.calcular_caos():.2f}%')
print(f'Média de caos: {sum(list_chaos)/len(list_chaos):.2f}%')
gra = sns.histplot(list_chaos)
gra.figure.savefig('caos.png')
