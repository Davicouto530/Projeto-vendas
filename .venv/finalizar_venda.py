# Importar os componentes para a construção da janela
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout, QMessageBox

#construção da class janela com o nome "caixa"

class FinalizarVenda(QWidget):
    #criação do metodo __init__ que inicia a janela e exibe ela na tela

    def __init__(self):
        super().__init__()
        
        #Vamos definir o tamanho e a posição da tela
        self.setGeometry(0,30,800,600)

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
        self.label_coluna.setStyleSheet("QLabel{}")

        # Criação de layout horizontal
        self.layout_h = QHBoxLayout()
        self.label_coluna.setLayout(self.layout_h)

        #Label coluna esquerda
        self.label_esquerda = QLabel()
        self.label_esquerda.setStyleSheet("QLabel{background-color:#d9d9d9}")
        self.label_esquerda.setFixedWidth(300)
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
        self.label_direita = QLabel("Cliente")
        self.label_direita.setStyleSheet("QLabel{background-color: #fff}")
        self.layout_h.addWidget(self.label_direita)







        




        self.layout_v.addWidget(self.label_coluna)




        #Rodape 

        self.label_rodape  = QLabel()
        self.label_rodape.setFixedHeight(100)
        self.label_rodape.setStyleSheet("QLabel{border-top:1px solid black}")
        self.layout_v.addWidget(self.label_rodape)







        #Adicionar o layout na tela
        self.setLayout(self.layout_v)

app = QApplication(sys.argv)
cx = FinalizarVenda()
cx.show()
app.exec_()