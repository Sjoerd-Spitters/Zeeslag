###GLOBALE VARIABELEN
from tkinter import *
import random
venster = Tk()
venster.geometry("900x900")
venster.wm_title("Zeeslagje")
venster.config(bg="lightblue")
bord = []

geselecteerde_boot = "Good Personality"
geselecteerde_richting = "horizontaal"  # of "verticaal"
 
boten_info = {
    "Wang Jangler": {"lengte": 6, "aantal": 1},
    "Sloop Doggy Dog": {"lengte": 4, "aantal": 2},
    "torpedo jager": {"lengte": 3, "aantal": 3},
    "Good Personality": {"lengte": 2, "aantal": 2}
}

boten_lijst = [] #hierin komen dictionaries met informatie over waar een boot ligt en of hij is geraakt
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
            coordinaat = kolom_letters[kolom] + str(rij + 1)
            knop = Button(venster, text="~", width=7, height=3,bg="#87CEEB",relief="raised",borderwidth=1)
            knop.config(command=lambda vakje=coordinaat, k=knop: knop_geklikt(vakje, k)) #Dit stukje hebben we gemaakt met hulp van chatGPT, het geeft de knop en de coordinaten van de knop terug wanneer er op geklikt word. Omdat er verwezen wordt naar de knop zelf, staat de command bij .config ipv bij de button zelf.
            knop.grid(row=rij+1, column=kolom+1 ,padx=1,pady=1)

#Gemaakt door:Iedereen
def knop_geklikt(coordinaat,knop):
    # print("je klikte op:", coordinaat) ########
    
    # knop.config(bg="red",state="disabled") #De kleur veranderd, en nu kan de knop ook niet nog een keer ingedrukt worden.
    vakNummer = str(coordinaat)
    #Dit stukje zet de coordinaat om naar een rij en kolomwaarde, om het te kunnen gebruiken in de 2D versie van het spel
    kolomLetter=vakNummer[0]
    rijWaardeVakje=vakNummer[1:]
    kolomWaardeVakje= ord(kolomLetter) - ord("A") +1 #De omzetting van letter naar cijfer gedaan met behulp van ChatGPT
    schot_checken(int(rijWaardeVakje)-1,int(kolomWaardeVakje)-1,knop) 
    ##########################################

def schot_checken(rij,kolom,knop):

    # print("rij:",rij,"kolom:",kolom) ########
    if bord[rij][kolom] == "x":
        print("Raak!")
        knop.config(bg="red",state="disabled")
        #gemaakt door: Rens
        geraakt_vakje = (kolom, rij) #dit maakt de code makkelijker te lezen
        for boot in boten_lijst: #boot is een index in de lijst en dus een dictionary
            if geraakt_vakje in boot["coordinaten"] and geraakt_vakje not in boot["geraakt"]: 
                boot["geraakt"].append(geraakt_vakje)
                print(boot['naam'],  "is geraakt!")

                if len(boot["geraakt"]) == boot["lengte"]: #als boot[geraakt] net zo veel veel geraakte vakjes bevat als de lengte van de boot is deze gezonken
                    print(boot['naam'],  "is gezonken!")
                    boot["gezonken"] = True #de boot wordt als gezonken opgeslagen
          
    else:
        print("Mis!")
        knop.config(bg="white",state ="disabled")

    alle_boten_gezonken = all(boot["gezonken"] for boot in boten_lijst)
    if alle_boten_gezonken:
        print("Alle boten zijn gezonken! Je hebt gewonnen!")
        spel_eindigen()
        

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
    
    for i in range(lengte): #dit gedeelte plaatst de boot 
      if richting == "horizontaal":
        ver = rij
        hor = kolom + i
    else: #richting is verticaal
        ver = rij + i
        hor = kolom
    bord[ver][hor] = "x"
    
    boten_info[geselecteerde_boot]["aantal"] -= 1 # laat de speler zien hoeveel boten er nog van deze soort boot geplaatst kunnen worden
    print(geselecteerde_boot , 'is geplaatst. je hebt nog:', boten_info[geselecteerde_boot]['aantal'] , "van deze boten over." )
    
    for rij in bord:
        print(rij)

#Gemaakt door:Sjoerd en Rens
def boot_plaats_checken(rij,kolom, lengte, richting):
    for i in range(lengte):
    # Bepaal de juiste rij en kolom op basis van richting
        if richting == "horizontaal":
            ver = rij
            hor = kolom + i

        else: #richting is verticaal
            ver = rij + i
            hor = kolom

        if not (0 <= ver < 10 and 0 <= hor < 10): #controle of de boot past op het raster
            return False

        for rij_index in range(-1, 2): #Dit loopt door alle vakjes om het vakje wat nu wordt behandeld en als er al wat omheen zit, word er niets geplaatst
            for kolom_index in range(-1,2): 
                buur_rij = ver + rij_index 
                buur_kolom = hor + kolom_index
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
                    coordinaten = []
                    for i in range(lengte): #dit gedeelte plaatst de boten daadwerkelijk
                        if richting == "horizontaal":
                            ver = rij
                            hor = kolom + i
                        else: #richting is verticaal
                            ver = rij + i
                            hor = kolom
                        bord[ver][hor] = "x"
                        coordinaten.append((hor, ver)) #coordinaten worden als tuple opgeslagen en niet apart
                        print(coordinaten)
                    
                    boten_lijst.append({"naam": naam,
                        "lengte": lengte,
                        "coordinaten": coordinaten,
                        "geraakt": [],
                        "gezonken": False})
                    print(boten_lijst)
                    geplaatst = True
    for rij in bord:
        print(rij)

def spel_eindigen():
    eind_melding = Label(venster, text=" Alle boten zijn gezonken! Spel afgelopen.", 
                         bg="lightblue", fg="darkred", font=("Helvetica", 16, "bold"))
    eind_melding.grid(row=11, column=0, columnspan=11, pady=20)

###HOOFDPROGRAMMA
maak_leeg_bord()
plaats_alle_boten_automatisch()
maak_gui_bord()
# boten_plaatsten(3, 1) 
# boten_plaatsten(4,1) kan niet want dan zou de boot naast een ander komen te liggen.
# boten_plaatsten(6,6)
# boten_plaatsten(9,9) kan niet want dan zou de boot buiten veld komen.

venster.mainloop()