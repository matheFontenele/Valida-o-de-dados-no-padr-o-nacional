# Importação de biblioteca para validação de documentos
from validate_docbr import CPF, CNPJ, TituloEleitoral

class Documento: # classe mãe, principal
    @staticmethod
    def pega_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Documento invalido!")
        
# Classe CPF-------------------
class DocCpf:
    def __init__(self, documento): # Inicia a classe CPF
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF invalido!")
            
    def valida(self, documento): # Valida se o CPF esta nos padrões corretos
        validador = CPF()
        return validador.validate(documento)
    
    def formata(self): # Cria a mascara de formatação para o CPF
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    def __str__(self): # Retorna em string o CPF
        return self.formata()

# Classe CNPJ--------------------
class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ invalido!')
    
    def valida(self, documento): # Valida se o CNPJ esta nos padrões corretos
        validador = CNPJ()
        return validador.validate(documento)
    
    def formata(self): # Cria a mascara de formatação para o CPF
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    
    def __str__(self): # Retorna em string o CPF
        return self.formata()


