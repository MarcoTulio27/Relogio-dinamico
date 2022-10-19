from tkinter import *
import tkinter
from datetime import datetime #pega o calendario e horas

#CORES:
cor1 = "#3d3d3d"       #preto
cor2 = "#fafcff"     #branca 
cor3 = "#21c25c"    #verde
cor4 = "#eb463b"      #vermelho
cor5 = "#dedcdc"       #cinza
cor6 = "#3080f0"    #azul

fundo = cor1
cor = cor2


janela = Tk()
janela.title("")
janela.geometry("440x180")   #tamanho da janela
janela.resizable(width=FALSE, height=FALSE) #falso porque nao poderá alterar a altura e largura 
janela.configure(bg=cor1)

def relogio():
    tempo = datetime.now()        #vai guardar tudo relacionado a hora e o tempo

    hora = tempo.strftime("%H:%M:%S") #Pra obter a hora ao vivo
    diaSemana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")  #b minusculo abrevia o nome do mês, maiusculo da o nome completo
    ano = tempo.strftime("%Y")
    #Passando a hora pra label:
    l1.config(text=hora) #passando o text com a hora certa
    l1.after(200, relogio)  #Recursao pra tornar a hora dinamica, mudar ao vivo
    l2.config(text=diaSemana +"  " + str(dia) + "/" + str(mes) + "/" + str(ano))



l1 = Label(janela, text ="", font = ("Arial 80"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text ="", font = ("Arial 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()   #pra abrir a janelagit push -u origin main


