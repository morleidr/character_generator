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

#   Male Character
if gender == 'Male':
    
    if race == 'Human':
        hr_roll = random.randint(1,len(human_races))-1
        human_race = human_races[hr_roll]

        #   Name Based on Human Race
        if human_race == 'Arabic':
            
            print('Human', gender,">", human_race)
            
            # Arabic Names based on:
            # Given name + Father name + Grandfather name
            
            print(m_ArabicNames[random.randint(1,len(m_ArabicNames))-1],
                  m_ArabicNames[random.randint(1,len(m_ArabicNames))-1],
                  m_ArabicNames[random.randint(1,len(m_ArabicNames))-1])
            
        elif human_race == 'Celtic':
            
            print('Human', gender,">", human_race)
            
            # Celtic M names shall be one of:
            # 1. x son of x(father) Patronymic
            # 2. x ap/ab x(father)
            # 2. x of x(place)
            # 3. x the x(noun)
            # https://en.wikipedia.org/wiki/Patronymic_surname

            # Determine connector
            m_CelticConnectors = ['son of','ap','ab','of','the']            
            m_CelticConnector = m_CelticConnectors[random.randint(1,len(m_CelticConnectors))-1] 
            print(m_CelticConnector)
            
            # Determine Name from connector
            if m_CelticConnector == 'the':
                
                print(m_CelticNames[random.randint(1,len(m_CelticNames))-1],m_CelticConnector,
                      Nouns[random.randint(1,len(Nouns))-1])      
                
            elif m_CelticConnector == 'of':
                
                print(m_CelticNames[random.randint(1,len(m_CelticNames))-1],m_CelticConnector,
                      Places[random.randint(1,len(Places))-1])
                
            else:
                
                print(m_CelticNames[random.randint(1,len(m_CelticNames))-1],m_CelticConnector,
                      m_CelticNames[random.randint(1,len(m_CelticNames))-1])

                
            
        elif human_race == 'Chinese':
            print('Human', gender,">", human_race)
            
            # Chinese M names shall be based on:
            # Family Name + Given Name
            
            print(fam_ChineseNames[random.randint(1,len(fam_ChineseNames))-1],
                  m_ChineseNames[random.randint(1,len(m_ChineseNames))-1])
            
        elif human_race == 'Egyptian':
            
            # Egyptian Names based on:
            # Given name + Father name + Grandfather name
            
            print('Human', gender,">", human_race)
            print(m_EgyptianNames[random.randint(1,len(m_EgyptianNames))-1],
                  m_EgyptianNames[random.randint(1,len(m_EgyptianNames))-1],
                  m_EgyptianNames[random.randint(1,len(m_EgyptianNames))-1])
            
        elif human_race == 'English':
            
            print('Human', gender,">", human_race)
            
            # English M names shall be one of:
            # 1. x son of x(father) Patronymic
            # 2. x of x(place)
            # 3. x the x(noun)
            # https://en.wikipedia.org/wiki/Patronymic_surname
            
            # Determine Connector
            m_EnglishConnectors = ['son of','of','the']
            m_EnglishConnector = m_EnglishConnectors[random.randint(1,len(m_EnglishConnectors))-1]
            print(m_EnglishConnector)
            
            # Determine Name based on Connector
            if m_EnglishConnector == 'the':
                
                print(m_EnglishNames[random.randint(1,len(m_EnglishNames))-1],m_EnglishConnector,
                      Nouns[random.randint(1,len(Nouns))-1])
                
            elif m_EnglishConnector == 'of':
                
                print(m_EnglishNames[random.randint(1,len(m_EnglishNames))-1],m_EnglishConnector,
                      Places[random.randint(1,len(Places))-1])
            
            else:
                
                print(m_EnglishNames[random.randint(1,len(m_EnglishNames))-1],m_EnglishConnector,
                      m_EnglishNames[random.randint(1,len(m_EnglishNames))-1])
                       
        elif human_race == 'French':
            
            # French M names shall be based on:
            # Given name + Surname (based on Top 100 French Surnames)
            
            print('Human', gender,">", human_race)
            print(m_FrenchNames[random.randint(1,len(m_FrenchNames))-1],
                  FrenchSurnames[random.randint(1,len(FrenchSurnames))-1])
            
        elif human_race == 'German':
            
            # German M names shall be based on:
            # Given name + middle name + surname (taken from Top 100)
            
            print('Human', gender,">", human_race)
            print(m_GermanNames[random.randint(1,len(m_GermanNames))-1],
                  m_GermanNames[random.randint(1,len(m_GermanNames))-1],
                  GermanSurnames[random.randint(1,len(GermanSurnames))-1])
            
        elif human_race == 'Greek':
            print('Human', gender,">", human_race)
            print('Greek M Name')
        elif human_race == 'Indian':
            print('Human', gender,">", human_race)
            print('Indian M Name')
            
        elif human_race == 'Japanese':
            print('Human', gender,">", human_race)
            print('Japanese M Name')
            
        elif human_race == 'Mesoamerican':
            print('Human', gender,">", human_race)
            print('Mesoamerican M Name')
            
        elif human_race == 'Niger-Congo':
            print('Human', gender,">", human_race)
            print('Congolese M Name')
            
        elif human_race == 'Norse':
            print('Human', gender,">", human_race)
            print('Norse M Name')
            
        elif human_race == 'Polynesian':
            print('Human', gender,">", human_race)
            print('Polynesian M Name')
            
        elif human_race == 'Roman':
            print('Human', gender,">", human_race)
            print('Roman M Name')
            
        elif human_race == 'Slavic':
            print('Human', gender,">", human_race)
            print('Slavic M Name')
            
        else:
            print('Human', gender,">", human_race)
            print('Spanish M Name')
        

        
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
     

    
#   Female Character
else:
    if race == 'Human':
        hr_roll = random.randint(1,len(human_races))-1
        human_race = human_races[hr_roll]

        #   Name Based on Human Race
        if human_race == 'Arabic':
            print('Human', gender,">", human_race)
            print('Arabic F Name')
            
        elif human_race == 'Celtic':
            print('Human', gender,">", human_race)
            print('Celtic F Name')
            
        elif human_race == 'Chinese':
            print('Human', gender,">", human_race)
            print('Chinese F Name')
            
        elif human_race == 'Egyptian':
            print('Human', gender,">", human_race)
            print('Egyptian F Name')
            
        elif human_race == 'English':
            print('Human', gender,">", human_race)
            print('English F Name')
            
        elif human_race == 'French':
            print('Human', gender,">", human_race)
            print('French F Name')
            
        elif human_race == 'German':
            print('Human', gender,">", human_race)
            print('German F Name')
            
        elif human_race == 'Greek':
            print('Human', gender,">", human_race)
            print('Greek F Name')
            
        elif human_race == 'Indian':
            print('Human', gender,">", human_race)
            print('Indian F Name')
            
        elif human_race == 'Japanese':
            print('Human', gender,">", human_race)
            print('Japanese F Name')
            
        elif human_race == 'Mesoamerican':
            print('Human', gender,">", human_race)
            print('Mesoamerican F Name')
        elif human_race == 'Niger-Congo':
            print('Human', gender,">", human_race)
            print('Congolese F Name')
            
        elif human_race == 'Norse':
            print('Human', gender,">", human_race)
            print('Norse F Name')
            
        elif human_race == 'Polynesian':
            print('Human', gender,">", human_race)
            print('Polynesian F Name')
            
        elif human_race == 'Roman':
            print('Human', gender,">", human_race)
            print('Roman F Name')
            
        elif human_race == 'Slavic':
            print('Human', gender,">", human_race)
            print('Slavic F Name')
            
        else:
            print('Human', gender,">", human_race)
            print('Spanish F Name')
        
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

    









