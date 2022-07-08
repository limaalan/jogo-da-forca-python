import json
import random
from visual import visual_ascii

#carrega o arquivo json na variável 
with open ('words.json','r') as f:
    dados = json.load(f)
f.close

def palavra_aleatoria ():
    #escolhe palavra aleatória para o jogo
    palavra= random.choice(dados['data'])
    #print(palavra)
    return palavra

# Função que revela apenas as letras que o jogador jogou , e informa as vidas restantes
def imprime_jogo(chutes, palavra,vidas):
    print("Seus palpites até aqui: ",end='')
    for j in chutes:
        print (j,end=' ')
    print("\n")
    for i in palavra :
        if i in chutes:
            print (i,end=' ')
        else :
            print('-',end=' ')
    print(visual_ascii[vidas])
    print("Vidas :",vidas)

#função que dada uma palavra e a quantidade de vidas, faz uma rodada do jogo da forca.
def jogo(palavra,vidas):

    corretos=0
    chutes=[] 
    chute = ''
    
    while ( corretos  < (len (palavra)) and vidas >0):
        imprime_jogo(chutes,palavra,vidas)
        chute = input("Digite uma letra :").lower()
        if (chute.isalpha() and len(chute)==1):
        
            #Caso o jogador já deu esse palpite
            if ( chute in chutes ):
                print("Você já deu esse palpite!")

            #Caso contrário verifica se está na palavra
            else :
                chutes.append(chute) 

                if ( chute in palavra):
                    for i in palavra:
                        if (chute ==i ):
                            corretos +=1
                else :
                    vidas -=1
                #print(" vidas = ",vidas)
            print("---------------------------------")
        else : 
            print("Digite somente uma letra.")


    if (vidas):
        imprime_jogo(chutes,palavra,vidas)
        print("Você ganhou ! a palavra era :",palavra)
    else :
        imprime_jogo(chutes,palavra,vidas)
        print("Você perdeu!, a palavra era :",palavra)  

def main():
    vidas=6
    opt = ''
    while opt!='sair':
        palavra = palavra_aleatoria()
        jogo(palavra,vidas)

        opt = input("Continuar jogando ? digite 'sair' para sair : ")
        print("---------------------------------------------------")

main()

