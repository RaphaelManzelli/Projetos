

from cProfile import label
from cgitb import text
from distutils.command.build import build
from msilib.schema import Font
from tkinter import	messagebox
from shutil import copy2
from string import whitespace
from textwrap import fill
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import width

from pkg_resources import working_set
#####################################################################################################################################





    ### Apagar frame da pg boa vindas

def apagar():
    frame_baixo.destroy()
   
 


###Criar tela principal

def entrar():
    frame_principal= Frame(tl_abertura, width=800, height=450, bg='white' )
    frame_principal.grid(column=0, row=1 )
    ###Apagando frame
    apagar()
    

    ###Confidurando tela principal

    #
    texto_distancia=Label(frame_principal, text='Distâcia percorrida em KM:  ', bg='white', font= 'time, 11' ,padx=5 )
    texto_distancia.grid(column=0, row=0)
    #
    ipt_distacia=Entry(frame_principal, border= '2', relief=RAISED )
    ipt_distacia.grid(column=1, row=0)
    #
    texto_tempo=Label(frame_principal, text='Tempo aproximado em Minutos:', bg='white', font= 'time, 11',  )
    texto_tempo.grid(column=2, row=0, padx=11)
    #
    ipt_tempo=Entry(frame_principal, border= '2', relief=RAISED )
    ipt_tempo.grid(column=3, row=0)
    #
    texto_percuso=Label(frame_principal, text='Percuso:', bg='white', font= 'time, 11', pady=15 )
    texto_percuso.grid(column=1, row=1)
    #
   
    percurso=['ida', 'ida/volta']

    cmb_percuso=ttk.Combobox(frame_principal, values=percurso)
    cmb_percuso.current(0)
    cmb_percuso.grid(column=2, row=1)
    #

    texto_configuracao=Label(frame_principal, text= 'CONFIGURAÇÕES', bg='white', font='time, 15', pady=25)
    texto_configuracao.grid(column=2, row=2)
    #
    
    texto_preco=Label(frame_principal, text='Preço por L:  R$', font='time, 11', bg='white',pady=15  )
    texto_preco.grid(column=0 , row=3) 
    #
    ipt_preco=Entry(frame_principal, border=2, relief=RAISED)
    ipt_preco.grid(column=1, row=3)
    #
    texto_km=Label(frame_principal, text='KM/L:', bg='white', font='time, 11')
    texto_km.grid(column=2, row=3)
    #
    ipt_km=Entry(frame_principal, border=2, relief= RAISED )
    ipt_km.grid(column=3, row=3)
    #
    texto_hora=Label(frame_principal, text='Valor por H: R$', bg='white', font='time, 11',  )
    texto_hora.grid(column=0, row=4)
    #
    ipt_hora=Entry(frame_principal, border=2, relief=RAISED)
    ipt_hora.grid(column=1, row=4)
    #
    texto_porcentagem=Label(frame_principal, text='Ganho pelo combustível  %', bg='white', font='time, 11')
    texto_porcentagem.grid(column=2, row=4)
    #
    ipt_porcentagem=Entry(frame_principal, border=2, relief=RAISED)
    ipt_porcentagem.grid(column=3, row=4)
    #
    bt_calcular=Button(frame_principal, text='CALCULAR', bg='gray', relief=RAISED, width=25, command= calculos  )
    bt_calcular.grid(column=0, row=6, pady=75)
    #
    bt_limpar=Button(frame_principal, text='LIMPAR', bg='gray', relief=RAISED, width=25,command=entrar  )
    bt_limpar.grid(column=3, row=6, pady=75)
    #
    texto_calculos=Label(frame_principal,bg='white', font='time, 11'  )
    texto_calculos.grid(column=2, row=5)



### Tela Boa Vinda
tl_abertura=Tk()
tl_abertura.title('Calcula Frete V 1.0')
tl_abertura.geometry('800x550+150+5')
tl_abertura.iconbitmap('calcula frete/icone.ico')
tl_abertura.resizable(width=0, height=0)
tl_abertura.configure(background='white')


### Estrutura Tela Boa Vinda
###Dividindo Janela

frame_cima= Frame(tl_abertura, width=800, height=100, bg='white')
frame_cima.grid(column=0, row=0 )
#
frame_baixo= Frame(tl_abertura, width=800, height=450, bg='white')
frame_baixo.grid(column=0, row=1 )

# Configurar frames
txt_titulo=Label(frame_cima, text= 'SEJAM BEM VINDOS \nA CALCULADORA FRETE',  font='arial, 15', bg='white', fg="black")
txt_titulo.place(x=270, y=25)
#
img_logo= PhotoImage(file='calcula frete/Logo.png')
#
img_fundo=Label(frame_baixo, image= img_logo, relief=FLAT, )
img_fundo.place(x=75, y=50)

###Botão entrada
 
bt_abertura= Button(frame_baixo, width=15, height=2, text='ENTRAR',command=  entrar,   background='white', relief=RAISED )
bt_abertura.place(x=350, y= 390)




######################
tl_abertura.mainloop()
#FIM#

