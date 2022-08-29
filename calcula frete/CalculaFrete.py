

from cProfile import label
from cgitb import text
from distutils.command.build import build
from msilib.schema import Font
from shutil import copy2
from string import whitespace
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import width

from pkg_resources import working_set



### Tela Principal
def bt_boa():
    tl_prinpal=Toplevel()
    tl_prinpal.title('Calcula Frete V 1.0')
    tl_prinpal.geometry('+150+5')
    tl_prinpal.iconbitmap('icone.ico')
    tl_prinpal.resizable(width=0, height=0)
    #
    txt_titulo1=Label(tl_prinpal, text='Olá essa é', font=('broadway, 25') )
    txt_titulo1.grid(column=0, row=0)
    #
    txt_titulo2=Label(tl_prinpal, text=' a sua ', font=('broadway, 25') )
    txt_titulo2.grid(column=1, row=0)
    #
    txt_titulo3=Label(tl_prinpal, text='calculadora ', font=('broadway, 25') )
    txt_titulo3.grid(column=2, row=0)
    #
    txt_titulo3=Label(tl_prinpal, text='de fretes', font=('broadway, 25') )
    txt_titulo3.grid(column=3, row=0)
    #
    bt_cadastro=Button(tl_prinpal, text='CADASTRO', padx=10, pady=10, background='white',command=cadastro    )
    bt_cadastro.grid(column=0, row=2, padx=10,pady=50, )
    #
    bt_calcular=Button(tl_prinpal, text='CALCULAR',padx=10, pady=10, background='white')
    bt_calcular.grid(column=1, row=2)
    #
    bt_limpar=Button(tl_prinpal, text='LIMPAR', padx=10, pady=10, background='white')
    bt_limpar.grid(column=2, row=2)
    #
    bt_sair=Button(tl_prinpal, text="SAIR",padx=10, pady=10, background='white', command=tl_abertura.destroy)
    bt_sair.grid(column=3, row=2)
    #
    check_ida=Checkbutton(tl_prinpal, text='Ida', )
    check_ida.grid(column=2, row=3)
    #
    check_volta=Checkbutton(tl_prinpal, text='ida/Volta')
    check_volta.grid(column=3, row=3)
    #
    txt_distancia=Label(tl_prinpal, text='Distância', font='arial, 15' )
    txt_distancia.grid(column=0, row=4)
    #
    ipt_distancia=Entry(tl_prinpal)
    ipt_distancia.grid(column=1, row=4)
    #
    txt_tempo=Label(tl_prinpal, text='Tempo \nem  minutos', font='arial, 15' )
    txt_tempo.grid(column=2, row=4)
    #
    ipt_tempo=Entry(tl_prinpal)
    ipt_tempo.grid(column=3, row=4)
    #
    txt_espaco1=Label(tl_prinpal)
    txt_espaco1.grid(column=0, row=5)
    #
    txt_resultado=Label(tl_prinpal, text='RESULTADOS', font='arial, 15')
    txt_resultado.grid(column=1, row=6)
    #
    txt_valor=Label(tl_prinpal, text='O valor a ser cobrado é dê:',font='arial, 13')
    txt_valor.grid(column=0, row=7)
    #
    ipt_valor=Entry(tl_prinpal)
    ipt_valor.grid(column=1, row=7)
    #
    txt_km=Label(tl_prinpal, text='Foram cobrado por KM:', font='arial, 13')
    txt_km.grid(column=2, row=7)
    #
    ipt_km=Entry(tl_prinpal)
    ipt_km.grid(column=3, row=7)
    #
    txt_minutos=Label(tl_prinpal, text='Foram cobrados por \nMinutos:', font='arial, 13')
    txt_minutos.grid(column=0, row=8)
    #
    ipt_minutos=Entry(tl_prinpal)
    ipt_minutos.grid(column=1, row=8)
    #
    txt_acrescimo=Label(tl_prinpal, text='Acrescimos', font='arial, 13')
    txt_acrescimo.grid(column=2, row=8)
   #
    ipt_acrescimo=Entry(tl_prinpal)
    ipt_acrescimo.grid(column=3, row=8)
    
   
   
   
   
    ###Tela de Cadastro
def cadastro():
    tl_cadastro=Toplevel()
    tl_cadastro.title('Cadastro ')
    tl_cadastro.geometry('+350+150')
    tl_cadastro.iconbitmap('icone.ico')
    tl_cadastro.resizable(width=0, height=0)
    #
   
    txt_nome=Label(tl_cadastro, text='Nome:' )
    txt_nome.grid(column=0, row=0, pady=10)
    #
    ipt_nome=Entry(tl_cadastro)
    ipt_nome.grid(column=1, row=0,  padx=5)
    #
    txt_veiculo=Label(tl_cadastro, text='Veículo:')
    txt_veiculo.grid(column=2, row=0)
    #
    listaveiculos=['Moto', 'Carro', 'Ultilitários', 'Caminhonete', 'Van', 'Caminhão']
    cmb_veiculo=ttk.Combobox(tl_cadastro, values=listaveiculos)
    cmb_veiculo.current(0)
    cmb_veiculo.grid(column=3, row=0)
    #
    txt_preco=Label(tl_cadastro, text='Preço Combustível')
    txt_preco.grid(column=0, row=1, pady=5)
    #
    ipt_preco=Entry(tl_cadastro)
    ipt_preco.grid(column=1, row=1 )
    #
    txt_prkm=Label(tl_cadastro, text='Km/L')
    txt_prkm.grid(column=2, row=1,pady=5  )
    # 
    ipt_prkm=Entry(tl_cadastro)
    ipt_prkm.grid(column=3, row=1)
    #
    txt_hora=Label(tl_cadastro, text='Preço por Hora')
    txt_hora.grid(column=0, row=2, pady=10 )
    #
    ipt_hora=Entry(tl_cadastro)
    ipt_hora.grid(column=1, row=2)
    #
    txt_porcentagem=Label(tl_cadastro, text= 'Combustível + %')
    txt_porcentagem.grid(column=2, row=2)
    #
    ipt_porcentagem=Entry(tl_cadastro)
    ipt_porcentagem.grid(column=3, row=2)
    #
    txt_espaco=Label(tl_cadastro)
    txt_espaco.grid(column=0, row=3)
    #
    bt_cadastrar=Button(tl_cadastro, text= 'Cadastrar',  background= 'grey', padx=20, pady=10 )
    bt_cadastrar.grid(column=0, row=5,)
    #
    bt_editar=Button(tl_cadastro, text='Editar',background= 'grey', padx=20, pady=10  )
    bt_editar.grid(column=1, row=5)
    #
    bt_cancelar=Button(tl_cadastro, text='Cancelar',background= 'grey', padx=20, pady=10 )
    bt_cancelar.grid(column=2, row=5)
    #
    bt_voltar=Button(tl_cadastro, text='Voltar', background= 'grey', padx=20, pady=10, command= tl_cadastro.destroy )
    bt_voltar.grid(column=3, row=5)
    
def apagar():
    frame_baixo.destroy()
    frame_cima.destroy()


def entrar():
    frame_principal= Frame(tl_abertura, width=800, height=550, )
    frame_principal.grid(column=0, row=0 )
    apagar()
    texto_test=Label(frame_principal, text='ola mundo ')
    texto_test.pack()

    

### Tela Boa Vinda
tl_abertura=Tk()
tl_abertura.title('Calcula Frete V 1.5')
tl_abertura.geometry('800x550+150+5')
tl_abertura.iconbitmap('icone.ico')
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



#
img_logo= PhotoImage(file='Logo.png')

img_fundo=Label(frame_baixo, image= img_logo, relief=FLAT, )
img_fundo.place(x=75, y=50)

###Botão entrada
 
bt_abertura= Button(frame_baixo, width=15, height=2, text='ENTRAR',command= apagar and entrar,   background='white', relief=RAISED )
bt_abertura.place(x=350, y= 390)



    










tl_abertura.mainloop()

