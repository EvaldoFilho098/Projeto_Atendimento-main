import pandas as pd

class Banco():
    
    def __init__(self):
        try:
            self.dados = pd.read_csv('Atendimento.csv')
        except:
            self.createTable()
        
        self.current = self.dados.shape[0]

    def createTable(self):
        self.dados = pd.DataFrame(columns=['Id','Local','Solicitante','Atendimento','Certificado','Meta','Resolvido','Data'])

    def Save(self):
        self.dados.to_csv('Atendimento.csv', index=False)
    
    def Atualiza(self):
        self.Save()
        self.dados = pd.read_csv('Atendimento.csv')
        self.current = self.dados.shape[0]