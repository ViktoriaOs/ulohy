from PIL import Image
obrazok = Image.new("RGB", (50, 50), (255, 255, 255))
pixels = obrazok.load()
sirka, vyska = obrazok.size
ram = 0

for ram in range(0, min(sirka, vyska) // 2, 2):
    for x in range(ram, sirka - ram):
        pixels[x, ram] = (0, 0, 0)
        pixels[x, vyska - ram - 1] = (0, 0, 0)
    for y in range(ram, vyska - ram):
        pixels[ram, y] = (0, 0, 0)
        pixels[sirka - ram - 1, y] = (0, 0, 0)
    ram += 2
obrazok.show()