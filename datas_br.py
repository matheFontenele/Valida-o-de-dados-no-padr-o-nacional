from datetime import datetime, timedelta

# Inicialização da calsse Data
class DatasBR:
    def __init__(self):
        self.momento_cad = datetime.today()
        
    def __str__(self): # transformando a sainda do format_data em string
        return self.format_data()
        
    def mes_cad(self): # Função utilizando a biblioteca de datas para retornar um mes da lista
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        mes_cad = self.momento_cad.month
        return meses[mes_cad-1]
    
    def dia_semana(self): # Função utilizando a biblioteca de datas para retornar um dia da semana da lista
        dia_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado',]
        dia_cad = self.momento_cad.weekday()
        return dia_semana[dia_cad+1]
    
    def format_data(self): # Formatação da data retornada para um padrão escolhido com o metodfo strftime
        data_formatada =self.momento_cad.strftime('%d/%m/%Y as %H:%M')
        return data_formatada
    
    def tempo_cad(self): # Retornando tempo de cadastro do usuario com a biblioteca timedelta
        tempo_cad = (datetime.today() + timedelta(days=30)) - self.momento_cad
        return tempo_cad