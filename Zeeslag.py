#GLOBALE VARIABELEN
from tkinter import *
venster = Tk()
# venster.geometry("800x800")
# venster.attributes('-fullscreen', True)
venster.wm_title("Zeeslagje")
venster.config(bg="lightblue")

#FUNCTIEDEFINITIES

#Gemaakt door:Sjoerd
def maak_gui_bord():
    #Eerst een leeg hokje
    lege_label = Label(venster, width=4, height=2, bg="lightblue")
    lege_label.grid(row=0, column=0)
    #Dit deel geeft de kolommen elk een letter:
    kolom_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] 
    for kolom in range(10):
        label = Label(venster,text=kolom_letters[kolom],width=4, height=2, bg="lightblue",font=("Helvetica",14,"bold"))
        label.grid(row=0, column=kolom+1)
    #Dit stukje geeft de rijen weer:
    for rij in range(1,11):
        rij_label = Label(venster,text=str(rij),width=4,height=2,bg="lightblue",font=("Helvetica",14,"bold"))
        rij_label.grid(row=rij, column=0)
    # Maakt een 10x10 raster van knoppen
    for rij in range(10):
        for kolom in range(10):
            coordinaat = f"{kolom_letters[kolom]}{rij + 1}"
            knop = Button(venster, text="~", width=7, height=3,bg="#87CEEB",relief="raised",borderwidth=1)
            knop.config(command=lambda vakje=coordinaat, k=knop: knop_geklikt(vakje, k)) #Dit stukje hebben we gemaakt met hulp van chatGPT, het geeft de knop en de coordinaten van de knop terug wanneer er op geklikt word. Omdat er verwezen wordt naar de knop zelf, staat de command bij .config ipv bij de button zelf.
            knop.grid(row=rij+1, column=kolom+1 ,padx=1,pady=1)

def knop_geklikt(coordinaat,knop):
    print("je klikte op:", coordinaat)
    knop.config(bg="red",state="disabled") #De kleur veranderd, en nu kan de knop ook niet nog een keer ingedrukt worden.
    
def maak_leeg_bord(grootte): #Niet nodig?
    bord = []
    print("  "," 1 ","  2  ","  3  ","  4  ","  5  ",)
    for aantal in range(grootte):
        rij = ['~'] * grootte
        bord.append(rij)
        print(aantal+1,rij, end="")
        # print(aantal, end="")
        print()
    return bord

#HOOFDPROGRAMMA
# maak_leeg_bord(5)
maak_gui_bord()

venster.mainloop()