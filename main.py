#Estudo de herança OO
class Veiculo():
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10

class Carro(Veiculo):
    def __init__(self,cor, marca, modelo, motor):
        super().__init__(cor, marca, modelo)
        self.motor  = motor

    def acelerar(self):
        self.velocidade += 20


class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossivel alterar salario diretamente. use a funcao calcula_salario().")



    def registra_hora_trabalhada(self):
        self.horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada



if __name__ == '__main__':
    pedro = Funcionario('Pedro', 'Gerente de Vendas', 50)
    pedro.salario = 100000
    print(pedro.__salario)


