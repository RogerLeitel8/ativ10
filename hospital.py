class Pessoa:
    def __init__(self, nome, rg, telefone, endereco):
        self.nome = nome
        self.rg = rg
        self.telefone = telefone
        self.endereco = endereco

class Medico(Pessoa):
    def __init__(self, crm):
        super().__init__(nome, rg, telefone, endereco)
        self.crm = crm

class Paciente(Pessoa):
    def __init__(self, sintomas):
        super().__init__(nome, rg, telefone, endereco)
        self.sintomas = sintomas

pessoa = Pessoa('raul', '45.998.643-6',  '11-988974356','rua camelo')
medico = Medico(674538298)
paciente = Paciente('febre')

print(pessoa.nome)

