class Conta_bancaria:

    taxa_juros = 0
    total_contas = 0

    def __init__(self, titular, saldo, nome):
        self.titula = titular
        self.saldo = saldo
        self.nome = nome
        Conta_bancaria.total_contas += 1

    def depositar(self, valor):
        
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso")
        else:
            print("Erro: O valor do sepósito não pode ser zero ou negativo")

    def sacar (self, debitado):
        
        if debitado > 0 and self.saldo >= debitado:
            self.saldo -= debitado
            print(f"Saldo debitado da sua conta R${debitado:.2f} realizado com sucesso")
        else:
            print(f"saldo insuficiente ou valor invalido comunique um atendente para mais informações")
    
    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
    
    @classmethod    
    def total_de_contas(cls):
        print(f"total de contas atuais são {cls.total_contas} ")
    
    @classmethod     
    def ajustar_taxa_juros(cls, nova_taxa):
        if nova_taxa < 0:
            print ("a taxa de juros deve ser positiva")
        else:
            cls.taxa_juros = nova_taxa
            print(f"nova taxa de juros ajustada para {nova_taxa:.2%}")

     

    @staticmethod
    def converter_moeda(valor: float, taxa: float) -> float:
        return valor * taxa

    @staticmethod
    def dias_no_ano() -> int:
        return 365
    

    
# valor_convertido = Util.converter_moeda(100, 5.2)
# print(f"Valor convertido: {valor_convertido}")

# dias = Util.dias_no_ano()
# print(f"Número de dias no ano: {dias}")


    @classmethod 
     
    def conta (cls):
      print(f"total de contas novas {cls.total_contas}")

# pessoa1 = Conta_bancaria ("lua",10,"fi-fei li")
# pessoa2 = Conta_bancaria ("ua",1000,"ei-fei li")
# pessoa3 = Conta_bancaria ("lu",1000,"fei-ei li")
# pessoa4 = Conta_bancaria ("a",10000,"fei-ei li")
# Conta_bancaria.conta()


# Conta_bancaria.ajustar_taxa_juros(0.3) 
# Conta_bancaria.ajustar_taxa_juros(-0.02)

# conta = Conta_bancaria ("lu", 1000, "luani")
# conta.depositar(50)  
# conta.depositar(-10)  
# conta.sacar(1049)  
# conta.sacar(200) 
# conta.verificar_saldo()
# conta.total_de_contas()
# conta.ajustar_taxa_juros(0.5)


conta = Conta_bancaria("joão",100,"juju")
conta.depositar(50)
conta.depositar(30)
conta.verificar_saldo()
conta.sacar(40)
conta.verificar_saldo()
conta.total_de_contas()

conta1 = Conta_bancaria ("joão", 100, "pio")
conta1.conta()

# conta = Conta_bancaria("João", 100, "juão")
# conta.depositar(50)  
# conta.depositar(-10)  
# conta.sacar(30)  
# conta.sacar(200) 

# conta = Conta_bancaria ("lu", 1000, "luani")
# conta.depositar(50)  
# conta.depositar(-10)  
# conta.sacar(1049)  
# conta.sacar(200) 
# conta.verificar_saldo()