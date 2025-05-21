#GLOBALE VARIABELEN
from tkinter import *
venster = Tk()
# venster.geometry("800x800")
# venster.attributes('-fullscreen', True)
venster.wm_title("Zeeslagje")
venster.config(bg="lightblue")
bord = []
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
    print(knop)
    
def maak_leeg_bord(): #Niet nodig?
    for aantal in range(10):
        rij = ['~'] * 10
        bord.append(rij)
        print(rij, end="")
        print()
    return bord

def boten_plaatsten(rij,kolom):
    bord[rij][kolom] = "x"
    print()
    print()
    for rij in range(10):
        print(bord[rij])
    return bord

def boot_plaats_checken():
    for rij_index in range(len(bord)):
        for kolom_index in range(len(bord[rij_index])):
            if bord[rij_index][kolom_index] == "x":
                print("Gevonden op rij", rij_index, "kolom", kolom_index)
#HOOFDPROGRAMMA
maak_leeg_bord()
maak_gui_bord()
boten_plaatsten(6,9)
boot_plaats_checken()

venster.mainloop()