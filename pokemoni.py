
import json
#convert json to slovnik slovnikov
with open(r"c:\Users\ostap\OneDrive\Počítač\inf\sila.json", "r", encoding="utf-8") as src:
    data = json.load(src)
att = {}
for key in data['super effective']:
    att[key] = {}
    for keyy in data['super effective']:
        att[key][keyy] = 1
for keyx in data['super effective']:
    for i in data['super effective'][keyx]:
        att[keyx][i] = 2
for keyx in data['not very effective']:
    for i in data['not very effective'][keyx]:
        att[keyx][i] = 0.5
for keyx in data['no effect']:
    for i in data['no effect'][keyx]:
        att[keyx][i] = 0.5
def power(team1:list, team2:list): 
    teampow = 0
    for k in team1:
        for x in team2:
            a = k.split(' ')
            b = x.split(' ')
            total = []
            for i in a:
                temp = 1
                for y in b:
                    temp = temp*att[i][y]
                total.append(temp)
            teampow += max(total)
    return teampow
def attack(N1:int,N2:int, listpok:str):
    listpok = listpok.split(',')
    t1 = listpok[:N1]   #rozdelenie na timy
    t2 = listpok[N1:]
    t1pow = power(t1,t2) 
    t2pow = power(t2,t1)
    
    if t1pow > t2pow:
        winner = "ME"
    elif t1pow < t2pow:
        winner = "FOE"
    else:
        winner = "EQUAL"
    return (t1pow, t2pow, winner)


print(attack(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))
#attack(input('a: '), input('b: '))