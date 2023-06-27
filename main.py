#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

primaryBack = "#5F9F9F"


class Gauche(Frame):
    def __init__(self, master, bg):
        super().__init__(master=master, bg=bg)

        Label(self, text="Résolution ax² + bx + c = 0", fg="white",
              font=("Helvetica", 16), bg=primaryBack).grid(row=0, column=0, sticky="we", columnspan=2)

        Label(self, text="Saisir les nombres",
              font=("Helvetica", 14), fg="white", bg=primaryBack).grid(row=1, column=0, sticky="we", columnspan=2)

        Label(self, text="Chiffre après la virgule:", fg="white", bg=primaryBack).grid(
            row=2, column=0, sticky="we")

        self.chiffre = StringVar()
        self.wchiffre = Entry(self, textvariable=self.chiffre)
        self.wchiffre.insert(0, "2")
        self.wchiffre.grid(row=2, column=1, sticky="we")

        Label(self, text="Valeur de a:", fg="white", bg=primaryBack).grid(
            row=3, column=0, sticky="we")

        self.A = StringVar()
        self.wvaleura = Entry(self, textvariable=self.A)
        self.wvaleura.focus_set()
        self.wvaleura.grid(row=3, column=1, sticky="we")

        Label(self, text="Valeur de b:", fg="white", bg=primaryBack).grid(
            row=4, column=0, sticky="we")

        self.B = StringVar()
        self.wvaleurb = Entry(self, textvariable=self.B)
        self.wvaleurb.grid(row=4, column=1, sticky="we")

        Label(self, text="Valeur de c:", fg="white", bg=primaryBack).grid(
            row=5, column=0, sticky="we")

        self.C = StringVar()
        self.wvaleurc = Entry(self, textvariable=self.C)
        self.wvaleurc.grid(row=5, column=1, sticky="we")

        Label(self, text="Intervalle de courbe I1:", fg="white", bg=primaryBack).grid(
            row=6, column=0, sticky="we")

        self.I1 = StringVar()
        self.wvaleuri1 = Entry(self, textvariable=self.I1)
        self.wvaleuri1.insert(0, "-11")
        self.wvaleuri1.grid(row=6, column=1, sticky="we")

        Label(self, text="Intervalle de courbe I2:", fg="white", bg=primaryBack).grid(
            row=7, column=0, sticky="we")

        self.I2 = StringVar()
        self.wvaleuri2 = Entry(self, textvariable=self.I2)
        self.wvaleuri2.insert(0, "10")
        self.wvaleuri2.grid(row=7, column=1, sticky="we")

        Button(self, text="Calculer", width=20,
               height=1, font=("Helvetica", 14), bg=primaryBack, fg="white", command=self.calcul).grid(row=8, column=0, columnspan=2)
        Button(self, text="Nouveau", width=20,
               height=1, font=("Helvetica", 14), bg=primaryBack, fg="white", command=self.vider_champ).grid(row=9, column=0, columnspan=2)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def to_int(self, value, error):
        try:
            return int(value)
        except:
            messagebox.showerror("Erreur", error)
            return "no"

    def calcul(self):
        a = self.A.get().strip()
        b = self.B.get().strip()
        c = self.C.get().strip()
        precision = self.chiffre.get().strip()
        I1 = self.I1.get().strip()
        I2 = self.I2.get().strip()

        if a == "" or b == "" or c == "" or precision == "" or I1 == "" or I2 == "":
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
            return self.screen(""), self.plot(clear=True)

        I1 = self.to_int(I1, "I1 n'est pas une valeur entière")
        I2 = self.to_int(I2, "I2 n'est pas une valeur entière")
        c = self.to_int(c, "c n'est pas une valeur entière")
        b = self.to_int(b, "b n'est pas une valeur entière")
        a = self.to_int(a, "a n'est pas une valeur entière")
        precision = self.to_int(
            precision, "Le nombre de chiffre après la virgule n'est pas une valeur entière")

        if a == "no" or b == "no" or c == "no" or precision == "no" or I1 == "no" or I2 == "no":
            return self.screen(""), self.plot(clear=True)

        if I1 >= I2:
            messagebox.showerror(
                "Erreur", "Veuillez ajuster les valeurs de l'intervalle")

        self.screen(self.equation_second_degre(a, b, c, precision))
        self.plot(a, b, c, I1, I2)

    def get_func_towrite(self, func):
        self.screen = func

    def get_func_plot(self, func):
        self.plot = func

    def equation_second_degre(self, a, b, c, precision):
        if a == 0:
            return "L'équation n'est pas du second degré"

        delta = b**2 - 4*a*c

        if delta == 0:
            x = -b / (2*a)
            return f"L'équation admet une unique solution réelle : \nx = {x:.{precision}f}"

        if delta < 0:
            # Calculer les solutions complexes
            alpha = -b / (2*a)
            beta = math.sqrt(-delta) / (2*a)

            alpha = round(alpha, precision)
            beta = round(beta, precision)

            sol_1 = complex(alpha, beta)
            sol_2 = complex(alpha, -beta)

            return f"L'équation n'admet pas de solutions réelles\nLes solutions complexes de l'équation sont: \nx1 = {sol_1}\nx2 = {sol_2}"

        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Les solutions de l'équation sont:\nx1 = {x1:.{precision}f}\nx2 = {x2:.{precision}f}"

    def vider_champ(self):
        self.wvaleura.delete(0, END)
        self.wvaleura.insert(0, "")
        self.wvaleurb.delete(0, END)
        self.wvaleurb.insert(0, "")
        self.wvaleurc.delete(0, END)
        self.wvaleurc.insert(0, "")

        if not self.chiffre.get().strip():
            self.wchiffre.delete(0, END)
            self.wchiffre.insert(0, "2")
        if not self.I1.get().strip():
            self.wvaleuri1.delete(0, END)
            self.wvaleuri1.insert(0, "-11")
        if not self.I2.get().strip():
            self.wvaleuri2.delete(0, END)
            self.wvaleuri2.insert(0, "10")


class Droite(Frame):
    def __init__(self, master, bg):
        super().__init__(master=master, bg=bg)

        self.terminal = Text(self, width=62, height=15, state='disabled')
        self.terminal.grid(row=0, column=0)

        self.fig = Figure(figsize=(5, 3))
        self.plot = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=1, column=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def write_to_screen(self, texte):
        self.terminal.configure(state='normal')
        self.terminal.delete("1.0", END)
        self.terminal.insert(END, texte)
        self.terminal.configure(state='disabled')

    def write_to_plot(self, a=None, b=None, c=None, I1=None, I2=None, clear=False):
        self.plot.clear()

        if not clear:
            x = range(I1, I2)
            y = [a * (xi ** 2) + b * xi + c for xi in x]

            self.plot.plot(x, y)

        self.canvas.draw()


class MyApp(Tk):
    def __init__(self):
        super().__init__()

        self.title("Calcul second degré")
        # self.resizable(False, False)
        # self.geometry("600x600")
        self.minsize(1000, 600)

        fGauche = Gauche(self, bg=primaryBack)
        fDroite = Droite(self, bg=primaryBack)

        fGauche.get_func_towrite(fDroite.write_to_screen)
        fGauche.get_func_plot(fDroite.write_to_plot)
        fGauche.grid(row=0, column=0, sticky="nswe")
        fDroite.grid(row=0, column=1, sticky="nswe")

        # Configurer la gestion de la mise en page Grid pour que les frames s'étendent
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.mainloop()


app = MyApp()
