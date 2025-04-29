class calculadora:
    @staticmethod
    def somar(a, b): # método estatico
        return a + b 
    
resultado = calculadora.somar(10, 5) # chamada diretamente pela classe
print(resultado) # sáida: 15