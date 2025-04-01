def konvertuj_subor(vstupny_subor: str, vystupny_subor: str):
    with open(vstupny_subor, "r") as f:
        riadky = f.readlines()
    
    sirka, vyska = map(int, riadky[0].split())
    

    spracovane_riadky = [spracuj_riadok(riadok.strip()) for riadok in riadky[1:]]
    
    
    with open(vystupny_subor, "w") as f:
        f.write(f"{sirka} {vyska}\n")
        f.write("\n".join(spracovane_riadky))


konvertuj_subor("ciernobiely_obrazok_1.txt", "konverzia_suboru_1_vystup.txt")
