"""
D&D Character Generator
-----------------------
Based on the Tiny Dungeon characters

By Morleidr
"""

import random
from character_data import *


#   Determine Gender
genders = ['Male','Female']
g_roll = random.randint(1,len(genders))-1
gender = genders[g_roll]


#   Determine Race
r_roll = random.randint(1,len(races))-1
race = races[r_roll]


#   Determine Name
#   Based on Race
if gender == 'Male':
    if race == 'Human':
        # need more if statements for human race
        print('Human', gender)
    elif race == 'Fey':
        print('Fey', gender)
    elif race == 'Dwarf':
        print('Dwarf', gender)
    elif race == 'Goblin':
        print('Goblin', gender)
    elif race == 'Salimar':
        print('Salimar', gender)
    elif race == 'Treefolk':
        print('Treefolk', gender)
    elif race == 'Karhu':
        print('Karhu', gender)
    else:
        print('Lizardfolk', gender)
    
        

    
##    lf_roll = random.randint(1,len(m_LizardfolkNames))-1
##    print("Name: ", m_LizardfolkNames[lf_roll])
else:
    if race == 'Human':
        # need more if statements for human race
        print('Human', gender)
    elif race == 'Fey':
        print('Fey', gender)
    elif race == 'Dwarf':
        print('Dwarf', gender)
    elif race == 'Goblin':
        print('Goblin', gender)
    elif race == 'Salimar':
        print('Salimar', gender)
    elif race == 'Treefolk':
        print('Treefolk', gender)
    elif race == 'Karhu':
        print('Karhu', gender)
    else:
        print('Lizardfolk', gender)
##    lf_roll = random.randint(1,len(f_LizardfolkNames))-1
##    print(f_LizardfolkNames[lf_roll])

    









