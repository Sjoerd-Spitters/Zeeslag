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
    # Maakt een 10x10 raster van knoppen en geeft informatie bij het klikken van een knopje
    for rij in range(10):
        for kolom in range(10):
            coordinaat = f"{kolom_letters[kolom]}{rij + 1}"
            knop = Button(venster, text="~", width=7, height=3,bg="#87CEEB",relief="raised",borderwidth=1)
            knop.config(command=lambda vakje=coordinaat, k=knop: knop_geklikt(vakje, k)) #Dit stukje hebben we gemaakt met hulp van chatGPT, het geeft de knop en de coordinaten van de knop terug wanneer er op geklikt word. Omdat er verwezen wordt naar de knop zelf, staat de command bij .config ipv bij de button zelf.
            knop.grid(row=rij+1, column=kolom+1 ,padx=1,pady=1)

#Gemaakt door:Iedereen
def knop_geklikt(coordinaat,knop):
    print("je klikte op:", coordinaat)
    knop.config(bg="red",state="disabled") #De kleur veranderd, en nu kan de knop ook niet nog een keer ingedrukt worden.
    vakNummer = str(coordinaat)
    #Dit stukje zet de coordinaat om naar een rij en kolomwaarde, om het te kunnen gebruiken in de 2D versie van het spel
    kolomLetter=vakNummer[0]
    rijWaardeVakje=vakNummer[1:]
    kolomWaardeVakje= ord(kolomLetter) - ord("A") +1 #De omzetting van letter naar cijfer gedaan met behulp van ChatGPT
    boten_plaatsten(int(rijWaardeVakje)-1,int(kolomWaardeVakje)-1) #Dit zet een kruisje 'x' op de plek waar geklikt is.
    

#Gemaakt door:Sjoerd
def maak_leeg_bord(): #Maakt het bord aan voor de '2D' versie van het spel
    for aantal in range(10):
        rij = ['~'] * 10
        bord.append(rij)
        print(rij, end="")
        print()
    return bord

#Gemaakt door:Sjoerd
def boten_plaatsten(rij,kolom): #Zet de boten neer 
    if boot_plaats_checken(rij,kolom):
        bord[rij][kolom] = "x"
    else:
        print("Je mag hier geen kruisje plaatsen")
    for rij in range(10):
        print(bord[rij])
    return bord

#Gemaakt door:Sjoerd
def boot_plaats_checken(rij,kolom):
    for rij_index in range(rij - 1, rij + 2): #Dit loopt door alle vakjes om het geklikte vakje en als er al wat zit, word er niets geplaatst
        for kolom_index in range(kolom - 1, kolom + 2):
            if bord[rij_index][kolom_index] == "x":
                return False
    return True

#HOOFDPROGRAMMA
maak_leeg_bord()
maak_gui_bord()


venster.mainloop()