import pyautogui
import time
from tkinter import *
from tkinter.ttk import Frame, Label, Entry, Combobox, Button


class Application:
  global tempo
  def condPara(self):
    tempo = self.entry.get()
    tempo = int(self.tempo)
    cord = pyautogui.position()
    while (pyautogui.position() == cord):
      pyautogui.hotkey('alt','tab')
      time.sleep(tempo)

  def __init__(self, master=None):
    
    self.widget = Frame(master)
    self.widget.pack()
    self.imagem = PhotoImage(file="icon/promarking.png")
    self.lbImg = Label(self.widget, image=self.imagem)
    self.lbImg.imagem = self.imagem
    self.lbImg.pack(fill='x')
        
    self.widget1 = Frame(master)
    self.widget1.pack()
    self.lb1 = Label(self.widget1,text="Tempo de troca tela",font="-weight bold -size 10")
    self.lb1.pack(side='left')
    self.entry = Entry(self.widget1)
    self.entry.pack (side='right')
    
    
    
    self.widget2 = Frame(master)
    self.widget2.pack()
    self.btn1 = Button(self.widget2,text="Salvar",command=self.condPara)
    self.btn1.pack(side='right')

  
root = Tk()
root.title("Guia de produção Promarking")
Application(root)
root.mainloop()