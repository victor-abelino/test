class Pessoa:
    populaçao = 0 #atributo de classe
    def __init__ (self,nome):
       self.nome = nome
       Pessoa.populaçao +=1
    
    @classmethod # metodo para acessar o cls
    def mostra_populaçao(cls): # método de classe
       print(f"Apopulação atual é {cls.populaçao}")

pessoa = Pessoa ("maria")
pessoa = Pessoa ("victor")
Pessoa.mostra_populaçao() #saída a população atual é