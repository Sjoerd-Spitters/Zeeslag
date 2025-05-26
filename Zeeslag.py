###GLOBALE VARIABELEN
from tkinter import *
import random
venster = Tk()
venster.geometry("900x900")
venster.wm_title("Zeeslagje")
venster.config(bg="lightblue")
bord = []

geselecteerde_boot = "patrouilleschip"

geselecteerde_richting = "horizontaal"  # of "verticaal"
 
boten_info = {
    "vliegdekschip": {"lengte": 6, "aantal": 1},
    "slagschip": {"lengte": 4, "aantal": 2},
    "onderzeeër": {"lengte": 3, "aantal": 1},
    "patrouilleschip": {"lengte": 2, "aantal": 4}
}

###FUNCTIEDEFINITIES

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
    for _ in range(10): # teller wordt niet gebruikt in de loop dus een naam is onnodig
        rij = ['~'] * 10
        bord.append(rij)
        print(rij, end="")
        print()
    print() # lege regel printen zodat borden niet aan elkaar worden geplakt.
    return bord


#gemaakt door: Sjoerd en Rens
def boten_plaatsten(rij, kolom): #zet de boten neer 
    lengte = boten_info[geselecteerde_boot]["lengte"]
    print( "de lengte is:", lengte ,type(lengte))
    richting = geselecteerde_richting
    print("de richting is:", richting)
    
    if not boot_plaats_checken(rij, kolom, lengte, richting): #checkt of de boot geplaatst mag worden, zo niet stopt de functie direct
        print("Je kunt hier geen boot plaatsen.")
        return
    
    for increment in range(lengte): #dit gedeelte plaatst de boot 
      if richting == "verticaal":
          r = rij + increment
          c = kolom
      else:  # horizontaal
          r = rij
          c = kolom + increment
      bord[r][c] = "x" #een boot plekje is een "x"
    
    boten_info[geselecteerde_boot]["aantal"] -= 1 # laat de speler zien hoeveel boten er nog van deze soort boot geplaatst kunnen worden
    print(geselecteerde_boot , 'is geplaatst. je hebt nog:', boten_info[geselecteerde_boot]['aantal'] , "van deze boten over." )
    
    for rij in bord:
        print(rij)

#Gemaakt door:Sjoerd en Rens
def boot_plaats_checken(rij,kolom, lengte, richting):
    for increment in range(lengte):
    # Bepaal de juiste rij en kolom op basis van richting
        if richting == "verticaal":
            r = rij + increment
            c = kolom
        else:  # de richting is dus horizontaal
            r = rij
            c = kolom + increment

        if not (0 <= r < 10 and 0 <= c < 10): #controle of de boot past op het raster
            return False

        for rij_index in range(-1, 2): #Dit loopt door alle vakjes om het vakje wat nu wordt behandeld en als er al wat omheen zit, word er niets geplaatst
            for kolom_index in range(-1,2): 
                buur_rij = r + rij_index 
                buur_kolom = c + kolom_index
                if 0 <= buur_rij < 10 and 0 <= buur_kolom < 10:  # checkt of de checker binnen grenzen aan het kijken is, dit voorkomt foutcodes
                    if bord[buur_rij][buur_kolom] == "x":
                        return False
    return True

def plaats_alle_boten_automatisch():
    for naam in boten_info: 
        lengte = boten_info[naam]["lengte"]
        aantal = boten_info[naam]["aantal"]

        for _ in range(aantal): #telller wordt niet gebruikt
            geplaatst = False 
            while not geplaatst: #de while loop zorgt ervoor dat het plaatsen pas stopt wanneer de boot succesvol is geplaatst
                rij = random.randint(0, 9) # willekeurige rij van 0 tot 10
                kolom = random.randint(0, 9) # willekeurige kolom van 0 tot 10
                richting = random.choice(["horizontaal", "verticaal"]) 

                if boot_plaats_checken(rij, kolom, lengte, richting): #boot moet voldoen aan plaatsingseisen
                    for i in range(lengte): 
                        if richting == "horizontaal":
                            bord[rij][kolom + i] = "x"
                        else:
                            bord[rij + i][kolom] = "x"
                    geplaatst = True
    for rij in bord:
        print(rij)


###HOOFDPROGRAMMA
maak_leeg_bord()
plaats_alle_boten_automatisch()
maak_gui_bord()
# boten_plaatsten(3, 1)
# boten_plaatsten(4,1) kan niet want dan zou de boot naast een ander komen te liggen.
# boten_plaatsten(6,6)
# boten_plaatsten(9,9) kan niet want dan zou de boot buiten veld komen.

venster.mainloop()