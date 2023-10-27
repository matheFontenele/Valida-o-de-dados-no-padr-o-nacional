import requests
# inicialização da classe Busca Endereço
class BuscaEndereco:

# Função principal de inicialização
    def __init__(self, cep): #
        cep = str(cep)
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError ('CEP invalido')
        
    def __str__(self):
        return self.format_cep()

# Função para validar se cep é valido por meio do tamanho 
    def cep_valido(self, cep): 
        if len(cep) == 8:
            return True
        else:
            return False
        
# Função para formatação dio CEP no padrão XXXXX.XXX
    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

# Função para acessar cep da API e retornar valo em JSON(retorna os dados em dicionario diferente do text que retorna em string)
    def acessa_api_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )