from dataclasses import dataclass, field
import math
import matplotlib.pyplot as plt

@dataclass
class Conjunto:
    amostras: list[int]
    numero_de_classes: int = field(init = False)
    maior_numero: int = field(init = False)
    menor_numero: int = field(init = False)
    amplitute_total: int = field(init = False)
    largura_da_classe: int = field(init = False)
    limite_inferior: list[int] = field(init = False)
    limite_superior: list[int] = field(init = False)
    frequencia: list[list[int]] = field(init = False)

    def __post_init__(self):
        self.numero_de_classes = int(1 + (3.322 * math.log(len(self.amostras), 10)))
        self.maior_numero = max(self.amostras)
        self.menor_numero = min(self.amostras)
        self.amplitute_total = self.maior_numero - self.menor_numero
        self.largura_da_classe = math.ceil(self.amplitute_total / self.numero_de_classes)

        self.limite_inferior = [self.menor_numero]
        for i in range(1, self.numero_de_classes):
            self.limite_inferior.append(self.limite_inferior[i - 1] + self.largura_da_classe)

        self.limite_superior = [n + (self.largura_da_classe - 1) for n in self.limite_inferior]

        self.frequencia = [[] for _ in range(self.numero_de_classes)]
        amostras_crescente = self.amostras
        amostras_crescente.sort()
        for n_conjunto in amostras_crescente:
            for i in range(self.numero_de_classes):
                if(self.limite_inferior[i] <= n_conjunto and n_conjunto <= self.limite_superior[i]):
                    self.frequencia[i].append(n_conjunto)
                    break

    def histogramaFrequenciaRelativa(self):
        grupos = [f'{intervalo}\na\n{intervalo + self.largura_da_classe}' for intervalo in self.limite_inferior]
        valores = [len(list) / len(self.amostras) for list in self.frequencia]

        plt.bar(grupos, valores)
        plt.xlabel('Classes')
        plt.ylabel('Frequência relativa')
        plt.show()