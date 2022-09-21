print("Du sitter alene på rommet ditt, du hører plutselig en merkelig lyd.")
print("Velger du å undersøke hva lyden er, eller bryr du deg ikke?")

valg = input("A: Undersøke lyden, B: Ikke bry deg -> ")

if valg == "A":
    print("Du går sakte ned trappen, ned til kjøkkenet. Du ser rundt hjørnet og der står bestemoren din og spiser opp kjøkkenet ditt")
    print("Bestemoren din legger ikke merke til at du ser henne. Du kan enten konfrontere henne, eller ringe politiet, hva gjør du?")
    valg = input("A: Konfrontere henne, B: Ringe politiet -> ")

    if valg == "B":
        print("Du hjemmer deg bak veggen så hun ikke ser deg, du får tatt ut telefonen av lomma, og gjør deg klar til å ringe politiet. Men så ser du at du har fått en melding fra det Norske ferdigmatsinstitutt (DNF forkorttet) det står i meldingen at de endelig har funnet en jobb til deg")
        print("Etter mye leting og søking har de funnet en jobb til deg hvor du kan jobbe med det du virkelig elsker, å lage ferdigmat. Velger du å ta jobbtilbudet og få en karriere innenfor ferdigmat, eller ringer du politiet for å rapportere bestemoren din?")
        valg = input("A: Ta jobben B: Ringe politiet -> ")

        
    if valg == "A":
        print("Du velger å konfrontere bestemoren din om hvorfor hun spiser kjøkkenet, hun ser veldig sur ut og begynner å løpe etter deg.")
        print("Hun har spist veldig mye kake i sitt liv og ryggen hennes er ikke topp, så hun løper ikke serlig raskt. Men hun klarer å jage deg ut i hagen")
        print("Du prøver å løpe ut av hagen og komme deg vekk, men du legger merke til en tung hagenisse du kan skade bestemoren din med. Velger du å prøve å komme deg unna, eller angripe henne med hagenissen?")
        valg = input("A: Komme deg vekk, B: Angripe henne -> ")



if valg == "B":
    print("Du velger å ikke undersøke lyden. Du er trøtt så du legger deg, det var dumt for mens du sover kommer bestemoren din opp på rommet ditt og stjeler alle eiendelene dine.")