with open("pangakonto.txt") as fail:
    sisu = fail. readlines()
for number in sisu:
    print(float(number))