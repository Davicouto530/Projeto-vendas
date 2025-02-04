# Importar os componentes para a construção da janela
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout, QMessageBox, QComboBox, QSizePolicy

#construção da class janela com o nome "caixa"

class FinalizarVenda(QWidget):
    #criação do metodo __init__ que inicia a janela e exibe ela na tela

    def __init__(self):
        super().__init__()
        
        #Vamos definir o tamanho e a posição da tela
        self.setGeometry(0,30,700,500)

        # Criar o layout horizontal para as colunas
        self.layout_v = QVBoxLayout()

        #Vamos definir o titulo da nossa janela
        self.setWindowTitle("Finalizar venda")

        self.label_titulo = QLabel("Finalizar venda")
        self.label_titulo.setFixedHeight(80)
        self.label_titulo.setStyleSheet("QLabel{font-size:15pt;font-weight:bold;border:1px solid black}")
        self.layout_v.addWidget(self.label_titulo)

        #Label coluna esquerda
        self.label_coluna = QLabel()
        self.label_coluna.setStyleSheet("QLabel{margin:0px}")

        # Criação de layout horizontal
        self.layout_h = QHBoxLayout()
        self.label_coluna.setLayout(self.layout_h)

        #Label coluna esquerda
        self.label_esquerda = QLabel()
        self.label_esquerda.setStyleSheet("QLabel{background-color:#d9d9d9}")
        self.layout_h.addWidget(self.label_esquerda)

        # layout vertical de dentro do layout horizontal da esquerda
        self.l_v_esq = QVBoxLayout()
        self.label_esquerda.setLayout(self.l_v_esq)

        # Label do vertical de dentro do layout horizontal da esquerda
        self.label_v_2 = QLabel()
        self.l_v_esq.addWidget(self.label_v_2)

        # PRIMEIRO Layout horizontal de caixa de texto dentro do layout vertical "label_v_2" da esquerda
        self.l_cx_txt1 = QHBoxLayout()
        self.label_v_2.setLayout(self.l_cx_txt1)

        # Label para o nome total venda
        self.label_total_venda = QLabel("Total venda")
        self.l_cx_txt1.addWidget(self.label_total_venda)

        # Linedit para caixa de texto 1 total venda
        self.edit_total_venda = QLineEdit()
        self.edit_total_venda.setStyleSheet("QLineEdit{font-size:12pt}")
        self.l_cx_txt1.addWidget(self.edit_total_venda)

        # SEGUNDO Layout horizontal de caixa de texto dentro do layout vertical "label_v_2" da esquerda

        self.label_v_3 = QLabel()
        self.l_v_esq.addWidget(self.label_v_3)

        # SEGUNDO Layout horizontal de caixa de texto dentro do layout vertical "label_v_2" da esquerda
        self.l_cx_txt3 = QHBoxLayout()
        self.label_v_3.setLayout(self.l_cx_txt3)

        # Label para o desconto
        self.label_desconto = QLabel("Desconto:")
        self.l_cx_txt3.addWidget(self.label_desconto)

        # Linedit para caixa de texto 2 DESCONTO
        self.edit_desconto = QLineEdit()
        self.edit_desconto.setStyleSheet("QLineEdit{font-size:12pt}")
        self.l_cx_txt3.addWidget(self.edit_desconto)


        # TERCEIRO Layout horizontal de caixa de texto dentro do layout vertical "label_v_4" da esquerda

        self.label_v_4 = QLabel()
        self.l_v_esq.addWidget(self.label_v_4)

        # TERCEIRO Layout horizontal de caixa de texto dentro do layout vertical "label_v_4" da esquerda
        self.l_cx_txt4 = QHBoxLayout()
        self.label_v_4.setLayout(self.l_cx_txt4)

        # Label para o acrescimos
        self.label_acrescimos = QLabel("Acréscimo:")
        self.l_cx_txt4.addWidget(self.label_acrescimos)

        # Linedit para caixa de texto 3 acrescimos
        self.edit_acrescimos = QLineEdit()
        self.edit_acrescimos.setStyleSheet("QLineEdit{font-size:12pt}")
        self.l_cx_txt4.addWidget(self.edit_acrescimos)

        # QUARTO Layout horizontal de caixa de texto dentro do layout vertical "label_v_5" da esquerda

        self.label_v_5 = QLabel()
        self.l_v_esq.addWidget(self.label_v_5)

        # QUARTO Layout horizontal de caixa de texto dentro do layout vertical "label_v_5" da esquerda
        self.l_cx_txt5 = QHBoxLayout()
        self.label_v_5.setLayout(self.l_cx_txt5)

        # Label para o total liquido
        self.label_total_liquido = QLabel("Total liquido:")
        self.l_cx_txt5.addWidget(self.label_total_liquido)

        # Linedit para caixa de texto 5 total_liquido
        self.edit_total_liquido = QLineEdit()
        self.edit_total_liquido.setStyleSheet("QLineEdit{font-size:12pt}")
        self.l_cx_txt5.addWidget(self.edit_total_liquido)

        # QUARTO Layout horizontal de caixa de texto dentro do layout vertical "label_v_6" da esquerda

        self.label_v_6 = QLabel()
        self.l_v_esq.addWidget(self.label_v_6)

        # QUARTO Layout horizontal de caixa de texto dentro do layout vertical "label_v_6" da esquerda
        self.l_cx_txt6 = QHBoxLayout()
        self.label_v_6.setLayout(self.l_cx_txt6)

        # Label para o troco
        self.label_total_liquido = QLabel("Troco:")
        self.l_cx_txt6.addWidget(self.label_total_liquido)

        # Linedit para caixa de texto 6 total_liquido
        self.edit_total_liquido = QLineEdit()
        self.edit_total_liquido.setStyleSheet("QLineEdit{font-size:12pt}")
        self.l_cx_txt6.addWidget(self.edit_total_liquido)



        # Label coluna da direita
        self.label_direita = QLabel()
        self.label_direita.setStyleSheet("QLabel{background-color:#fff; margin: 0; padding: 0}")
        self.layout_h.addWidget(self.label_direita)

         # layout vertical de dentro do layout horizontal da direita
        self.l_v_dir = QVBoxLayout()
        self.label_direita.setLayout(self.l_v_dir)

        # Label do vertical de dentro do layout horizontal da direita
        self.label_v_direita1 = QLabel()
        self.l_v_dir.addWidget(self.label_v_direita1)

        # PRIMEIRO Layout horizontal de caixa de texto dentro do layout vertical "label_v_direita1" da direita
        self.l_cx_txt1_direita = QHBoxLayout()
        self.label_v_direita1.setLayout(self.l_cx_txt1_direita)

        # Label para o cliente
        self.label_cliente = QLabel("Cliente:")
        self.label_cliente.setStyleSheet("QLabel{ margin: 0px; padding: 0px}")
        self.l_cx_txt1_direita.addWidget(self.label_cliente)

        # Linedit para caixa de texto 1 de cliente
        self.edit_cliente = QLineEdit()
        self.edit_cliente.setStyleSheet("QLineEdit{font-size:12pt}")
        self.l_cx_txt1_direita.addWidget(self.edit_cliente)



        # SEGUNDO Layout horizontal de caixa de texto dentro do layout vertical "label_v_2" da esquerda

        self.label_v_direita2 = QLabel()
        self.l_v_dir.addWidget(self.label_v_direita2)

        # SEGUNDO Layout horizontal de caixa de texto dentro do layout vertical "label_v_2" da esquerda
        self.l_cx_txt2_direita = QHBoxLayout()
        self.label_v_direita2.setLayout(self.l_cx_txt2_direita)

        # Label para o vendedor
        self.label_vendedor = QLabel("Vendedor:")
        self.l_cx_txt2_direita.addWidget(self.label_vendedor)

        # Linedit para caixa de texto 2 vendedor
        self.edit_vendedor = QLineEdit()
        self.edit_vendedor.setStyleSheet("QLineEdit{font-size:12pt}")
        self.l_cx_txt2_direita.addWidget(self.edit_vendedor)

        

        # TERCEIRO Layout horizontal de caixa de texto dentro do layout vertical "label_v_2" da esquerda

        self.label_v_direita3 = QLabel()
        self.l_v_dir.addWidget(self.label_v_direita3)

        # TERCEIRO Layout horizontal de caixa de texto dentro do layout vertical "label_v_2" da esquerda
        self.l_cx_txt3_direita = QHBoxLayout()
        self.label_v_direita3.setLayout(self.l_cx_txt3_direita)

        # Label para o forma de pagamento
        self.label_pagamento = QLabel("Forma de pag:")
        self.l_cx_txt3_direita.addWidget(self.label_pagamento)

        # Linedit para caixa de texto 3 forma de pagamento
        self.edit_pagamento = QComboBox()
        self.edit_pagamento.setStyleSheet("QLineEdit{font-size:12pt}")
        self.l_cx_txt3_direita.addWidget(self.edit_pagamento)

        # Linedit para caixa de texto 3 forma de pagamento
        self.edit_pagamento = QLineEdit()
        self.edit_pagamento.setStyleSheet("QLineEdit{font-size:12pt}")
        self.l_cx_txt3_direita.addWidget(self.edit_pagamento)


        # TERCEIRO Layout horizontal de caixa de texto dentro do layout vertical "label_v_2" da esquerda

        self.label_v_direita4 = QLabel()
        self.l_v_dir.addWidget(self.label_v_direita4)

        # QUARTO Layout horizontal de caixa de texto dentro do layout vertical "label_v_2" da esquerda
        self.l_cx_txt4_direita = QHBoxLayout()
        self.label_v_direita4.setLayout(self.l_cx_txt4_direita)

        # Label para o resumo
        self.label_resumo = QLabel()
        self.l_cx_txt4_direita.addWidget(self.label_resumo)

        # Linedit para caixa de texto 4 resumo
        self.edit_resumo = QLineEdit()
        self.edit_resumo.setStyleSheet("QLineEdit{font-size:12pt; height:100px}")
        self.edit_resumo.setFixedHeight(100)
        self.l_cx_txt4_direita.addWidget(self.edit_resumo)


        self.label_espaco = QLabel("")

        self.label_v_direita_espaco = QLabel()
        self.l_v_dir.addWidget(self.label_v_direita_espaco)

        # TERCEIRO Layout horizontal de caixa de texto dentro do layout vertical "label_v_2" da esquerda
        self.l_cx_txt_espaco_direita = QHBoxLayout()
        self.label_v_direita3.setLayout(self.l_cx_txt3_direita)

        # Label para o forma de pagamento
        self.l_cx_txt3_direita.addWidget(self.label_espaco)

        




        self.layout_v.addWidget(self.label_coluna)




        #Rodape 

        self.label_rodape  = QLabel('')
        self.label_rodape.setFixedHeight(100)
        self.layout_v.addWidget(self.label_rodape)

        self.layout_horizontal_rodape = QHBoxLayout()
        self.label_rodape.setLayout(self.layout_horizontal_rodape)
        
        self.label_rodape_1 = QLabel()
        self.layout_horizontal_rodape.addWidget(self.label_rodape_1)

        self.layout_v_rodape1 = QVBoxLayout()
        self.label_rodape_1.setLayout(self.layout_v_rodape1)

        self.bottom_1 = QPushButton('(Esc) Sair')
        self.layout_v_rodape1.addWidget(self.bottom_1)

        
        
        
        self.label_rodape_2 = QLabel()
        self.layout_horizontal_rodape.addWidget(self.label_rodape_2)

        
        self.layout_v_rodape_2 = QVBoxLayout()
        self.label_rodape_2.setLayout(self.layout_v_rodape_2)

        self.label_text = QLabel("Selecione o documento para emissão:")
        self.label_text.setStyleSheet("QLabel")
        self.layout_v_rodape_2.addWidget(self.label_text)

        self.bottom_2 = QPushButton('(F6)Cupom Fiscal')
        self.layout_v_rodape_2.addWidget(self.bottom_2)

        
        self.bottom_3 = QPushButton('(F6)Cupom Fiscal')
        self.layout_v_rodape_2.addWidget(self.bottom_3)










        self.label_rodape_3 = QLabel()
        self.layout_horizontal_rodape.addWidget(self.label_rodape_3)

        
        self.layout_v_rodape_3 = QVBoxLayout()
        self.label_rodape_3.setLayout(self.layout_v_rodape_3)

        self.bottom_4 = QPushButton('(F7)Pedido de Venda')
        self.layout_v_rodape_3.addWidget(self.bottom_4)

        self.bottom_5 = QPushButton('(F9)NFC-e Offline')
        self.layout_v_rodape_3.addWidget(self.bottom_5)



     


        #Adicionar o layout na tela
        self.setLayout(self.layout_v)

app = QApplication(sys.argv)
cx = FinalizarVenda()
cx.show()
app.exec_()