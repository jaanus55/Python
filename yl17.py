with open("pangakonto.txt") as fail:
    sisu = fail. readlines()
for number in sisu:
    #print(float(number))
    tehingute_arv+=1
    if float(number) > 0:
        tehingute_arv_pos += 1
        pos_arv_summa += float(number)


        print(f"Tehingute arv: {tehingute_arv}")
        print(f"Positiivsete tehingute arv: {tehingute_arv_pos}")
        print(f"Positiivsete arvude summa: {pos_arv_summa: 2f)")
        


npalgad = 0
#See on teine ülesanne
with open("palgad.txt") as fail:
    sisu = fail. readlines
