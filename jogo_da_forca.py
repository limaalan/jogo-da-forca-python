import json
import random

#from numpy import correlate

#carrega o arquivo json na variável 
with open ('words.json','r') as f:
    dados = json.load(f)

def palavra_aleatoria ():
    #escolhe palavra aleatória para o jogo
    palavra= random.choice(dados['data'])
    print(palavra)
    return palavra

def jogo(palavra):

    vidas = 2
    corretos=0
    chutes=[] 
    chute = ''
    
    while ( corretos  < (len (palavra)) and vidas >0):

        chute = input("Digite uma letra :")
        #Caso o jogador já deu esse palpite
        if ( chute in chutes ):
            print("Você já deu esse palpite!",end="")

        #Caso contrário verifica se está na palavra
        else :
            chutes.append(chute) 

            if ( chute not in palavra):
                vidas -=1
            else :
                for i in palavra:
                    if (i in chutes):
                        print(i,end=" ")
                        if ( chute == i ):
                            corretos+=1
                    else :
                        print('-',end=" ")
            
            print(" vidas = ",vidas)
        #print(f"\ncorretos:{corretos}\n")

    if (vidas):
        print("Você ganhou !")
    else :
        print("Você perdeu!")      

def main():
    opt = ''
    while opt!='sair':
        palavra = palavra_aleatoria()
        jogo(palavra)

        opt = input("Continuar jogando ? digite 'sair' para sair : ")

main()

f.close