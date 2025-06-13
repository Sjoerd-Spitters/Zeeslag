###GLOBALE VARIABELEN
#Sjoerd Spitters, Rens Spitters, Thomas van de wetering
from tkinter import *
import random
from PIL import Image, ImageTk
aantal_schoten_speler1 = 0
aantal_schoten_speler2 = 0
label_schoten_speler1 = None
label_schoten_speler2 = None

spelmodus = None
vensterWelkom = Tk()
breedte = vensterWelkom.winfo_screenwidth()
hoogte = vensterWelkom.winfo_screenheight()
vensterWelkom.wm_title("Welkom")
vensterWelkom.config(bg="lightblue")
vensterWelkom.geometry(str(breedte) + "x" + str(hoogte))
bord_speler1 = []
bord_speler2 = []
geselecteerde_boot = "Good Personality"
geselecteerde_richting = "horizontaal"  # of "verticaal"
 
boten_info = {
    "Wang Jangler": {"lengte": 6, "aantal": 1},
    "Sloop Doggy Dog": {"lengte": 4, "aantal": 1},
    "Torpedo Jager": {"lengte": 3, "aantal": 2},
    "Good Personality": {"lengte": 2, "aantal":1 }
}

boten_lijst_1 = [] #hierin komen dictionaries met informatie over waar een boot ligt en of hij is geraakt
boten_lijst_2 = []
###FUNCTIEDEFINITIES

#Gemaakt door Thomas
def welkomstscherm():
    achtergrond_afbeelding = Image.open("zeeslag/achtergrond.jpg")  #Maakt de afbeelding open
    achtergrond_afbeelding = achtergrond_afbeelding.resize((breedte, hoogte), Image.Resampling.LANCZOS)  #zorgt ervoor dat het in elk scherm past
    bg = ImageTk.PhotoImage(achtergrond_afbeelding)
    achtergrond_label = Label(vensterWelkom, image=bg)
    achtergrond_label.image = bg
    achtergrond_label.place(x=0, y=0, relwidth=1, relheight=1)

    # knop_plaatje = Image.open("startknop.png") 
    # knop_plaatje = knop_plaatje.resize((300, 250), Image.Resampling.LANCZOS)
    # startknop_img = ImageTk.PhotoImage(knop_plaatje)


    # beginKnop = Button(vensterWelkom, image=startknop_img, command=begin_spel, borderwidth=10, highlightthickness=0, bg="grey", activebackground="grey")
    # beginKnop.image = startknop_img
    # beginKnop.place(relx=0.5, rely=0.4,  anchor="center")

    #singleplayer knop
    global sp_knop_img, mp_knop_img
    sp_knop_img = ImageTk.PhotoImage(Image.open("zeeslag/startknop.png").resize((300, 250)))
    Button(vensterWelkom, image=sp_knop_img, command=lambda: begin_spel("single"), borderwidth=5, bg="grey").place(relx=0.3, rely=0.4, anchor=CENTER)
    #label met singleplyer er op
    Button(vensterWelkom, image=sp_knop_img, command=lambda: begin_spel("single"), borderwidth=5, bg="grey").place(relx=0.3, rely=0.4, anchor=CENTER)
    Label(vensterWelkom, text="Singleplayer", font=("Helvetica", 16, "bold"), bg="lightgrey").place(relx=0.3, rely=0.65, anchor=CENTER)

    # Multiplayer knop
    mp_knop_img = ImageTk.PhotoImage(Image.open("zeeslag/startknop.png").resize((300, 250)))
    Button(vensterWelkom, image=mp_knop_img, command=lambda: begin_spel("multi"), borderwidth=5, bg="grey").place(relx=0.7, rely=0.4, anchor=CENTER)
    
    # label met multiplayer er op
    Button(vensterWelkom, image=mp_knop_img, command=lambda: begin_spel("multi"), borderwidth=5, bg="grey").place(relx=0.7, rely=0.4, anchor=CENTER)
    Label(vensterWelkom, text="Multiplayer", font=("Helvetica", 16, "bold"), bg="lightgrey").place(relx=0.7, rely=0.65, anchor=CENTER)
        
    logo_img = Image.open("zeeslag/zeeslaglogo.png")  # vervang dit met jouw bestandsnaam
    logo_img = logo_img.resize((600, 150))  # pas grootte aan naar wens
    logo_foto = ImageTk.PhotoImage(logo_img)

    # Bewaar referentie aan afbeelding zodat deze zichtbaar blijft
    vensterWelkom.titel_afbeelding = logo_foto

    # Voeg afbeelding toe aan het venster
    Label(vensterWelkom, image=logo_foto, bg="lightblue").place(relx=0.5, rely=0.1, anchor=CENTER)

#Gemaakt door iedereen
def begin_spel(modus):

    global spelmodus
    spelmodus = modus

    vensterWelkom.destroy() #welkomstvenster sluit

    global venster
    venster = Tk()
    venster.geometry(str(breedte) + "x" + str(hoogte))
    venster.wm_title("Zeeslagje")
    venster.config(bg="lightblue")

    #achtergrond instellen
    achtergrond_afbeelding = Image.open("zeeslag/achtergrond.jpg")  # Gebruik je eigen afbeeldingsnaam hier
    achtergrond_afbeelding = achtergrond_afbeelding.resize((breedte, hoogte), Image.Resampling.LANCZOS)  # Schaal naar venstergrootte
    bg = ImageTk.PhotoImage(achtergrond_afbeelding)
    achtergrond_label = Label(venster, image=bg)
    achtergrond_label.image = bg  # Houd een referentie vast
    achtergrond_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #maakt lege borden aan
    maak_lege_borden()



    if modus == "single":
        boot_plaats_willekeurig_bepalen(bord_speler1, boten_lijst_1)
        boot_plaats_willekeurig_bepalen(bord_speler2, boten_lijst_2)
    elif modus == "multi":
        boot_plaats_willekeurig_bepalen(bord_speler1, boten_lijst_1)
        boot_plaats_willekeurig_bepalen(bord_speler2, boten_lijst_2)

    maak_gui_bord()
    venster.mainloop()

def start_spel_met_modus(modus):
    global spelmodus
    spelmodus = modus
    vensterWelkom.destroy()
    begin_spel()
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
        #tweede bord
        label2 = Label(venster,text=kolom_letters[kolom],width=4, height=2, bg="lightblue",font=("Helvetica",14,"bold"))
        label2.grid(row=0, column=kolom+13)        
    #Dit stukje geeft de rijen weer:
    for rij in range(1,11):
        rij_label = Label(venster,text=str(rij),width=4,height=2,bg="lightblue",font=("Helvetica",14,"bold"))
        rij_label.grid(row=rij, column=0)
        #ruimte tussen borden
        spacer = Label(venster,width=4,height=2,bg="black")
        spacer.grid(row=rij,column=11)
        rij_label2 = Label(venster,text=str(rij),width=4,height=2,bg="lightblue",font=("Helvetica",14,"bold"))
        rij_label2.grid(row=rij, column=12)
        
        global label_schoten_speler1, label_schoten_speler2

        label_schoten_speler1 = Label(venster, text="Speler 1 schoten: 0", font=("Helvetica", 12), bg="lightblue")
        label_schoten_speler1.place(x=100, y=hoogte - 100)

        label_schoten_speler2 = Label(venster, text="Speler 2 schoten: 0", font=("Helvetica", 12), bg="lightblue")
        label_schoten_speler2.place(x=breedte - 250, y=hoogte - 100)

    # Maakt een 10x10 raster van knoppen en geeft informatie bij het klikken van een knopje
    for rij in range(10):
        for kolom in range(10):
            coordinaat1 = kolom_letters[kolom] + str(rij + 1)
            coordinaat2=  kolom_letters[kolom] + str(rij + 1) #Het tweede speelbord start nota bene ook op dezelfde plaats voor de coordinaten
            knop = Button(venster, text="~", width=7, height=3,bg="#87CEEB",relief="raised",borderwidth=1)
            knop.config(command=lambda vakje=coordinaat1, k=knop: knop_geklikt(vakje, k, "speler_1")) #Dit stukje hebben we gemaakt met hulp van chatGPT, het geeft de knop en de coordinaten van de knop terug wanneer er op geklikt word. Omdat er verwezen wordt naar de knop zelf, staat de command bij .config ipv bij de button zelf.
            knop.grid(row=rij+1, column=kolom+1 ,padx=1,pady=1)
            # voor tweede bord
            knop2 = Button(venster, text="~", width=7, height=3,bg="#87CEEB",relief="raised",borderwidth=1)
            knop2.config(command=lambda vakje=coordinaat2, k=knop2: knop_geklikt(vakje, k, "speler_2"))
            knop2.grid(row=rij+1, column=kolom+13,padx=1,pady=1)
    if spelmodus == "multi":
        for rij in range(10):
            for kolom in range(10):
                # Beide knoppen actief
                knop.config(state=NORMAL)
                knop2.config(state=NORMAL)
    if spelmodus == "single":
        # Bij singleplayer: alleen linker bord interactief
        for rij in range(10):
            for kolom in range(10):
                knop2 = venster.grid_slaves(row=rij+1, column=kolom+13)[0]
                knop2.config(state=DISABLED)  # Rechter bord uitschakelen

#Gemaakt door:Iedereen
def knop_geklikt(coordinaat, knop, speler):
    global aantal_schoten_speler1, aantal_schoten_speler2

    if speler == "speler_1":
        aantal_schoten_speler1 += 1
        label_schoten_speler1.config(text=f"Speler 1 schoten: {aantal_schoten_speler1}")
        bord = bord_speler1
        boten_lijst = boten_lijst_1
    else:
        aantal_schoten_speler2 += 1
        label_schoten_speler2.config(text=f"Speler 2 schoten: {aantal_schoten_speler2}")
        bord = bord_speler2
        boten_lijst = boten_lijst_2

    vakNummer = str(coordinaat)
    kolomLetter = vakNummer[0]
    rijWaardeVakje = vakNummer[1:]
    kolomWaardeVakje = ord(kolomLetter) - ord("A") + 1

    schot_checken(int(rijWaardeVakje) - 1, int(kolomWaardeVakje) - 1, knop, bord, boten_lijst)
    return bord


#Gemaakt door Rens en Sjoerd
def schot_checken(rij,kolom,knop,bord, boten_lijst):
    if bord[rij][kolom] == "x":
        print("Raak!")
        knop.config(bg="red", state="disabled")
        Raakplaatje(knop.winfo_rootx() - venster.winfo_rootx(), knop.winfo_rooty() - venster.winfo_rooty())
        #gemaakt door: Rens
        # Dit stuk past de boot lijst aan, zodat het schot wordt geregistreerd.
        geraakt_vakje = (kolom, rij) #dit maakt de code makkelijker te lezen
        for boot in boten_lijst: #boot is een index in de lijst en dus een dictionary
            if geraakt_vakje in boot["coordinaten"] and geraakt_vakje not in boot["geraakt"]: 
                boot["geraakt"].append(geraakt_vakje)
                print(boot['naam'],  "is geraakt!")
                if len(boot["geraakt"]) == boot["lengte"]: #als boot[geraakt] net zo veel veel geraakte vakjes bevat als de lengte van de boot is deze gezonken
                    print(boot['naam'],  "is gezonken!")
                    gezonkenplaatje(knop.winfo_rootx() - venster.winfo_rootx(), knop.winfo_rooty() - venster.winfo_rooty())
        #gemaakt door: Rens
                    boot["gezonken"] = True #de boot wordt als gezonken opgeslagen
    else: #Niet geraakt, dus er is misgeschoten
        print("Mis!")
        knop.config(bg="white",state ="disabled")#knop wel uitzetten, zodat hij niet nogmaals word ingedrukt
        misplaatje(knop.winfo_rootx() - venster.winfo_rootx(), knop.winfo_rooty() - venster.winfo_rooty())

    alle_boten_gezonken = all(boot["gezonken"] for boot in boten_lijst_1)
    if alle_boten_gezonken:
        print("Alle boten zijn gezonken! Je hebt gewonnen!")
        gewonnenplaatje(knop.winfo_rootx() - venster.winfo_rootx(), knop.winfo_rooty() - venster.winfo_rooty())


    # Alleen bij singleplayer: computer laat automatisch schieten
    if spelmodus == "single" and not alle_boten_gezonken:
        venster.after(1000, computer_schot)

def computer_schot():
    # Eenvoudige AI: willekeurig schieten
    rij = random.randint(0, 9)
    kolom = random.randint(0, 9)
    
    # Zoek een knop in het grid (speler 1 bord)
    for child in venster.winfo_children():
        if isinstance(child, Button) and child.grid_info()["row"] == rij+1 and child.grid_info()["column"] == kolom+1:
            knop_geklikt(f"{chr(65+kolom)}{rij+1}", child, "speler_1")
            break
#Gemaakt door:Sjoerd
def maak_lege_borden(): #Maakt het bord aan voor de '2D' versie van het spel
    for _ in range(10): # teller wordt niet gebruikt in de loop dus een naam is onnodig
        rij = ['~'] * 10
        bord_speler1.append(rij)
        rij_bord2 = ['~'] * 10
        bord_speler2.append(rij_bord2) #Er moet een andere variabele gemaakt worden voor bord 2, omdat ze anders naar hetzelfde refereren. Ik heb dit probleem opgelost met behulp van deepseek.
    return bord_speler1, bord_speler2

#gemaakt door: Sjoerd en Rens
##################DEZE FUNCITE IS NOG NIET IN GEBRUIK####################
def boten_plaatsten(rij, kolom): #zet de boten neer 
    lengte = boten_info[geselecteerde_boot]["lengte"]
    richting = geselecteerde_richting
    
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
    bord_speler1[ver][hor] = "x"
    
    boten_info[geselecteerde_boot]["aantal"] -= 1 # laat de speler zien hoeveel boten er nog van deze soort boot geplaatst kunnen worden
    print(geselecteerde_boot , 'is geplaatst. je hebt nog:', boten_info[geselecteerde_boot]['aantal'] , "van deze boten over." )
    
    for rij in bord_speler1:
        print(rij)

#Gemaakt door:Sjoerd en Rens
def boot_plaats_checken(rij,kolom, lengte, richting,bord):
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

#Gemaakt door: Rens
def boot_plaats_willekeurig_bepalen(bord,boten_lijst):
    for naam in boten_info: 
        lengte = boten_info[naam]["lengte"]
        aantal = boten_info[naam]["aantal"]
        for _ in range(aantal): #telller wordt niet gebruikt
            geplaatst = False 
            while not geplaatst: #de while loop zorgt ervoor dat het plaatsen pas stopt wanneer de boot succesvol is geplaatst
                rij = random.randint(0, 9) # willekeurige rij van 0 tot 10
                kolom = random.randint(0, 9) # willekeurige kolom van 0 tot 10
                richting = random.choice(["horizontaal", "verticaal"]) 
                #checken of de boot hier past
                if boot_plaats_checken(rij, kolom, lengte, richting,bord): #boot moet voldoen aan plaatsingseisen
                    coordinaten = []
                    for i in range(lengte): #dit gedeelte plaatst de boten daadwerkelijk
                        if richting == "horizontaal":
                            ver = rij
                            hor = kolom + i
                        else: #richting is verticaal
                            ver = rij + i
                            hor = kolom
                        bord[ver][hor] = "x" #Zet een "x" neer op elke waarde plek van de boot
                        coordinaten.append((hor, ver)) #coordinaten worden als tuple opgeslagen en niet apart
                    #Nu nog de info lijst updaten                     
                    boten_lijst.append({"naam": naam,
                        "lengte": lengte,
                        "coordinaten": coordinaten,
                        "geraakt": [],
                        "gezonken": False})
                    geplaatst = True
    for rij in bord:
        print(rij)

def plaats_alle_boten_automatisch(): #Dit zet de boten automatisch op een willekeurige plek
    boot_plaats_willekeurig_bepalen(bord_speler1,boten_lijst_1)
    print()
    print()
    boot_plaats_willekeurig_bepalen(bord_speler2,boten_lijst_2)

#Gemaakt door: Rens
def spel_eindigen():
    global venster
    eind_melding = Label(venster, text=" Alle boten zijn gezonken! Spel afgelopen.", 
                         bg="lightblue", fg="darkred", font=("Helvetica", 16, "bold"))
    eind_melding.grid(row=11, column=0, columnspan=11, pady=20)

#thomas

#er komt nu een plaatje als je een boot raakt
def Raakplaatje(x=300, y=300, duur=1000):
    raakpiraat_img = Image.open("zeeslag/raakpiraat.png")
    raakpiraat_img = raakpiraat_img.resize((150, 150), Image.Resampling.LANCZOS)
    raakpiraat_tk = ImageTk.PhotoImage(raakpiraat_img)

    raakpiraat_label = Label(venster, image=raakpiraat_tk, bg="lightblue")
    raakpiraat_label.image = raakpiraat_tk 
    raakpiraat_label.place(x=x, y=y)

    #zorgt ervoor dat het plaatje na 1 seconde weg gaat
    venster.after(duur, raakpiraat_label.destroy)

#ook een als je de boot mist
def misplaatje(x=300, y=300, duur=1000):
    misplons_img = Image.open("zeeslag/misplons.png")
    misplons_img = misplons_img.resize((150, 150), Image.Resampling.LANCZOS)
    misplons_tk = ImageTk.PhotoImage(misplons_img)

    misplons_label = Label(venster, image=misplons_tk, bg="lightblue")
    misplons_label.image = misplons_tk 
    misplons_label.place(x=x, y=y)

    #zorgt ervoor dat het plaatje na 1 seconde weg gaat
    venster.after(duur, misplons_label.destroy)

#en als de boot gezonken is
def gezonkenplaatje(x=300, y=300, duur=3000):
    gezonkenaap_img = Image.open("zeeslag/gezonkenaap.png")
    gezonkenaap_img = gezonkenaap_img.resize((300, 300), Image.Resampling.LANCZOS)
    gezonkenaap_tk = ImageTk.PhotoImage(gezonkenaap_img)

    gezonkenaap_label = Label(venster, image=gezonkenaap_tk, bg="lightblue")
    gezonkenaap_label.image = gezonkenaap_tk 
    gezonkenaap_label.place(x=x, y=y)

    #zorgt ervoor dat het plaatje na 3 seconde weg gaat
    venster.after(duur, gezonkenaap_label.destroy)

#en als je wint
def gewonnenplaatje(duur=3000):
    gewonnen_img = Image.open("zeeslag/gewonnen.png")
    gewonnen_img = gewonnen_img.resize((500, 500), Image.Resampling.LANCZOS)
    gewonnen_tk = ImageTk.PhotoImage(gewonnen_img)

    gewonnen_label = Label(venster, image=gewonnen_tk, bg="lightblue")
    gewonnen_label.image = gewonnen_tk 
    gewonnen_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    #zorgt ervoor dat het plaatje na 3 seconde weg gaat
    venster.after(duur, gewonnen_label.destroy)


###HOOFDPROGRAMMA
welkomstscherm()

vensterWelkom.mainloop()