#Kuva mõõdetava kuu nimetus
#Kuva viimase mõõtmise tulemus
#Kuva ainult temperatuurid
#Leia kuu maksimaalne ja minimaalne temperatuur
#Leia kuu keskmine temperatuur
#Mitu korda esines -20 kraadi
#Eemalda element nr 5
#Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
#Sorteeri temperatuurid nimekirjas kasvavas järjekorras

jtemp = ["jaanuar", -16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,

print(f"Mõõdetav kuu: {jtemp[0]}")       ]
print(f"Viimane mõõtmise tulemus: {jtemp[-1]}kraadi")

maks = -100
mini = 100

for t in range(1,len(jtemp)):
    print(jtemp[t], end= "")  #prindib kõik tempid
    if jtemp[t]>maks:
        maks = jtemp[t]
    if jtemp[t]<mini:
        mini = jtemp[t]
    summa+=jtemp[t]
    kokku+=1
    if jtemp[t]== -20:
       kordused+=1
    
    jtemp.pop(5)  #kustutab
    jtemp.insert(5,55)  #lisab
    temps.sort()


   
