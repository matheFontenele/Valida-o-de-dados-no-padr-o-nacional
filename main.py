"""
from cpf_cnpj import Documento

from validate_docbr import CNPJ
cpf_exemplo = '06965770384'
cnpj_exemplo = '60701190000104'
titulo_exemplo = '088527620701'

documento = Documento.pega_documento(titulo_exemplo)
print(documento)
"""

"""
from telefonesBr import TelefonesBr
import re

telefone = "05585933000400"
telefone_objeto = TelefonesBr(telefone)

print(telefone_objeto)
"""

"""
from datas_br import DatasBR

cad = DatasBR()
print(cad)
"""

"""
from datetime import datetime, timedelta
from datas_br import DatasBR

hoje =  DatasBR()
print(hoje.tempo_cad())
"""

import requests
from acesso_cep import BuscaEndereco
cep = 60510188
obj_cep = BuscaEndereco(cep)
bairro, cidade, uf = obj_cep.acessa_api_cep()

print(bairro, cidade, uf)