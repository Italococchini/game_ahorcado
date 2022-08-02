import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import pathlib
import random
from PIL import Image

class App:
    
    # GUI
    def __init__(self, root):     

        # Configuracion 
        self.listado_palabras = []
        self.listado_img= {
            "I0",
            "I1",
            "I2",
            "I3",
            "I4",
            "I5"
        }
        self.path = pathlib.Path(__file__).parent.absolute()
        root.title("El Ahorcado")
        width=600
        height=520
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Estilos
        ft = tkFont.Font(family='Arial',size=10)
        FTitle = tkFont.Font(family='Arial',size=16)
        bgColor = "#efefef"
        fg = "#000000"
        justify = "center"
        GB_width = 70
        GB_height = 25
        Position_Y = 60

        # Titulos
        GLabel_titulo=tk.Label(root)
        GLabel_titulo["font"] = ft
        GLabel_titulo["fg"] = "#333333"
        GLabel_titulo["justify"] = justify
        GLabel_titulo["text"] = "Palabra Secreta"
        GLabel_titulo.place(x=10,y=10,width=width,height=30)
        GLabel_titulo.config(bg="white")

        GLabel_Oportunidades=tk.Label(root)
        GLabel_Oportunidades["font"] = ft
        GLabel_Oportunidades["fg"] = "#333333"
        GLabel_Oportunidades["justify"] = justify
        GLabel_Oportunidades["text"] = "Vidas disponibles: "
        GLabel_Oportunidades.place(x=270,y=Position_Y+30,width=231,height=30)
        GLabel_Oportunidades.config(bg="white")

        self.GLabel_Vidas=tk.Label(root)
        self.GLabel_Vidas["font"] = ft
        self.GLabel_Vidas["fg"] = "#333333"
        self.GLabel_Vidas["justify"] = justify
        self.GLabel_Vidas["text"] = "5"
        self.GLabel_Vidas.place(x=270,y=Position_Y+60,width=231,height=30)
        self.GLabel_Vidas.config(bg="white")

        GLabel_Alfabeto=tk.Label(root)
        GLabel_Alfabeto["font"] = ft
        GLabel_Alfabeto["fg"] = "#333333"
        GLabel_Alfabeto["justify"] = justify
        GLabel_Alfabeto["text"] = "Alfabeto"
        GLabel_Alfabeto.place(x=20,y=Position_Y+30,width=231,height=30)
        GLabel_Alfabeto.config(bg="white")

        self.GLabel_Palabra=tk.Label(root)
        self.GLabel_Palabra["font"] = FTitle
        self.GLabel_Palabra["fg"] = "#333333"
        self.GLabel_Palabra["justify"] = justify
        self.GLabel_Palabra["text"] = ""
        self.GLabel_Palabra.place(x=10,y=50, width=width-10)
        self.GLabel_Palabra.config(bg="white")

        # Elementos - Alfabeto
        self.GButton_A=tk.Button(root)
        self.GButton_A["bg"] = bgColor
        self.GButton_A["font"] = ft
        self.GButton_A["fg"] = fg
        self.GButton_A["justify"] = justify
        self.GButton_A["text"] = "A"
        self.GButton_A.place(x=20,y=Position_Y+60,width=GB_width,height=GB_height)
        self.GButton_A["command"] = self.GButton_A_command
        self.GButton_A['state'] = tk.DISABLED

        self.GButton_B=tk.Button(root)
        self.GButton_B["bg"] = bgColor
        self.GButton_B["font"] = ft
        self.GButton_B["fg"] = fg
        self.GButton_B["justify"] = justify
        self.GButton_B["text"] = "B"
        self.GButton_B.place(x=100,y=Position_Y+60,width=GB_width,height=GB_height)
        self.GButton_B["command"] = self.GButton_B_command
        self.GButton_B['state'] = tk.DISABLED

        self.GButton_C=tk.Button(root)
        self.GButton_C["bg"] = bgColor
        self.GButton_C["font"] = ft
        self.GButton_C["fg"] = fg
        self.GButton_C["justify"] = justify
        self.GButton_C["text"] = "C"
        self.GButton_C.place(x=180,y=Position_Y+60,width=GB_width,height=GB_height)
        self.GButton_C["command"] = self.GButton_C_command
        self.GButton_C['state'] = tk.DISABLED

        self.GButton_D=tk.Button(root)
        self.GButton_D["bg"] = bgColor
        self.GButton_D["font"] = ft
        self.GButton_D["fg"] = fg
        self.GButton_D["justify"] = justify
        self.GButton_D["text"] = "D"
        self.GButton_D.place(x=20,y=Position_Y+90,width=GB_width,height=GB_height)
        self.GButton_D["command"] = self.GButton_D_command
        self.GButton_D['state'] = tk.DISABLED

        self.GButton_E=tk.Button(root)
        self.GButton_E["bg"] = bgColor
        self.GButton_E["font"] = ft
        self.GButton_E["fg"] = fg
        self.GButton_E["justify"] = justify
        self.GButton_E["text"] = "E"
        self.GButton_E.place(x=100,y=Position_Y+90,width=GB_width,height=GB_height)
        self.GButton_E["command"] = self.GButton_E_command
        self.GButton_E['state'] = tk.DISABLED

        self.GButton_F=tk.Button(root)
        self.GButton_F["bg"] = bgColor
        self.GButton_F["font"] = ft
        self.GButton_F["fg"] = fg
        self.GButton_F["justify"] = justify
        self.GButton_F["text"] = "F"
        self.GButton_F.place(x=180,y=Position_Y+90,width=GB_width,height=GB_height)
        self.GButton_F["command"] = self.GButton_F_command
        self.GButton_F['state'] = tk.DISABLED

        self.GButton_G=tk.Button(root)
        self.GButton_G["bg"] = bgColor
        self.GButton_G["font"] = ft
        self.GButton_G["fg"] = fg
        self.GButton_G["justify"] = justify
        self.GButton_G["text"] = "G"
        self.GButton_G.place(x=20,y=Position_Y+120,width=GB_width,height=GB_height)
        self.GButton_G["command"] = self.GButton_G_command
        self.GButton_G['state'] = tk.DISABLED

        self.GButton_H=tk.Button(root)
        self.GButton_H["bg"] = bgColor
        self.GButton_H["font"] = ft
        self.GButton_H["fg"] = fg
        self.GButton_H["justify"] = justify
        self.GButton_H["text"] = "H"
        self.GButton_H.place(x=100,y=Position_Y+120,width=GB_width,height=GB_height)
        self.GButton_H["command"] = self.GButton_H_command
        self.GButton_H['state'] = tk.DISABLED

        self.GButton_I=tk.Button(root)
        self.GButton_I["bg"] = bgColor
        self.GButton_I["font"] = ft
        self.GButton_I["fg"] = fg
        self.GButton_I["justify"] = justify
        self.GButton_I["text"] = "I"
        self.GButton_I.place(x=180,y=Position_Y+120,width=GB_width,height=GB_height)
        self.GButton_I["command"] = self.GButton_I_command
        self.GButton_I['state'] = tk.DISABLED

        self.GButton_J=tk.Button(root)
        self.GButton_J["bg"] = bgColor
        self.GButton_J["font"] = ft
        self.GButton_J["fg"] = fg
        self.GButton_J["justify"] = justify
        self.GButton_J["text"] = "J"
        self.GButton_J.place(x=20,y=Position_Y+150,width=GB_width,height=GB_height)
        self.GButton_J["command"] = self.GButton_J_command
        self.GButton_J['state'] = tk.DISABLED

        self.GButton_M=tk.Button(root)
        self.GButton_M["bg"] = bgColor
        self.GButton_M["font"] = ft
        self.GButton_M["fg"] = fg
        self.GButton_M["justify"] = justify
        self.GButton_M["text"] = "M"
        self.GButton_M.place(x=20,y=Position_Y+180,width=GB_width,height=GB_height)
        self.GButton_M["command"] = self.GButton_M_command
        self.GButton_M['state'] = tk.DISABLED

        self.GButton_P=tk.Button(root)
        self.GButton_P["bg"] = bgColor
        self.GButton_P["font"] = ft
        self.GButton_P["fg"] = fg
        self.GButton_P["justify"] = justify
        self.GButton_P["text"] = "P"
        self.GButton_P.place(x=100,y=Position_Y+210,width=GB_width,height=GB_height)
        self.GButton_P["command"] = self.GButton_P_command
        self.GButton_P['state'] = tk.DISABLED

        self.GButton_S=tk.Button(root)
        self.GButton_S["bg"] = bgColor
        self.GButton_S["font"] = ft
        self.GButton_S["fg"] = fg
        self.GButton_S["justify"] = justify
        self.GButton_S["text"] = "S"
        self.GButton_S.place(x=100,y=Position_Y+240,width=GB_width,height=GB_height)
        self.GButton_S["command"] = self.GButton_S_command
        self.GButton_S['state'] = tk.DISABLED

        self.GButton_V=tk.Button(root)
        self.GButton_V["bg"] = bgColor
        self.GButton_V["font"] = ft
        self.GButton_V["fg"] = fg
        self.GButton_V["justify"] = justify
        self.GButton_V["text"] = "V"
        self.GButton_V.place(x=100,y=Position_Y+270,width=GB_width,height=GB_height)
        self.GButton_V["command"] = self.GButton_V_command
        self.GButton_V['state'] = tk.DISABLED

        self.GButton_Y=tk.Button(root)
        self.GButton_Y["bg"] = bgColor
        self.GButton_Y["font"] = ft
        self.GButton_Y["fg"] = fg
        self.GButton_Y["justify"] = justify
        self.GButton_Y["text"] = "Y"
        self.GButton_Y.place(x=100,y=Position_Y+300,width=GB_width,height=GB_height)
        self.GButton_Y["command"] = self.GButton_Y_command
        self.GButton_Y['state'] = tk.DISABLED

        self.GButton_K=tk.Button(root)
        self.GButton_K["bg"] = bgColor
        self.GButton_K["font"] = ft
        self.GButton_K["fg"] = fg
        self.GButton_K["justify"] = justify
        self.GButton_K["text"] = "K"
        self.GButton_K.place(x=100,y=Position_Y+150,width=GB_width,height=GB_height)
        self.GButton_K["command"] = self.GButton_K_command
        self.GButton_K['state'] = tk.DISABLED

        self.GButton_N=tk.Button(root)
        self.GButton_N["bg"] = bgColor
        self.GButton_N["font"] = ft
        self.GButton_N["fg"] = fg
        self.GButton_N["justify"] = justify
        self.GButton_N["text"] = "N"
        self.GButton_N.place(x=100,y=Position_Y+180,width=GB_width,height=GB_height)
        self.GButton_N["command"] = self.GButton_N_command
        self.GButton_N['state'] = tk.DISABLED

        self.GButton_Q=tk.Button(root)
        self.GButton_Q["bg"] = bgColor
        self.GButton_Q["font"] = ft
        self.GButton_Q["fg"] = fg
        self.GButton_Q["justify"] = justify
        self.GButton_Q["text"] = "Q"
        self.GButton_Q.place(x=180,y=Position_Y+210,width=GB_width,height=GB_height)
        self.GButton_Q["command"] = self.GButton_Q_command
        self.GButton_Q['state'] = tk.DISABLED

        self.GButton_T=tk.Button(root)
        self.GButton_T["bg"] = bgColor
        self.GButton_T["font"] = ft
        self.GButton_T["fg"] = fg
        self.GButton_T["justify"] = justify
        self.GButton_T["text"] = "T"
        self.GButton_T.place(x=180,y=Position_Y+240,width=GB_width,height=GB_height)
        self.GButton_T["command"] = self.GButton_T_command
        self.GButton_T['state'] = tk.DISABLED

        self.GButton_W=tk.Button(root)
        self.GButton_W["bg"] = bgColor
        self.GButton_W["font"] = ft
        self.GButton_W["fg"] = fg
        self.GButton_W["justify"] = justify
        self.GButton_W["text"] = "W"
        self.GButton_W.place(x=180,y=Position_Y+270,width=GB_width,height=GB_height)
        self.GButton_W["command"] = self.GButton_W_command
        self.GButton_W['state'] = tk.DISABLED

        self.GButton_Z=tk.Button(root)
        self.GButton_Z["bg"] = bgColor
        self.GButton_Z["font"] = ft
        self.GButton_Z["fg"] = fg
        self.GButton_Z["justify"] = justify
        self.GButton_Z["text"] = "Z"
        self.GButton_Z.place(x=180,y=Position_Y+300,width=GB_width,height=GB_height)
        self.GButton_Z["command"] = self.GButton_Z_command
        self.GButton_Z['state'] = tk.DISABLED

        self.GButton_L=tk.Button(root)
        self.GButton_L["bg"] = bgColor
        self.GButton_L["font"] = ft
        self.GButton_L["fg"] = fg
        self.GButton_L["justify"] = justify
        self.GButton_L["text"] = "L"
        self.GButton_L.place(x=180,y=Position_Y+150,width=GB_width,height=GB_height)
        self.GButton_L["command"] = self.GButton_L_command
        self.GButton_L['state'] = tk.DISABLED

        self.GButton_O=tk.Button(root)
        self.GButton_O["bg"] = bgColor
        self.GButton_O["font"] = ft
        self.GButton_O["fg"] = fg
        self.GButton_O["justify"] = justify
        self.GButton_O["text"] = "O"
        self.GButton_O.place(x=20,y=Position_Y+210,width=GB_width,height=GB_height)
        self.GButton_O["command"] = self.GButton_O_command
        self.GButton_O['state'] = tk.DISABLED

        self.GButton_U=tk.Button(root)
        self.GButton_U["bg"] = bgColor
        self.GButton_U["font"] = ft
        self.GButton_U["fg"] = fg
        self.GButton_U["justify"] = justify
        self.GButton_U["text"] = "U"
        self.GButton_U.place(x=20,y=Position_Y+270,width=GB_width,height=GB_height)
        self.GButton_U["command"] = self.GButton_U_command
        self.GButton_U['state'] = tk.DISABLED

        self.GButton_X=tk.Button(root)
        self.GButton_X["bg"] = bgColor
        self.GButton_X["font"] = ft
        self.GButton_X["fg"] = fg
        self.GButton_X["justify"] = justify
        self.GButton_X["text"] = "X"
        self.GButton_X.place(x=20,y=Position_Y+300,width=GB_width,height=GB_height)
        self.GButton_X["command"] = self.GButton_X_command
        self.GButton_X['state'] = tk.DISABLED

        self.GButton_ENIE=tk.Button(root)
        self.GButton_ENIE["bg"] = bgColor
        self.GButton_ENIE["font"] = ft
        self.GButton_ENIE["fg"] = fg
        self.GButton_ENIE["justify"] = justify
        self.GButton_ENIE["text"] = "Ñ"
        self.GButton_ENIE.place(x=180,y=Position_Y+180,width=GB_width,height=GB_height)
        self.GButton_ENIE["command"] = self.GButton_ENIE_command
        self.GButton_ENIE['state'] = tk.DISABLED

        self.GButton_R=tk.Button(root)
        self.GButton_R["bg"] = bgColor
        self.GButton_R["font"] = ft
        self.GButton_R["fg"] = fg
        self.GButton_R["justify"] = justify
        self.GButton_R["text"] = "R"
        self.GButton_R.place(x=20,y=Position_Y+240,width=GB_width,height=GB_height)
        self.GButton_R["command"] = self.GButton_R_command
        self.GButton_R['state'] = tk.DISABLED

        # self.GButton_ESP=tk.Button(root)
        # self.GButton_ESP["bg"] = bgColor
        # self.GButton_ESP["font"] = ft
        # self.GButton_ESP["fg"] = fg
        # self.GButton_ESP["justify"] = justify
        # self.GButton_ESP["text"] = "ESPACIO"
        # self.GButton_ESP.place(x=20,y=Position_Y+330,width=GB_width * 3 + 20,height=GB_height)
        # self.GButton_ESP["command"] = self.GButton_ESP_command
        # self.GButton_ESP['state'] = tk.DISABLED

        # Agregar nuevas palabras
        GLabel_NewWord=tk.Label(root)
        GLabel_NewWord["font"] = ft
        GLabel_NewWord["fg"] = "#333333"
        GLabel_NewWord["justify"] = justify
        GLabel_NewWord["text"] = "Agregar Palabra Secreta"
        GLabel_NewWord.place(x=20,y=Position_Y+350,width=GB_width * 5,height=GB_height)
        GLabel_NewWord.config(bg="white")

        self.TNewWord=tk.Entry(root)
        self.TNewWord["bg"] = bgColor
        self.TNewWord["font"] = ft
        self.TNewWord["fg"] = fg
        self.TNewWord["justify"] = tk.LEFT
        self.TNewWord.place(x=20,y=Position_Y+380,width=GB_width * 5,height=GB_height)
        self.TNewWord['state'] = tk.NORMAL

        self.GButton_Add=tk.Button(root)
        self.GButton_Add["bg"] = bgColor
        self.GButton_Add["font"] = ft
        self.GButton_Add["fg"] = fg
        self.GButton_Add["justify"] = justify
        self.GButton_Add["text"] = "Agregar"
        self.GButton_Add.place(x=390,y=Position_Y+380,width=GB_width,height=GB_height)
        self.GButton_Add["command"] = self.GButton_Add_command
        self.GButton_Add['state'] = tk.DISABLED

        self.GButton_DelAll=tk.Button(root)
        self.GButton_DelAll["bg"] = bgColor
        self.GButton_DelAll["font"] = ft
        self.GButton_DelAll["fg"] = fg
        self.GButton_DelAll["justify"] = justify
        self.GButton_DelAll["text"] = "Eliminar Todo"
        self.GButton_DelAll.place(x=470,y=Position_Y+380,height=GB_height)
        self.GButton_DelAll["command"] = self.GButton_DelAll_command
        self.GButton_DelAll['state'] = tk.DISABLED

        self.GButton_startGame=tk.Button(root)
        self.GButton_startGame["bg"] = bgColor
        self.GButton_startGame["font"] = ft
        self.GButton_startGame["fg"] = fg
        self.GButton_startGame["justify"] = justify
        self.GButton_startGame["text"] = "¡INICIAR JUEGO!"
        self.GButton_startGame.place(x=20,y=Position_Y+410,width=width-40,height=GB_height + 10)
        self.GButton_startGame["command"] = self.startGame
        self.GButton_startGame['state'] = tk.NORMAL


        self.Img = tk.PhotoImage(file="5.jpg")
        self.labelImg = tk.Label(root, image=self.Img)
        self.labelImg.place(x=300,y=180)

    # Actions

    # def GButton_ESP_command(self):
    #     self.Select_Option(self.GButton_ESP, " ")

    def GButton_Add_command(self):
        word = self.TNewWord.get()
        if word != '':
            words = list(word)
            invalidaChar = False
            for letter in words:
                if letter.upper() not in [" ","A","B","C","D","E","F","G","H","I","J","M","P","S","V","Y","K","N","Q","T","W","Z","L","O","U","X","Ñ","R"]:
                    invalidaChar = True
            if len(word) > 25:
                messagebox.showinfo(title=None, message="La palabra secreta debe contener un maximo de 25 caracteres '" + word + "'" )
            elif invalidaChar:
                messagebox.showinfo(title=None, message="Se detectaron caracteres invalidos, debe ingresar caracteres alfabeticos desde la A hasta la Z" )
            else:
                self.listado_palabras.append( word.upper() )
                messagebox.showinfo(title=None, message="Se agrego la palabra '" + word + "'" )
        else:
            messagebox.showinfo(title=None, message="No se pudo agregar la palabra secreta" )
        print(self.listado_palabras)

    def GButton_DelAll_command(self):
        self.listado_palabras = []

    def GButton_A_command(self):
        self.Select_Option(self.GButton_A, "A")

    def GButton_B_command(self):
        self.Select_Option(self.GButton_B, "B")

    def GButton_C_command(self):
        self.Select_Option(self.GButton_C, "C")

    def GButton_D_command(self):
        self.Select_Option(self.GButton_D, "D")

    def GButton_E_command(self):
        self.Select_Option(self.GButton_E, "E")

    def GButton_F_command(self):
        self.Select_Option(self.GButton_F, "F")

    def GButton_G_command(self):
        self.Select_Option(self.GButton_G, "G")

    def GButton_H_command(self):
        self.Select_Option(self.GButton_H, "H")

    def GButton_I_command(self):
        self.Select_Option(self.GButton_I, "I")

    def GButton_J_command(self):
        self.Select_Option(self.GButton_J, "J")

    def GButton_M_command(self):
        self.Select_Option(self.GButton_M, "M")

    def GButton_P_command(self):
        self.Select_Option(self.GButton_P, "P")

    def GButton_S_command(self):
        self.Select_Option(self.GButton_S, "S")

    def GButton_V_command(self):
        self.Select_Option(self.GButton_V, "V")

    def GButton_Y_command(self):
        self.Select_Option(self.GButton_Y, "Y")

    def GButton_K_command(self):
        self.Select_Option(self.GButton_K, "K")

    def GButton_N_command(self):
        self.Select_Option(self.GButton_N, "N")

    def GButton_Q_command(self):
        self.Select_Option(self.GButton_Q, "Q")

    def GButton_T_command(self):
        self.Select_Option(self.GButton_T, "T")

    def GButton_W_command(self):
        self.Select_Option(self.GButton_W, "W")

    def GButton_Z_command(self):
        self.Select_Option(self.GButton_Z, "Z")

    def GButton_L_command(self):
        self.Select_Option(self.GButton_L, "L")

    def GButton_O_command(self):
        self.Select_Option(self.GButton_O, "O")

    def GButton_U_command(self):
        self.Select_Option(self.GButton_U, "U")

    def GButton_X_command(self):
        self.Select_Option(self.GButton_X, "X")

    def GButton_ENIE_command(self):
        self.Select_Option(self.GButton_ENIE, "Ñ")

    def GButton_R_command(self):
        self.Select_Option(self.GButton_R, "R" )


    # Definiciones 

    def Select_Option(self, button, letra):

        if button:
            button.config(state=tk.DISABLED)

        controlWord = ''
        showLabel = ''
        letters = list(self.secretWord)
        self.letras.append(letra)

        # Validar Opcion
        if letra not in letters and len(self.letras) > 1:
            self.vidas["fallada"] = self.vidas["fallada"] + 1
            totalVidas = self.vidas['total'] + ( self.vidas["fallada"] * -1 )
            self.GLabel_Vidas.config( text=totalVidas )
            self.Img = tk.PhotoImage(file= str(totalVidas) + ".jpg")
            self.labelImg = tk.Label(root, image=self.Img)
            self.labelImg.place(x=300,y=180)
        else:
            # Mostrar resultado
            for letter in letters:
                if letter in self.letras:
                    showLabel = showLabel + '  ' + letter
                    controlWord = controlWord + letter
                else:
                    showLabel = showLabel + " _ "
            self.GLabel_Palabra.config(text=showLabel)

        if self.vidas["fallada"] == self.vidas["total"]:
            messagebox.showinfo(title=None, message="Juego Terminado: ¡Perdiste!")
            self.stopGame()
            return

        if "".join(letters) == controlWord:
            messagebox.showinfo(title=None, message="Juego Terminado: ¡Ganaste!")
            self.stopGame()
            return

    def stopGame(self):
        self.TNewWord.config(state=tk.NORMAL)
        self.GButton_Add.config(state=tk.NORMAL)
        self.GButton_DelAll.config(state=tk.NORMAL)
        self.GButton_startGame.config(state=tk.NORMAL)
        self.resetGame(tk.DISABLED)
        self.GLabel_Palabra.config(text="")


    def startGame(self):
        rango = len(self.listado_palabras)
        if rango == 0:
            messagebox.showinfo(title=None, message="Debes agregar las palabras secretas para Jugar.")
        else:
            self.TNewWord.config(state=tk.DISABLED)
            self.GButton_Add.config(state=tk.DISABLED)
            self.GButton_DelAll.config(state=tk.DISABLED)
            self.GButton_startGame.config(state=tk.DISABLED)
            self.resetGame(tk.NORMAL)

    def resetGame(self, stateOption):

        # Iniciar Juego
        self.vidas = {
            "total": 5,
            "fallada": 0,
            "imgNormal": "",
            "imgFallada": ""
        }

        self.GLabel_Vidas.config( text=self.vidas['total'] )
        self.Img = tk.PhotoImage(file= str(self.vidas['total']) + ".jpg")
        self.labelImg = tk.Label(root, image=self.Img)
        self.labelImg.place(x=300,y=180)


        rango = len(self.listado_palabras)
        if rango == 0:
            messagebox.showinfo(title=None, message="Debes agregar las palabras secretas para Jugar.")
        else:
            indexPalabra = random.randint(0,rango-1)
            self.secretWord = self.listado_palabras[indexPalabra]
            self.letras = []
            self.Select_Option(False," ")

        # Reset Alfabeto
        self.GButton_A.config(state=stateOption)
        self.GButton_B.config(state=stateOption)
        self.GButton_C.config(state=stateOption)
        self.GButton_D.config(state=stateOption)
        self.GButton_E.config(state=stateOption)
        self.GButton_F.config(state=stateOption)
        self.GButton_G.config(state=stateOption)
        self.GButton_H.config(state=stateOption)
        self.GButton_I.config(state=stateOption)
        self.GButton_J.config(state=stateOption)
        self.GButton_M.config(state=stateOption)
        self.GButton_P.config(state=stateOption)
        self.GButton_S.config(state=stateOption)
        self.GButton_V.config(state=stateOption)
        self.GButton_Y.config(state=stateOption)
        self.GButton_K.config(state=stateOption)
        self.GButton_N.config(state=stateOption)
        self.GButton_Q.config(state=stateOption)
        self.GButton_T.config(state=stateOption)
        self.GButton_W.config(state=stateOption)
        self.GButton_Z.config(state=stateOption)
        self.GButton_L.config(state=stateOption)
        self.GButton_O.config(state=stateOption)
        self.GButton_U.config(state=stateOption)
        self.GButton_X.config(state=stateOption)
        self.GButton_ENIE.config(state=stateOption)
        self.GButton_R.config(state=stateOption)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='#ffffff')
    app = App(root)
    app.stopGame()
    root.mainloop()

