class Pessoa:
    def __init__(self, nome=None, idade=18):
            self.idade = idade
            self.nome = nome
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Kiril')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Dogão'
    print(p.nome)
