from tkinter import*

import time

ws = Tk()
ws.iconbitmap("Hacker.ico")
ws.title("Relógio Digital")

ws.resizable(0,0)




lb1 = Label(ws, font = ("Boulder", 68, "bold"), bg = "silver", fg = "#363529", bd =25)

lb1.grid(row = 0, column =1)


def relogio():

    agora = time.strftime("%H:%M:%S") #obtendo a hora em tempio real e definindo o formato da hora
    lb1.configure(text = agora) #definindo o texto da label que seria as horas
    lb1.after(200, relogio) #chamando a função dentro dela mesma e dizendo para atualizar a cada 200 milésimos 

relogio()

ws.geometry("400x150")

ws.mainloop()
