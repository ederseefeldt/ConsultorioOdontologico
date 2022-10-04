from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic,QtWidgets

pacientes = [] #É importante que este vetor seja iniciado fora de uma função, pois assim, posso utilizar ele em qualquer parte do código

#Função que adiciona o nome digitado na lista quando o botão é apertado
def adicionar():
        nome_paciente = janela.nome_paciente.text()
        if (nome_paciente == ""):
            QMessageBox.warning(janela, "Alerta", "Nenhum nome inserido!")
        else:
            pacientes.append(nome_paciente) #Insere o nome do paciente do vetor
            janela.lista_pacientes.addItem(nome_paciente)
            janela.nome_paciente.setText("")
            janela.nome_paciente.setFocus()
        

#Função que fechar o sistema
def fechar():
    result = QMessageBox.question(janela, "Saindo do sistema", "Deseja mesmo sair do sistema?", QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        janela.close()

#Função que mostra todos os pacientes que foram inseridos, mesmo que eles ja tenham sido atendidos e saído das listas  
def mostrar():
    janela.lista_pacientes.clear()
    tam = len(pacientes) #lê o tamanho do vetor
    for i in range(tam):
        janela.lista_pacientes.addItem(pacientes[i])

#Função que limpa todas as listas    
def limpar():
    janela.lista_pacientes.clear()
    janela.lista_atendimento.clear()
    janela.nome_paciente.setFocus()

#Função que passa o paciente selecionado para a lista de atendimento
def atender():
    paciente = janela.lista_pacientes.currentItem().text()
    paciente_selecionado = janela.lista_pacientes.currentRow()
    janela.lista_pacientes.takeItem(paciente_selecionado)
    
    janela.lista_atendimento.clear()
    janela.lista_atendimento.addItem(paciente)
    
#Programa
app=QtWidgets.QApplication([])
janela=uic.loadUi("consultorio.ui")

#Chamadas das funções
janela.btn_adicionar.clicked.connect(adicionar)
janela.btn_fechar.clicked.connect(fechar)
janela.btn_mostrar.clicked.connect(mostrar)
janela.btn_limpar.clicked.connect(limpar)
janela.btn_atender.clicked.connect(atender)

#Chama a interface e executa o código
janela.show()
app.exec()