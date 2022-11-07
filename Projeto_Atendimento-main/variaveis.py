from Banco import Banco
from datetime import date

data = date.today().strftime("%d/%m/%Y")

#Abrindo arquivos do banco de dados
banco = Banco()
qtd_atendimentos = banco.current 
dados = banco.dados
qtd_h = dados.loc[dados["Data"] == data].count()
qtd_h = qtd_h[0]

#VARIAVEIS DE COR, TAMANHO E FONTE
largura = 1024
altura = 600

xLabels = 40
xEntrys = 165

yInicialCadastro = 50

entrysWidth = 30

cor = "grey13" 
cor_contraste = "white"
cor_meta = "orange red"
fonte_Titulos= ("Century Gothic",32)
fonte_Textos= ("Century Gothic",12)
fonte_Destaques= ("Century Gothic",24)
titulos = "META CERTIFICADO DIGITAL "

# LISTAS
lista_certificados = ['A1','A3 - TOKEN', 'A3 - CARTAO','A3 - TOKEN E CARTAO', 'NENHUM']
lista_solicitantes = ['AGR','CLIENTE']
lista_atendimentos = ["INSTALAÇÃO DRIVE",
            "INSTALAÇÃO CERTIFICADO",
            "PARAMETRIZAÇÃO",
            "EMISSÃO DE CERTIFICADO",
            "DESBLOQUEIO DE MÁQUINA",
            "DESBLOQUEIO PIN",
            "INICIALIZAÇÃO DE DISPOSITIVO",
            "SISAGR",
            "INVENTÁRIO DE MÁQUINA",
            "CRM",
            "JAVA",
            "MANUTENÇÕES",
            "CONECTIVIDADE",
            "E-SAJ",
            "PJE",
            "TJ",
            "IDENTIFICAÇÃO DE MÍDIA",
            "BIRDID",
            "ALTERAR SENHA",
            "A1 NÃO CONSTA",
            "EMISSOR DE NOTA",
            "DÚVIDA CERTIFICADO",
            "INSTALAÇÃO APLICATIVOS",
            "PERDA DE CERTIFICADO"
        ]