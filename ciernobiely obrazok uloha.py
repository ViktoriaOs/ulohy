from PIL import Image
fr = open(r"c:\Users\ostap\OneDrive\Počítač\inf\kompresia1.txt","r")
first_line = fr.readline()
sirka, vyska = first_line.strip().split()
sirka = int(sirka)
vyska = int(vyska)

obrazok = Image.new("RGB", (sirka,vyska),(255,255,255))
pixels = obrazok.load()
x = 0
y = 0
for riadok in fr:
    temp = riadok.strip()
    for x in range(0,len(temp)):
        if temp[x] == "1":
            pixels[x,y] = (255,255,255)

        if temp[x] == "0":
            pixels[x,y] = (0,0,0)
    y+=1


obrazok.show()