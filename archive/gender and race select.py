import csv

gender_list = ["Female","Male"]
race_list = ["Human","Fey","Dwarf","Goblin","Salimar","Treefolk","Karhu","Lizardfolk"]

"""
Gather Human Races
"""
f = open('Races.csv','r')
reader = csv.reader(f)
human_race = []
for column in reader:
    human_race.append(column[1])
human_race.remove('Human Race')



while True:
    print("Press Enter to generate a characters race and gender")
    input()
    import random
    gender_roll = random.randint(1,2) -1
    race_roll = random.randint(1,len(race_list)) - 1
    
    if race_list[race_roll] == 'Human':
        h_race_roll = random.randint(1,len(race_list)) - 1
        #print("Gender: ",gender_list[gender_roll])
        #print("Race: ",race_list[race_roll],human_race[h_race_roll])
        print("\nYour character is: ",gender_list[gender_roll],race_list[race_roll],"(",human_race[h_race_roll],")\n")
    else:
#    gender_roll = gender_roll - 1

        #print("Gender: ",gender_list[gender_roll])
        #print("Race: ",race_list[race_roll])

        print("\nYour character is: ",gender_list[gender_roll],race_list[race_roll],"\n")

    
    
