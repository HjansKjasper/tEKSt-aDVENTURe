from random import randint
liv = 100
klokke = 0
pickpocket = 10
baguette = 0

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
valg = input("A: Ta jobben B: ikke ta jobben -> ")

if valg == "A":
    print()
    print("Du velger å ta jobben, og du ser øynene til damen lyse opp.")
    print("Damen: Virkelig fantastisk! Men da starter du i morgen, og jeg ønsker deg virkelig lykke til!")
    print()
    print("Du reiser deg fra stolen, og begynner å gå mot døra, men på veien ut ser du at damen har en virkelig fin og dyr klokke hengende på armen. Du er ikke en veldig flink lommetyv, men du fikk veldig lyst på klokken.")
    print("Prøver du å stjele klokken uten at hun merker det, eller lar du det være?")
    valg = input("A: Prøve å stjele klokken B: Bare fortsette videre -> ")

    if valg == "A":
        print()
        print("Rett før du er ute av døren stopper du opp.")
        print("Damen: Hva foregår?")
        print("Du later som du snubler i noe, og faller i retning mot damen.")
        input("Du er ikke spesielt god på lommetyveri, og har en 50 prosent sjanse til å klare det, trykk på enter for å se hva som skjer.")
        rand = randint(1,2)
    
        if rand == 1:
            print()
            print("Du var heldig, og klarte å få med deg klokken, uten at hun merket at du tok den. Men det så litt dumt ut, du ligger på bakken og du kjenner at du skadet kneet ditt.")
            print()
            print("Du mistet litt liv, fikk en dyr klokke og ble litt bedre på lommetyveri.")
            print()
            print("Damen ser litt dumt på deg mens du reiser deg og går ut av rommet uten å si noen ting.")
            liv -= 10
            klokke += 1
            pickpocket += 10

        if rand == 2:
            print()
            print("Du var desverre ikke fullt så heldig, damen trekker seg unna, og bak henne står et bord. Du er midt i fallet nå og kan ikke stoppe det på noen som helst måte. Du treffer bordet med hodet først og dør")
            print("Bedre lykke neste gang!")
            exit()

    if valg == "B":
        print()
        print("Du går ut av rommet, og damen følger etter deg, hun stopper deg.")
        print("Damen: Du,",navn + " jeg syntes faktisk du var så kul at du skal få denne baguetten av meg.")
        print()
        print("Du fikk 1 baguett")
        baguette += 1

print()
print("Du fortsetter lengre ut i gangen, du kjenner at du gleder deg til å jobbe med ferdigmat. Selv om du er brennende engasjert for å leke potteplante, føler du at du gjorde det rette valget.")
print("Frisk luft hadde vært litt greit nå, og siden du nå befinner deg i tolvte etasje, hadde det vært litt forfriskende å gå opp på taket for få litt luft og en fin utsikt.")
print("Velger du å gå opp på taket, eller drar du bare hjem?")
valg = input("A: Gå opp på taket B: Gå hjem -> ")

if valg == "A":
    print()
    print("Du velger å gå opp på taket, temperaturen er helt perfekt. Dagen så langt hadde vært litt for varm, men her var det en god vind som hjalp.")
    if baguette > 0:
        print("Når du sitter der kjenner du at begynner å bli litt sulten, du husker også at du en gang leste at baguetter gjorde deg en bedre lommetyv (det var kanskje i se og hør")

    
    