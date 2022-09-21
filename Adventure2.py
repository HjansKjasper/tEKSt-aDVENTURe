from random import randint
liv = 100
klokke = 0
pickpocket = 1
baguette = 0
tak = 0
pistol = 0



def jobbintervju():
    global navn
    print()
    print("Du hadde aldri trodd at du måtte ta et så vanskelig valg i livet ditt, dette jobbinervjuet hadde gått helt strålende, og hvis du nå takket ja hadde du fått lov å jobbe med det du virkelig elsker, å tilberede ferdigmat.")
    print("Uansett hva det var, Fjordlands, Toro eller Helstrøms ferdigmatserie, elsket du å tilberede det, og denne jobben ga deg muligheten til å jobbe med det hver dag, hele dagen. Følelsen av å dra av plasttoppen, sette den i mikroen og vente, var det ingenting som kunne slå.")
    print("Men du var litt usikker, tar du denne jobben hadde du aldri fått tid til hobbyen din, en annen ting du virkelig elsket, å stå i hjørnet å late som du var en potteplante. Om det var på fester eller hjemme alene, å sitte i en krukke i hjørnet med blader teipet på hodet, det var fantastisk!")
    print("Men å drømme seg bort nå er litt dumt, du er jo midt i et jobbintervju. Du har ikke hørt alt damen på den andre siden av bordet har sagt til deg mens tankene dine var et annet sted, men du starter å følge med nå.")
    print()
    print("Damen: Ja du virker jo rett og slett som den perfekte personen for denne jobben, til og med et fagbrev i å tilberede ferdigmat, det er det ikke så mange som har!")
    navn = input("Og du må unskylde meg, jeg er ikke så flink med navn, hva var det du sa du het igjen? -> ") 
    print()
    print(navn,"ja, selvfølgelig, når du sier det så husker jeg det.")
    print("Men hva sier du", navn + ", tar du jobben?")
    
    asking = True
    while asking == True:
        valg = input("A: Ta jobben B: ikke ta jobben -> ")

        if valg == "A":
            asking = False
            ta_jobben()
        elif valg == "B":
            asking = False
            ikke_ta_jobben()
        else:
            print()
            print("Det var ingen alternativ som var",valg,"prøv på nytt")

def ta_jobben():
    print()
    print("Du velger å ta jobben, og du ser øynene til damen lyse opp.")
    print("Damen: Virkelig fantastisk! Men da starter du i morgen, og jeg ønsker deg virkelig lykke til!")
    print()
    print("Du reiser deg fra stolen, og begynner å gå mot døra, men på veien ut ser du at damen har en virkelig fin og dyr klokke hengende på armen. Du er ikke en veldig flink lommetyv, men du fikk veldig lyst på klokken.")
    print("Prøver du å stjele klokken uten at hun merker det, eller lar du det være?")
    valg = input("A: Prøve å stjele klokken B: Bare fortsette videre -> ")

    if valg == "A":
        stjel_klokke()
    elif valg == "B":
        gang()

def stjel_klokke():
    print()
    print("Rett før du er ute av døren stopper du opp.")
    print("Damen: Hva foregår?")
    print("Du later som du snubler i noe, og faller i retning mot damen.")
    input("Du er ikke spesielt god på lommetyveri, og har en 50 prosent sjanse til å klare det, trykk på enter for å se hva som skjer.")
    rand = randint(1,2)

    if rand == 1:
        heldig()
    elif rand == 2:
        uheldig()

def heldig():
    global liv, klokke, pickpocket
    print()
    print("Du var heldig, og klarte å få med deg klokken, uten at hun merket at du tok den. Men det så litt dumt ut, du ligger på bakken og du kjenner at du skadet kneet ditt.")
    print()
    print("Du mistet litt liv, fikk en dyr klokke og ble litt bedre på lommetyveri.")
    print()
    print("Damen ser litt dumt på deg mens du reiser deg og går ut av rommet uten å si noen ting.")
    liv -= 10
    klokke += 1
    pickpocket += 1
    korridor()

def uheldig():
    print()
    print("Du var desverre ikke fullt så heldig, damen trekker seg unna, og bak henne står et bord. Du er midt i fallet nå og kan ikke stoppe det på noen som helst måte. Du treffer bordet med hodet først og dør")
    print("Bedre lykke neste gang!")
    input()
    exit()

def gang():
    global baguette, navn
    print()
    print("Du går ut av rommet, og damen følger etter deg, hun stopper deg.")
    print("Damen: Du,",navn + " jeg syntes faktisk du var så kul at du skal få denne baguetten av meg.")
    print()
    print("Du fikk 1 baguette!")
    baguette += 1
    korridor() 

def korridor():
    print()
    print("Du fortsetter lengre ut i gangen, du kjenner at du gleder deg til å jobbe med ferdigmat. Selv om du er brennende engasjert for å leke potteplante, føler du at du gjorde det rette valget.")
    print("Frisk luft hadde vært litt greit nå, og siden du nå befinner deg i tolvte etasje, hadde det vært litt forfriskende å gå opp på taket for å få litt luft og en fin utsikt.")
    print("Velger du å gå opp på taket, eller drar du bare hjem?")
    valg = input("A: Gå opp på taket B: Gå hjem -> ")

    if valg == "A":
        taket()

    elif valg =="B":
        første_etasje()

def første_etasje():
    global pickpocket
    print()
    print("Du bestemmer deg for å dra rett hjem, så du tar heisen ned til første etasje")
    print("Du står i heisen med en annen mann, og du ser han har noe tungt i lommen sin")
    if pickpocket == 1:
        print("Du er ikke den beste lommetyven i verden og kommer til å ha en 50 prosent sjanse til å klare å stjele fra mannen")
        print("Prøver du å stjele fra mannen?")
        valg = input("A: Prøv å stjele fra mannen B: La være -> ")
        
        if valg == "A":
            stjel_fra_mannen()

        elif valg == "B":
            ikke_stjel_fra_mannen()

    if pickpocket > 1:
        print("Du er ikke en så aller verst lommetyv, og kommer til å ha en 66.6 prosent sjanse til å klare å stjele fra mannen")
        print("Prøver du å stjele fra mannen?")
        valg = input("A: Prøv å stjele fra mannen B: La være -> ")

        if valg == "A":
            stjel_fra_mannen2()
        
        elif valg == "B":
            ikke_stjel_fra_mannen()

def stjel_fra_mannen():
    print()
    print("Du velger å prøve å stjele fra mannen, du har en 50 prosent sjanse til å klare det")
    input("Trykk på enter for å se hva som skjer ")
    rand = randint(1,2)

    if rand == 1:
        uheldig2()
    elif rand == 2:
        heldig2()

def stjel_fra_mannen2():
    print()
    print("Du velger å prøve å stjele fra mannen, du har en 66.6 prosent sjanse til å klare det.")
    input("Trykk på enter for å se hva som skjer. ")
    rand = randint(1,3)

    if rand == 1:
        uheldig2()
    elif rand > 1:
        heldig2()

def ikke_stjel_fra_mannen():
    print()
    print("Du velger å ikke stjele fra mannen.")
    print("Heisen stopper i første etasje, og du begynner å gå mot døra ut.")
    taket2()

def uheldig2():
    global pickpocket
    print()
    print("Du var desverre uheldig, og bommet på lommen til mannen, men heldigvis merket ikke mannen noen ting.")
    print()
    print("Du ble desverre litt dårligere i lommetyveri.")
    print()
    pickpocket -=1
    print("Heisen stopper i første etasje, og du begynner å gå mot døra ut.")
    taket2()

def heldig2():
    global pistol, pickpocket
    print()
    print("Du var heldig, og du klarte å stjele fra mannen uten at han merket noen ting, men sjokkerende nok hadde mannen en pistol i lomma.")
    print()
    print("Du ble en litt bedre lommetyv")
    print("Du fikk en pistol.")
    pickpocket +=1
    pistol +=1
    print()
    print("Heisen stopper i første etasje, og du begynner å gå mot døra ut.")
    taket2()

def taket():
    print()
    print("Du velger å gå opp på taket, temperaturen er helt perfekt. Dagen så langt hadde vært litt for varm, men her var det en god vind som hjalp.")
    if baguette > 0:
        print("Når du sitter der kjenner du at du begynner å bli litt sulten, du husker også at du en gang leste at baguetter gjorde deg en bedre lommetyv. (Det var kanskje i se og hør du leste det)")
        print("Velger du å spise baguetten din, eller sparer du den til senere?")
        print()
        valg = input("A: Spise baguetten B: Spare den til senere -> ")

        if valg == "A":
            spis_baguette()
        elif valg == "B":
            ikke_spis_baguette()
    else:
        print()
        print("Når du sitter der kjenner du at du begynner å bli litt sulten, men du har desverre ikke med deg noe mat du kan spise.")
        taket2()

def spis_baguette():
    global pickpocket, tak
    print()
    print("Du velger å spise baguetten, den smakte veldig godt, og du merket at du ble en bedre lommetyv!")
    pickpocket += 1
    tak = 1
    taket2()

def ikke_spis_baguette():
    print()
    print("Du velger å ikke spise baguetten, selv om den ser ganske god ut.")
    taket2()

def taket2():
    print()
    if tak == 1:
        print("Men nå må du komme deg hjem, du går ned fra taket og forsetter helt ned til første etasje.")
    print("Du kjenner det blir godt å komme deg hjem, det har vært en lang dag.")
    print("Men jo nærmere døra ut du kommer, jo mere urolig blir du. Du ser en gjeng med høye sterke menn, kledd i svart stå utenfor. Det ser ut som de venter på noen.")
    print("Bare for sikkerhets skyld tenker du at det er lurt å finne en annen vei ut. Du snur deg, men der står det en mann som nå blokkerer veien tilbake. Nå er det ingen annen vei ut.")
    print("Går du ut døren, eller prøver du å presse deg forbi mannen bak deg for så å rømme?")

    asking = True
    while asking == True:
        valg = input("A: Gå ut døra B: Prøve å rømme -> ")

        if valg == "A":
            asking = False
            gå_ut()

        elif valg == "B":
            asking = False
            rømme()

        else:
            print()
            print("Det var ingen alternativ som var",valg,"prøv på nytt")

def rømme():
    global pistol, baguette
    if pistol == 1:
        print()
        print("Du prøver å rømme, men mannen lar deg ikke forbi. Du drar ut pistolen din og truer mannen, før du vet ordet av det blir du skutt og du dør")
        input("Bedre lykke neste gang, trykk enter for å starte på nytt")
        jobbintervju()

    else:
        print("Du prøver å rømme, men mannen lar deg ikke komme forbi")
        if baguette == 1:
            print()
            print("Du har en baguette til overs, så du spør pent om mannen vil ha en baguette. Mannen takker ja og han lar deg komme forbi")
            print("Du rømmer og lever lykkelig resten av livet ditt")
            input("Trykk enter for å lukke spillet")
            exit
        else:
            print()
            print("Du blir skutt for å prøve og rømme, du dør av skuddet")
            input("Bedre lykke neste gang! Trykk enter for å prøve på nytt")
            jobbintervju()

def gå_ut():
    global klokke, pistol
    print()
    print("Du velger å gå ut døren, og du blir konfrontert av mennene. De forteller at hvis noen fortjener å få lov til å jobbe med å tilberede ferdigmat, bør det være dem. De har jobbet hele sitt liv for dette, og nå hadde du ødelagt drømmen deres.")
    print("Derfor fortjener du å dø.")
    if klokke == 1 and pistol == 1:
        print()
        print("Men du har vært så flink, du har både fått tak i en klokke og en pistol, derfor fortjener du å leve, mennene lar deg gå og du lever lykkelig resten av livet ditt")
        input("trykk enter for å lukke spillet")
        exit

    else:
        print()
        print("Du blir skutt og du dør")
        input("Bedre lykke neste gang (Kanskje du kan klare å overleve?) trykk enter for å prøve på nytt")
        jobbintervju()

def ikke_ta_jobben():
    print()
    print("Du velger å ikke ta jobben")
    print("Hjertet ditt stopper og du dør momentat")
    input("Bedre lykke neste gang, trykk enter for å prøve på nytt")
    jobbintervju()




jobbintervju()