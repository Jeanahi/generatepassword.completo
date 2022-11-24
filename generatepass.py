from tkinter import *
import random 
import string

def generatePass():
    lst=[]
    for i in range(1,13):
        alphabet_lowers=list(string.ascii_lowercase)
        alphabet_upper=list(string.ascii_uppercase)
        alphabet_symbol=list(string.punctuation)
        str=alphabet_lowers+alphabet_upper+alphabet_symbol
        character=random.choice(str)
        lst.append(character)
    a="".join(lst)
    print(a)
    label.config(text=a)  


root = Tk()

root.title("Generador de Password")

root.geometry("500x500")

root.resizable(0,0)


my_button=Button(root, text="Generar",font="arial 15 bold ",command=generatePass).pack() 
my_label=Label(root,text="").pack()
exit_button=Button(root, text="Salir", font="arial 15 bold",command=root.destroy).pack()
my_label=Label(root,text="").pack()
label_et=Label(root,text="Esta es la contraseña : ")
label_et.pack()
label=Label(root,text="",font="arial 15 bold ")
label.pack()

root.mainloop()