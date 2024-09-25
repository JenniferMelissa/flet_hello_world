#terminal: pip install flet

import flet as  ft 

#sempre que o projeto usar flet precisa começar com os codigos abaixo: OBRIGATORIO, sem excessao
def main(page: ft.Page): #funcao sempre vai ter a 'main' e ela é a principal, para gerar ou criar outras fucoes, elas percisam ser geradas dentro da 'main', mesmo em casos de imports de funcoes
    page.title = 'Olá, mundo!' #titulo da janela
    page.scroll = 'adaptive' #forma como a margem vai se comportar na janela, tela se adapta

    #declaracao de variaveis
    #ft.TextField(label='Nome'):ft.TextField é input basico, gera uma caixinha de texto + (label='Nome'): nome da caixa de texto (SERVE PRA RECEBER VALORES, mas nao armazena em lugar nenhum)
    #porem, nesse caso, como esta usando uma variavel pra ela, está armazenando na memoria
    nome =  ft.TextField(label='Nome')

    #comeca a escrever depois do page.add(aqui dentro)
    page.add(
        #ft.Text: digitar texto

        #size = 30: tamanho da fonte em pixels
        #font_family='Times New Roman': altera o tipo da fonte
        #color=#ff0000' ou color='red': cor da fonte
        #weight='bold': deixou a frase em negrito
        ft.Text('Olá, mundo!', size=30, font_family='Times New Roman', color='pink',weight='bold'),
        nome,
        ft.TextButton('Clique aqui')
       
    ) 
    page.update() #sempre tem que ser a ultima coisa, isso que faz o page.add() funcionar

 #execucao do programa, janela é gerada aqui
ft.app(main)

#esse codigo ja é suficiente para gerar uma janela
########### termina aqui a obrigatoriedade da estrutura, codigo fonte (o que quero exibir) fica dentro dessa estrutura
#funciona para web, mobile e desktop, mas na hora de publicar que precisa definir onde voce vai publicar(web, mobile e desktop)