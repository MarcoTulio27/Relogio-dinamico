import os 
import random #para sortear números aleatórios
from colorama import Fore, Back, Style  #para usar cores será importado: Cor da frente, de fundo e estilo da fonte

#FUNÇÕES PRINCIPAIS que usarei: jogada do jogador, jogada do computador, verificar vitoria, redefinir o jogo pra jogar de novo, e tudo isso 
#em loop
#VARIÁVEIS GLOBAIS:
jogarNovamente = "sim"
jogadas = 0     #pra determinar numero de jogadas no jogo, jogo da  veia tem 9 jogadas no máximo
quemJoga = 2    #2 joga o humano e 1 joga o pc
maxJogadas = 9
vit = "nao"
velha = [       #é só uma lista em formato do jogo da velha, parece matriz
    [" ", " ", " "],    #primeira lista
    [" ", " ", " "],
    [" ", " ", " "]
]

#Função pra desenhar a tela:
def tela():
    global velha    #Variaveis globais dentro de loops devem vir com global antes, sem loops nao é obrigado
    global jogadas
    os.system("cls")    #pra limpar a tela
    print("    0   1   2")  #pode usar for também
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2]) #primeira linha da matriz
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("   -----------")
    print("Jogadas: " +  Fore.GREEN + str(jogadas) + Fore.RESET)

#Função das jogadas do jogador:
def jogadorJoga():
    global jogadas  #Variavei que vao ser precisas
    global quemJoga
    global maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:  #jogador vai digitar a linha e coluna
        
        try:                        #Pra ver se a jogada é valida
            l=int(input("Linha..: "))
            c=int(input("Coluna..: "))
            while velha[l][c]!= " ":    #Só sai desse loop se digitar uma linha e coluna válida
                l = int(input("Linha..: "))
                c = int(input("Coluna..: "))    
            velha[l][c] = "X"       #Vai preencher o espaço digitado pela pessoa
            quemJoga=1
            jogadas+=1
        except: #se digitar algo errado na coluna ou na linha, que nao seja os numeros delas
            print("Jogada invalida")
            os.system("pause")


#Funçaõ pra jogada do pc
def cpuJoga():
    global jogadas  
    global quemJoga
    
    global maxJogadas
    if quemJoga==1 and jogadas<maxJogadas:
            l = random.randrange(0,3)   #O pc vai digitar algo aleatorio de 0 a 2(sempre -1 que o tamanho total)
            c = random.randrange(0,3)
            while velha[l][c]!=" ": #O pc nao vai  ter erro de jogada, vai sortear até achar algo vazio
                l = random.randrange(0,3)   
                c = random.randrange(0,3)
            velha[l][c] = "O"
            jogadas+=1
            quemJoga = 2


#Função pra verificar vitoria:
#sao 3 probabilidades de vitoria, e 8 no total(8 pro humano e 8 pro pc) 3 pela coluna e pela linha e 2 pela diagonal
#Pode ser com if ou loop, ou se somar as posições de vitoria com +1, se a soma der 3 é vitoria

def verificarVitoria():
    global velha
    vitoria = "nao"
    simbolos = ["X", "O"]
    for s in simbolos:  #Vai percorrer tudo com s valendo X e depois com s valendo O
        vitoria = "nao"
        #Verificar vitoria em linhas
        indlinhas=indcolunas=0
        while indlinhas<3:
            soma = 0
            indcolunas = 0
            while indcolunas<3:
                if(velha[indlinhas][indcolunas]==s):    #Se a posiçao for igual a X ou O                               
                    soma+=1
                    indcolunas+=1
            
            if(soma==3):
                vitoria = s     #ganhou o X ou O
                break
            indlinhas+=1
        if(vitoria!="nao"):
            break
        #Verificar colunas
         indlinhas=indcolunas = 0
        while indcolunas<3:
            soma = 0
            indlinhas = 0
            while indlinhas<3:
                if(velha[indlinhas][indcolunas]==s):                           
                    soma+=1
                    indlinhas+=1
            
            if(soma==3):
                vitoria = s     
                break
            indcolunas+=1
        if(vitoria!="nao"):
            break
        #Verificando a Diagonal 1:
        soma = 0
        indiag = 0
        while indiag<3:     #diagonais [0][0], [1][1] e [2][2]
            if(velha[indiag][indiag]==s):                           
                    soma+=1
            indiag+=1
        if(soma==3):
            vitoria = s     
            break
        #Diagonal 2:
        soma = 0
        indiag = 0
        indiagcolun = 2
        while indiagcolun>=0:     #diagonais [0][0], [1][1] e [2][2]
            if(velha[indiag][indiagcolun]==s):                          
                    soma+=1
            indiag+=1
            indiagcolun-=1  #Vai voltando com as colunas
        if(soma==3):
            vitoria = s     
            break
    return vitoria


#Função para redefinir, inicializar todas as variáveis:
def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit

    jogadas = 0     
    quemJoga = 2    
    maxJogadas = 9
    vit = "nao"
    velha = [       
        [" ", " ", " "],    
        [" ", " ", " "],
        [" ", " ", " "]
    ]

                  


#A cada jogada vai fazer verificações, que eu jogo, o pc joga e refaz o jogo, tudo no loop principal 
while(jogarNovamente=="sim" or jogarNovamente=="SIM"):
    while True: #loop infinito, enquanto nao tiver break ele nao para, o jogo vai acontecer aqui dentro
        tela()  #chamar a tela, jogada do jogador, jogada do pc, ver a vitoria e refazer o joguinho
        jogadorJoga()
        cpuJoga()
        tela()
        vit = verificarVitoria()    #verificaVitoria pode retornar nao, X, O, 
        if(vit!="nao")or(jogadas>=maxJogadas):    #verificar as condições de vitoria
            break

    print(Fore.RED + "Fim de jogo" + Fore.YELLOW)    #Pra colorir a mensagem é pelo FORE
    if(vit=="X" or vit =="O"):
        print("Resultado: Jogador " + vit + " venceu")
    else:
        print("Resultado: Empate")
    jogarNovamente=input(Fore.BLUE + "Jogar novamente? [sim/nao]: " + Fore.WHITE)
    redefinir()