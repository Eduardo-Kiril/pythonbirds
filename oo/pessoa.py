class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=18):
            self.idade = idade
            self.nome = nome
            self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    jota = Pessoa(nome='Jota')
    kiril = Pessoa(jota, nome='Kiril')
    print(Pessoa.cumprimentar(kiril))
    print(id(kiril))
    print(kiril.cumprimentar())
    print(kiril.nome)
    print(kiril.idade)
    for filho in kiril.filhos:
        print(filho.nome)
    kiril.sobrenome = "Rodrigues"
    kiril.olhos = 1
    Pessoa.olhos = 3
    print(kiril.__dict__)
    print(jota.__dict__)
    print(Pessoa.olhos)
    print(kiril.olhos)
    print(jota.olhos)
