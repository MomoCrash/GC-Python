from tkinter import *
class Window:
  '''Init Window class
  (root,width,height,windowTitle)'''
  
  def __init__(self,root,width:int,height:int,windowTitle:str):
    root.title(windowTitle)
    root.geometry(str(width)+'x'+str(height))
    self.window=Frame(root)
    
  def jouer(self,type_quiz):
    self.window.grid_remove()
    Jeu(root).ouvrir()
    
  def rejouer(self):
    global count
    global score
    count = 0
    score = 0
    recommencer()
    self.window.grid_remove()
    Choix(root).ouvrir()
    
  def ouvrir(self):
    self.window.grid(column=0,row=0,sticky='news')

class Menu(Window):
  
  def __init__(self,root):
    super().__init__(root,600,300,'Projet')
    # fenetre d'accueil
    title=Text(self.window, padx=20, pady=100)
    title.insert(INSERT,"WORDLE")
    title.tag_add('title','1.0', '1.17')
    title.tag_configure('title',font=('Times New Roman',22,'bold'), justify='center')
    title['state']='disabled'
    bout1=Button(self.window, text="Start", command=self.jouer)
    bout2=Button(self.window, text="Quitter", command=root.destroy)

    title.grid(column=0,row=0,columnspan=2,sticky='news')
    bout1.grid(column=0,row=1,sticky='nsew')
    bout2.grid(column=1,row=1,sticky='snew')
    
    self.window.columnconfigure(0,weight=1)
    self.window.columnconfigure(1,weight=1)
    self.window.rowconfigure(0,weight=1)

class Jeu(Window):
  
  def __init__(self,root):
    super().__init__(root,600,300,'Projet')
    # fenetre d'accueil
    title=Text(self.window, padx=20)
    title.insert(INSERT,"WORDLE")
    title.tag_add('title','1.0', '1.17')
    title.tag_configure('title',font=('Times New Roman',22,'bold'), justify='center')
    title['state']='disabled'
    bout1=Button(self.window, text="Start", command=self.choisir)
    bout2=Button(self.window, text="Quitter", command=root.destroy)

    title.grid(column=0,row=0,columnspan=2,sticky='news')
    bout1.grid(column=0,row=1,sticky='nsew')
    bout2.grid(column=1,row=1,sticky='snew')
    
    self.window.columnconfigure(0,weight=1)
    self.window.columnconfigure(1,weight=1)
    self.window.rowconfigure(0,weight=1)


root=Tk()
menu=Menu(root)
menu.ouvrir()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()