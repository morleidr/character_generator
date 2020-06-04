"""
D&D Character Generator
-----------------------
Based on the Tiny Dungeon characters

By Morleidr
"""

import random
from character_data import *


while True:
    print("\nPress Enter to generate a character")
    input()

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
                
                print("Name: ",
                      m_ArabicNames[random.randint(1,len(m_ArabicNames))-1],
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
                
                # Determine Name from connector
                if m_CelticConnector == 'the':
                    
                    print("Name: ",
                          m_CelticNames[random.randint(1,len(m_CelticNames))-1],m_CelticConnector,
                          Nouns[random.randint(1,len(Nouns))-1])      
                    
                elif m_CelticConnector == 'of':
                    
                    print("Name: ",
                          m_CelticNames[random.randint(1,len(m_CelticNames))-1],m_CelticConnector,
                          Places[random.randint(1,len(Places))-1])
                    
                else:
                    
                    print("Name: ",
                          m_CelticNames[random.randint(1,len(m_CelticNames))-1],m_CelticConnector,
                          m_CelticNames[random.randint(1,len(m_CelticNames))-1])

                    
                
            elif human_race == 'Chinese':
                print('Human', gender,">", human_race)
                
                # Chinese M names shall be based on:
                # Family Name + Given Name
                
                print("Name: ",
                      fam_ChineseNames[random.randint(1,len(fam_ChineseNames))-1],
                      m_ChineseNames[random.randint(1,len(m_ChineseNames))-1])
                
            elif human_race == 'Egyptian':
                
                # Egyptian Names based on:
                # Given name + Father name + Grandfather name
                
                print('Human', gender,">", human_race)
                print("Name: ",
                      m_EgyptianNames[random.randint(1,len(m_EgyptianNames))-1],
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
                
                # Determine Name based on Connector
                if m_EnglishConnector == 'the':
                    
                    print("Name: ",
                          m_EnglishNames[random.randint(1,len(m_EnglishNames))-1],m_EnglishConnector,
                          Nouns[random.randint(1,len(Nouns))-1])
                    
                elif m_EnglishConnector == 'of':
                    
                    print("Name: ",
                          m_EnglishNames[random.randint(1,len(m_EnglishNames))-1],m_EnglishConnector,
                          Places[random.randint(1,len(Places))-1])
                
                else:
                    
                    print("Name: ",
                          m_EnglishNames[random.randint(1,len(m_EnglishNames))-1],m_EnglishConnector,
                          m_EnglishNames[random.randint(1,len(m_EnglishNames))-1])
                           
            elif human_race == 'French':
                
                # French M names shall be based on:
                # Given name + Surname (based on Top 100 French Surnames)
                
                print('Human', gender,">", human_race)
                print("Name: ",
                      m_FrenchNames[random.randint(1,len(m_FrenchNames))-1],
                      FrenchSurnames[random.randint(1,len(FrenchSurnames))-1])
                
            elif human_race == 'German':
                
                # German M names shall be based on:
                # Given name + middle name + surname (taken from Top 100)
                
                print('Human', gender,">", human_race)

                mGivenGer = m_GermanNames[random.randint(1,len(m_GermanNames))-1]
                mMiddleGer = m_GermanNames[random.randint(1,len(m_GermanNames))-1]
                mSurnameGer = GermanSurnames[random.randint(1,len(GermanSurnames))-1]

                while mGivenGer == mMiddleGer:
                    mGivenGer = m_GermanNames[random.randint(1,len(m_GermanNames))-1]
                    mMiddleGer = m_GermanNames[random.randint(1,len(m_GermanNames))-1]
                else:
                    print("Name: ",mGivenGer,mMiddleGer,mSurnameGer)
                
            elif human_race == 'Greek':

                # Greek M names shall be based on:
                # Given name + patronymic surnamne (taken from Top 100)
                
                print('Human', gender,">", human_race)
                print("Name: ",
                      m_GreekNames[random.randint(1,len(m_GreekNames))-1],
                      GreekSurnames[random.randint(1,len(GreekSurnames))-1])
                
            elif human_race == 'Indian':

                print('Human', gender,">", human_race)

                # Indian names shall be one of:
                # 1. Given name + father name
                # 2. Father initial + given name (example: A, Kiran)
                
                # Determine name type:
                i_NameTypes = ['given','initial']
                i_NameType = i_NameTypes[random.randint(1,len(i_NameTypes))-1]
                
                # Print name based on name type    
                if i_NameType == 'given':
                    print("Name: ",
                          m_IndianNames[random.randint(1,len(m_IndianNames))-1],
                          m_IndianNames[random.randint(1,len(m_IndianNames))-1])

                else:
                    print("Name: ",
                          m_IndianNames[random.randint(1,len(m_IndianNames))-1][0],
                          m_IndianNames[random.randint(1,len(m_IndianNames))-1],
                          sep = ', ')
                
            elif human_race == 'Japanese':
                
                print('Human', gender,">", human_race)

                # Japanese M names shall be:
                # Surname + given name
                
                print("Name: ",
                      JapaneseSurnames[random.randint(1,len(JapaneseSurnames))-1],
                      m_JapaneseNames[random.randint(1,len(m_JapaneseNames))-1])
                
            elif human_race == 'Mesoamerican':

                # Mesoamerican M names shall be:
                # Given name
                
                print('Human', gender,">", human_race)
                print("Name: ",
                      m_MesoamericanNames[random.randint(1,len(m_MesoamericanNames))-1])
                
            elif human_race == 'Niger-Congo':

                # Niger-Congo M names shall be:
                # Given name + middle initial + father name
                # (There is nothing suggesting this is how
                #  naming systems are for Niger-Congo.
                #  This is made up.)
                
                print('Human', gender,">", human_race)
                print("Name: ",
                      m_CongoleseNames[random.randint(1,len(m_CongoleseNames))-1],
                      m_CongoleseNames[random.randint(1,len(m_CongoleseNames))-1][0],
                      m_CongoleseNames[random.randint(1,len(m_CongoleseNames))-1])
                
            elif human_race == 'Norse':
                
                print('Human', gender,">", human_race)

                # Norse M names shall be patronymic:
                # Father name ending -i becomes -ason
                # Father name ending -a becomes -uson
                # Father name ending -nn becomes -nsson
                # Father name ending -ll becomes -lsson
                # Father name ending -rr becomes -rson
                # Father name ending -r becomes -sson
                # Father name ending not listed, add -son

                vname = m_NorseNames[random.randint(1,len(m_NorseNames))-1]
                vsuffix = vname[len(vname)-1:]

                if vsuffix == 'i':
                    print("Name: ",
                          m_NorseNames[random.randint(1,len(m_NorseNames))-1],
                          ' ',
                          vname[0:-1],'ason',sep='')
                elif vsuffix == 'a':
                    print("Name: ",
                          m_NorseNames[random.randint(1,len(m_NorseNames))-1],
                          ' ',
                          vname[0:-1],'uson',sep='')
                elif vsuffix == 'n':
                    vsuffix2 = vname[len(vname)-2:]
                    if vsuffix2 == 'nn':
                        print("Name: ",
                              m_NorseNames[random.randint(1,len(m_NorseNames))-1],
                              ' ',
                              vname[0:-1],'sson',sep='')
                    else:
                        print("Name: ",
                              m_NorseNames[random.randint(1,len(m_NorseNames))-1],
                              ' ',
                              vname[0:-1],'son',sep='')
                elif vsuffix == 'l':
                    vsuffix2 = vname[len(vname)-2:]
                    if vsuffix2 == 'll':
                        print("Name: ",
                              m_NorseNames[random.randint(1,len(m_NorseNames))-1],
                              ' ',
                              vname[0:-1],'sson',sep='')
                    else:
                        print("Name: ",
                              m_NorseNames[random.randint(1,len(m_NorseNames))-1],
                              ' ',
                              vname[0:-1],'son',sep='')
                elif vsuffix == 'r':
                    vsuffix2 = vname[len(vname)-2:]
                    if vsuffix2 == 'rr':
                        print("Name: ",
                              m_NorseNames[random.randint(1,len(m_NorseNames))-1],
                              ' ',
                              vname[0:-1],'son',sep='')
                    else:
                        print("Name: ",
                              m_NorseNames[random.randint(1,len(m_NorseNames))-1],
                              ' ',
                              vname[0:-1],'sson',sep='')
                else:
                    print("Name: ",
                          m_NorseNames[random.randint(1,len(m_NorseNames))-1],
                          ' ',
                          vname,'son',sep='')
                
                
            elif human_race == 'Polynesian':

                # Polynesian M Name shall be:
                # Given name + patronymic name
                
                print('Human', gender,">", human_race)
                
                print("Name: ",
                      m_PolynesianNames[random.randint(1,len(m_PolynesianNames))-1],
                      m_PolynesianNames[random.randint(1,len(m_PolynesianNames))-1])
                
            elif human_race == 'Roman':

                # Roman M Name shall be:
                # praenomen + nomen + cognomen
                
                print('Human', gender,">", human_race)

                praenomen = m_RomanNames[random.randint(1,len(m_RomanNames))-1]
                nomen = m_RomanNames[random.randint(1,len(m_RomanNames))-1]
                cognomen = m_RomanNames[random.randint(1,len(m_RomanNames))-1]
                
                # 'while loop' to ensure no repetition of name
                while praenomen == nomen or praenomen == cognomen or nomen == cognomen:
                    praenomen = m_RomanNames[random.randint(1,len(m_RomanNames))-1]
                    nomen = m_RomanNames[random.randint(1,len(m_RomanNames))-1]
                    cognomen = m_RomanNames[random.randint(1,len(m_RomanNames))-1]
                else:
                    print("Name: ",
                          praenomen,nomen,cognomen)
                
            elif human_race == 'Slavic':

                print('Human', gender,">", human_race)

                # Slavic M names shall be patronymic:
                # Father name ending is consonant add -ovic
                # Father name ending is vowel, omit last vowel, add -yevic

                sname = m_SlavicNames[random.randint(1,len(m_SlavicNames))-1]
                sSuffix = sname[len(sname)-1:]


                if sSuffix == 'a' or sSuffix == 'e' or sSuffix == 'i' or sSuffix == 'o' or sSuffix == 'u':
                    print("Name: ",
                          m_SlavicNames[random.randint(1,len(m_SlavicNames))-1],
                          ' ',
                          sname[0:-1],'yevic',sep='')
                else:
                    print("Name: ",
                          m_SlavicNames[random.randint(1,len(m_SlavicNames))-1],
                          ' ',
                          sname,'ovic',sep='')

                
            else:
                
                # Spanish Names shall be:
                # Given name + Surname
                
                print('Human', gender,">", human_race)
                
                print("Name: ",
                      m_SpanishNames[random.randint(1,len(m_SpanishNames))-1],
                      SpanishSurnames[random.randint(1,len(SpanishSurnames))-1],sep='')
            

            
        elif race == 'Fey':
            
            # Fey M names shall be:
            # Given name + Family name + matronymic name
            # Matronymic name = dír/mír/kír/tír + mother's name
            # example: Adran Firahel dírEnna
            
            FeyMatronymic = ['dír','mír','kír','tír']
            
            print('Fey', gender)
            print("Name: ",
                  m_FeyNames[random.randint(1,len(m_FeyNames))-1],' ',
                  fam_FeyNames[random.randint(1,len(fam_FeyNames))-1],' ',
                  FeyMatronymic[random.randint(1,len(FeyMatronymic))-1],
                  f_FeyNames[random.randint(1,len(f_FeyNames))-2],sep='')
            
        elif race == 'Dwarf':
            
            print('Dwarf', gender)

            # Dwarf M names shall be one of:
            # 1. Given name + son of + father name
            # 2. Given name + clan name

            dConnectors = ['son of', 'clan']
            dConnector = dConnectors[random.randint(1,len(dConnectors))-1]

            dGiven = m_DwarfNames[random.randint(1,len(m_DwarfNames))-1]
            dFather = m_DwarfNames[random.randint(1,len(m_DwarfNames))-1]
            dClan = clan_DwarfNames[random.randint(1,len(clan_DwarfNames))-1]

            if dConnector == 'son of':
                while dGiven == dFather:
                    dGiven = m_DwarfNames[random.randint(1,len(m_DwarfNames))-1]
                    dFather = m_DwarfNames[random.randint(1,len(m_DwarfNames))-1]
                else:
                    print("Name: ",dGiven,dConnector,dFather)
            else:
                print("Name: ",dGiven,dClan)        
            
        elif race == 'Goblin':
            
            print('Goblin', gender)

            # Goblin M names shall be:
            # Given name + matronymic + patronymic
            # Matronymic name shall be:
            # Mother's name + tag, or tag + mother's name
            # Patronymic name shall be:
            # Father's name + gat, or gat + father's name

            gobGiven = m_GoblinNames[random.randint(1,len(m_GoblinNames))-1]
            gobMother = f_GoblinNames[random.randint(1,len(f_GoblinNames))-1]
            gobFather = m_GoblinNames[random.randint(1,len(m_GoblinNames))-1]
            gobPatron = random.randint(1,2)
            gobMatron = random.randint(1,2)

            if gobPatron == 1:
                gobPatronPos = ['Gat',gobFather.lower()]
            else:
                gobPatronPos = [gobFather,'gat']

            if gobMatron == 1:
                gobMatronPos = ['Tag',gobMother.lower()]
            else:
                gobMatronPos = [gobMother,'tag']

            print("Name: ",
                  gobGiven," ",
                  gobMatronPos[0],gobMatronPos[1]," ",
                  gobPatronPos[0],gobPatronPos[1],sep='')
            
        elif race == 'Salimar':
            
            print('Salimar', gender)

            # Salimar M names shall be:
            # Given name + father name (separated only by "-")

            salGiven = m_SalimarNames[random.randint(1,len(m_SalimarNames))-1]
            salFather = m_SalimarNames[random.randint(1,len(m_SalimarNames))-1]

            while salGiven == salFather:
                salGiven = m_SalimarNames[random.randint(1,len(m_SalimarNames))-1]
                salFather = m_SalimarNames[random.randint(1,len(m_SalimarNames))-1]
            else:
                print("Name: ",salGiven,"-",salFather.lower(),sep='')
            
        elif race == 'Treefolk':
            
            print('Treefolk', gender)

            # Treefolk M names shall be:
            # "Nickname" + family name + given name
            # Nickname shall be first 4 letters of given name
            # Family name shall be:
            # Mother's name + father's name (no spaces)

            treeGiven = m_TreefolkNames[random.randint(1,len(m_TreefolkNames))-1]
            treeNick = treeGiven[:4]
            treeMother = f_TreefolkNames[random.randint(1,len(f_TreefolkNames))-1]
            treeFather = m_TreefolkNames[random.randint(1,len(m_TreefolkNames))-1]

            print("Name: ",'"',treeNick,'"'," ",
                  treeMother,treeFather.lower()," ",treeGiven,sep='')
            
        elif race == 'Karhu':
            
            print('Karhu', gender)

            # Karhu M names shall be:
            # Given name + clan name

            karGiven = m_KarhuNames[random.randint(1,len(m_KarhuNames))-1]
            karClan = clan_KarhuNames[random.randint(1,len(clan_KarhuNames))-1]

            print("Name: ",karGiven, karClan)
            
        else:
            
            print('Lizardfolk', gender)

            # Lizardfolk M names shall be:
            # Given name + ' + clan name

            lizName = m_LizardfolkNames[random.randint(1,len(m_LizardfolkNames))-1]
            lizClan = clan_LizardfolkNames[random.randint(1,len(clan_LizardfolkNames))-1]

            print("Name: ",lizName,"'",lizClan.lower(),sep='')
         

        
    #   Female Character

    else:
        if race == 'Human':
            hr_roll = random.randint(1,len(human_races))-1
            human_race = human_races[hr_roll]

            #   Name Based on Human Race
            if human_race == 'Arabic':
                
                print('Human', gender,">", human_race)

                # Arabic Names based on:
                # Given name + Father name + Grandfather name

                print("Name: ",
                      f_ArabicNames[random.randint(1,len(m_ArabicNames))-1],
                      m_ArabicNames[random.randint(1,len(m_ArabicNames))-1],
                      m_ArabicNames[random.randint(1,len(m_ArabicNames))-1])
                
            elif human_race == 'Celtic':
                
                print('Human', gender,">", human_race)

                # Celtic F names shall be one of:
                # 1. x Ní x(father) Patronymic
                # 2. x of x(place)
                # 3. x the x(noun)
                # https://en.wikipedia.org/wiki/Patronymic_surname
                
                # Determine connector
                f_CelticConnectors = ['Ní','of','the']            
                f_CelticConnector = f_CelticConnectors[random.randint(1,len(f_CelticConnectors))-1] 
                
                # Determine Name from connector
                if f_CelticConnector == 'the':
                    
                    print("Name: ",
                          f_CelticNames[random.randint(1,len(f_CelticNames))-1],f_CelticConnector,
                          Nouns[random.randint(1,len(Nouns))-1])      
                    
                elif f_CelticConnector == 'of':
                    
                    print("Name: ",
                          f_CelticNames[random.randint(1,len(f_CelticNames))-1],f_CelticConnector,
                          Places[random.randint(1,len(Places))-1])
                    
                else:
                    
                    print("Name: ",
                          f_CelticNames[random.randint(1,len(f_CelticNames))-1],f_CelticConnector,
                          m_CelticNames[random.randint(1,len(m_CelticNames))-1])
                
            elif human_race == 'Chinese':
                
                print('Human', gender,">", human_race)

                # Chinese F names shall be based on:
                # Family Name + Given Name
                
                print("Name: ",
                      fam_ChineseNames[random.randint(1,len(fam_ChineseNames))-1],
                      f_ChineseNames[random.randint(1,len(f_ChineseNames))-1])
                
            elif human_race == 'Egyptian':
                
                print('Human', gender,">", human_race)

                # Egyptian F Names based on:
                # Given name + Father name + Grandfather name
                
                print("Name: ",
                      f_EgyptianNames[random.randint(1,len(f_EgyptianNames))-1],
                      m_EgyptianNames[random.randint(1,len(m_EgyptianNames))-1],
                      m_EgyptianNames[random.randint(1,len(m_EgyptianNames))-1])
                
            elif human_race == 'English':
                
                print('Human', gender,">", human_race)

                # English F names shall be one of:
                # 1. x daughter of x(father) Patronymic
                # 2. x of x(place)
                # 3. x the x(noun)
                # https://en.wikipedia.org/wiki/Patronymic_surname
                
                # Determine Connector
                f_EnglishConnectors = ['daughter of','of','the']
                f_EnglishConnector = f_EnglishConnectors[random.randint(1,len(f_EnglishConnectors))-1]
                
                # Determine Name based on Connector
                if f_EnglishConnector == 'the':
                    
                    print("Name: ",
                          f_EnglishNames[random.randint(1,len(f_EnglishNames))-1],f_EnglishConnector,
                          Nouns[random.randint(1,len(Nouns))-1])
                    
                elif f_EnglishConnector == 'of':
                    
                    print("Name: ",
                          f_EnglishNames[random.randint(1,len(f_EnglishNames))-1],f_EnglishConnector,
                          Places[random.randint(1,len(Places))-1])
                
                else:
                    
                    print("Name: ",
                          f_EnglishNames[random.randint(1,len(f_EnglishNames))-1],f_EnglishConnector,
                          m_EnglishNames[random.randint(1,len(m_EnglishNames))-1])
                
            elif human_race == 'French':
                
                print('Human', gender,">", human_race)

                # French F names shall be based on:
                # Given name + Surname (based on Top 100 French Surnames)
                
                print("Name: ",
                      f_FrenchNames[random.randint(1,len(f_FrenchNames))-1],
                      FrenchSurnames[random.randint(1,len(FrenchSurnames))-1])
                
            elif human_race == 'German':
                
                print('Human', gender,">", human_race)

                # German F names shall be based on:
                # Given name + middle name + surname (taken from Top 100)
                
                fGivenGer = f_GermanNames[random.randint(1,len(f_GermanNames))-1]
                fMiddleGer = f_GermanNames[random.randint(1,len(f_GermanNames))-1]
                fSurnameGer = GermanSurnames[random.randint(1,len(GermanSurnames))-1]

                while fGivenGer == fMiddleGer:
                    fGivenGer = f_GermanNames[random.randint(1,len(f_GermanNames))-1]
                    fMiddleGer = f_GermanNames[random.randint(1,len(f_GermanNames))-1]
                else:
                    print("Name: ", fGivenGer, fMiddleGer, fSurnameGer)
                
            elif human_race == 'Greek':
                
                print('Human', gender,">", human_race)

                # Greek F names shall be based on:
                # Given name + patronymic surnamne (taken from Top 100)
                
                print("Name: ",
                      f_GreekNames[random.randint(1,len(f_GreekNames))-1],
                      GreekSurnames[random.randint(1,len(GreekSurnames))-1])
                
            elif human_race == 'Indian':
                
                print('Human', gender,">", human_race)
                
                # Indian names shall be one of:
                # 1. Given name + father name
                # 2. Father initial + given name (example: A, Kiran)
                
                # Determine name type:
                i_NameTypesF = ['given','initial']
                i_NameTypeF = i_NameTypesF[random.randint(1,len(i_NameTypesF))-1]
                
                # Print name based on name type    
                if i_NameTypeF == 'given':
                    print("Name: ",
                          f_IndianNames[random.randint(1,len(m_IndianNames))-1],
                          m_IndianNames[random.randint(1,len(m_IndianNames))-1])

                else:
                    print("Name: ",
                          m_IndianNames[random.randint(1,len(m_IndianNames))-1][0],
                          f_IndianNames[random.randint(1,len(m_IndianNames))-1],
                          sep = ', ')
                
            elif human_race == 'Japanese':
                
                print('Human', gender,">", human_race)
                
                # Japanese F names shall be:
                # Surname + given name
                
                print("Name: ",
                      JapaneseSurnames[random.randint(1,len(JapaneseSurnames))-1],
                      f_JapaneseNames[random.randint(1,len(f_JapaneseNames))-1])
                
            elif human_race == 'Mesoamerican':
                
                print('Human', gender,">", human_race)
                
                # Mesoamerican F names shall be:
                # Given name
                
                print("Name: ",
                      f_MesoamericanNames[random.randint(1,len(f_MesoamericanNames))-1])
                
            elif human_race == 'Niger-Congo':
                
                print('Human', gender,">", human_race)
                
                # Niger-Congo F names shall be:
                # Given name + middle initial + father name
                # (There is nothing suggesting this is how
                #  naming systems are for Niger-Congo.
                #  This is made up.)

                print("Name: ",
                      f_CongoleseNames[random.randint(1,len(f_CongoleseNames))-1],
                      f_CongoleseNames[random.randint(1,len(f_CongoleseNames))-1][0],
                      m_CongoleseNames[random.randint(1,len(m_CongoleseNames))-1])
                
            elif human_race == 'Norse':
                
                print('Human', gender,">", human_race)
                
                # Norse f names shall be patronymic:
                # Father name ending -i becomes -adóttir
                # Father name ending -a becomes -adóttir
                # Father name ending -nn becomes -nsdóttir
                # Father name ending -ll becomes -lsdóttir
                # Father name ending -rr becomes -rssdóttir
                # Father name ending -r becomes -sdóttir
                # Father name ending not listed, add -sdóttir

                vname = m_NorseNames[random.randint(1,len(m_NorseNames))-1]
                vsuffix = vname[len(vname)-1:]

                if vsuffix == 'i':
                    print("Name: ",
                          f_NorseNames[random.randint(1,len(f_NorseNames))-1],
                          ' ',
                          vname[0:-1],'adóttir',sep='')
                elif vsuffix == 'a':
                    print("Name: ",
                          f_NorseNames[random.randint(1,len(f_NorseNames))-1],
                          ' ',
                          vname[0:-1],'adóttir',sep='')
                elif vsuffix == 'n':
                    vsuffix2 = vname[len(vname)-2:]
                    if vsuffix2 == 'nn':
                        print("Name: ",
                              f_NorseNames[random.randint(1,len(f_NorseNames))-1],
                              ' ',
                              vname[0:-1],'sdóttir',sep='')
                    else:
                        print("Name: ",
                              f_NorseNames[random.randint(1,len(f_NorseNames))-1],
                              ' ',
                              vname,'sdóttir',sep='')
                elif vsuffix == 'l':
                    vsuffix2 = vname[len(vname)-2:]
                    if vsuffix2 == 'll':
                        print("Name: ",
                              f_NorseNames[random.randint(1,len(f_NorseNames))-1],
                              ' ',
                              vname[0:-1],'sdóttir',sep='')
                    else:
                        print("Name: ",
                              m_NorseNames[random.randint(1,len(m_NorseNames))-1],
                              ' ',
                              vname,'sdóttir',sep='')
                elif vsuffix == 'r':
                    vsuffix2 = vname[len(vname)-2:]
                    if vsuffix2 == 'rr':
                        print("Name: ",
                              f_NorseNames[random.randint(1,len(f_NorseNames))-1],
                              ' ',
                              vname[0:-1],'sdóttir',sep='')
                    else:
                        print("Name: ",
                              f_NorseNames[random.randint(1,len(f_NorseNames))-1],
                              ' ',
                              vname,'sdóttir',sep='')
                else:
                    print("Name: ",
                          f_NorseNames[random.randint(1,len(f_NorseNames))-1],
                          ' ',
                          vname,'sdóttir',sep='')

                
            elif human_race == 'Polynesian':
                
                print('Human', gender,">", human_race)
                
                # Polynesian F Name shall be:
                # Given name + patronymic name
                            
                print("Name: ",
                      f_PolynesianNames[random.randint(1,len(f_PolynesianNames))-1],
                      m_PolynesianNames[random.randint(1,len(m_PolynesianNames))-1])
                
            elif human_race == 'Roman':
                
                print('Human', gender,">", human_race)
                
                # Roman F Name shall be:
                # praenomena + nomena + cognomena

                praenomena = f_RomanNames[random.randint(1,len(f_RomanNames))-1]
                nomena = f_RomanNames[random.randint(1,len(f_RomanNames))-1]
                cognomena = f_RomanNames[random.randint(1,len(f_RomanNames))-1]
                
                # 'while loop' to ensure no repetition of name
                while praenomena == nomena or praenomena == cognomena or nomena == cognomena:
                    praenomena = f_RomanNames[random.randint(1,len(f_RomanNames))-1]
                    nomena = f_RomanNames[random.randint(1,len(f_RomanNames))-1]
                    cognomena = f_RomanNames[random.randint(1,len(f_RomanNames))-1]
                else:
                    print("Name: ",
                          praenomena,nomena,cognomena)
                
            elif human_race == 'Slavic':
                
                print('Human', gender,">", human_race)
                
                # Slavic M names shall be patronymic:
                # Father name ending is consonant add -ovna
                # Father name ending is vowel, omit last vowel, add -yevna

                snamef = f_SlavicNames[random.randint(1,len(f_SlavicNames))-1]
                sSuffixf = snamef[len(snamef)-1:]


                if sSuffixf == 'a' or sSuffixf == 'e' or sSuffixf == 'i' or sSuffixf == 'o' or sSuffixf == 'u':
                    print("Name: ",
                          f_SlavicNames[random.randint(1,len(f_SlavicNames))-1],
                          ' ',
                          snamef[0:-1],'yevna',sep='')
                else:
                    print("Name: ",
                          f_SlavicNames[random.randint(1,len(f_SlavicNames))-1],
                          ' ',
                          snamef,'ovna',sep='')
                
            else:
                
                print('Human', gender,">", human_race)
                
                # Spanish Names shall be:
                # Given name + Surname
                
                print("Name: ",
                      f_SpanishNames[random.randint(1,len(f_SpanishNames))-1],
                      SpanishSurnames[random.randint(1,len(SpanishSurnames))-1],sep='')
            
        elif race == 'Fey':
            
            print('Fey', gender)

            # Fey F names shall be:
            # Given name + Family name + matronymic name
            # Matronymic name = dír/mír/kír/tír + mother's name
            # example: Adran Firahel dírEnna
            
            FeyMatronymic = ['dír','mír','kír','tír']
            
            print("Name: ",
                  f_FeyNames[random.randint(1,len(f_FeyNames))-1],' ',
                  fam_FeyNames[random.randint(1,len(fam_FeyNames))-1],' ',
                  FeyMatronymic[random.randint(1,len(FeyMatronymic))-1],
                  f_FeyNames[random.randint(1,len(f_FeyNames))-2],sep='')
            
        elif race == 'Dwarf':
            
            print('Dwarf', gender)

            # Dwarf F names shall be one of:
            # 1. Given name + father name + sdortirr
            # 2. Given name + clan name

            FdConnectors = ['daughter', 'clan']
            FdConnector = FdConnectors[random.randint(1,len(FdConnectors))-1]

            FdGiven = f_DwarfNames[random.randint(1,len(f_DwarfNames))-1]
            FdFather = m_DwarfNames[random.randint(1,len(m_DwarfNames))-1]
            FdClan = clan_DwarfNames[random.randint(1,len(clan_DwarfNames))-1]

            if FdConnector == 'daughter':
                print("Name: ",FdGiven,' ',FdFather,'sdortirr',sep='')
            else:
                print("Name: ",FdGiven,FdClan)
            
        elif race == 'Goblin':
            
            print('Goblin', gender)

            # Goblin F names shall be:
            # Given name + matronymic + patronymic
            # Matronymic name shall be:
            # Mother's name + tag, or tag + mother's name
            # Patronymic name shall be:
            # Father's name + gat, or gat + father's name

            FgobGiven = f_GoblinNames[random.randint(1,len(f_GoblinNames))-1]
            FgobMother = f_GoblinNames[random.randint(1,len(f_GoblinNames))-1]
            FgobFather = m_GoblinNames[random.randint(1,len(m_GoblinNames))-1]
            FgobPatron = random.randint(1,2)
            FgobMatron = random.randint(1,2)

            if FgobPatron == 1:
                FgobPatronPos = ['Gat',FgobFather.lower()]
            else:
                FgobPatronPos = [FgobFather,'gat']

            if FgobMatron == 1:
                FgobMatronPos = ['Tag',FgobMother.lower()]
            else:
                FgobMatronPos = [FgobMother,'tag']

            print("Name: ",
                  FgobGiven," ",
                  FgobMatronPos[0],FgobMatronPos[1]," ",
                  FgobPatronPos[0],FgobPatronPos[1],sep='') 
            
        elif race == 'Salimar':
            
            print('Salimar', gender)

            # Salimar F names shall be:
            # Given name + mother name (separated only by "-")

            FsalGiven = f_SalimarNames[random.randint(1,len(f_SalimarNames))-1]
            salMother = f_SalimarNames[random.randint(1,len(f_SalimarNames))-1]

            while FsalGiven == salMother:
                FsalGiven = f_SalimarNames[random.randint(1,len(f_SalimarNames))-1]
                salMother = f_SalimarNames[random.randint(1,len(f_SalimarNames))-1]
            else:
                print("Name: ",FsalGiven,"-",salMother.lower(),sep='')
            
        elif race == 'Treefolk':
            
            print('Treefolk', gender)

            # Treefolk F names shall be:
            # "Nickname" + family name + given name
            # Nickname shall be first 4 letters of given name
            # Family name shall be:
            # Mother's name + father's name (no spaces)

            FtreeGiven = f_TreefolkNames[random.randint(1,len(f_TreefolkNames))-1]
            FtreeNick = FtreeGiven[:4]
            FtreeMother = f_TreefolkNames[random.randint(1,len(f_TreefolkNames))-1]
            FtreeFather = m_TreefolkNames[random.randint(1,len(m_TreefolkNames))-1]

            print("Name: ",'"',FtreeNick,'"'," ",
                  FtreeMother,FtreeFather.lower()," ",FtreeGiven,sep='')
            
        elif race == 'Karhu':
            
            print('Karhu', gender)

            # Karhu F names shall be:
            # Given name + clan name

            FkarGiven = f_KarhuNames[random.randint(1,len(f_KarhuNames))-1]
            FkarClan = clan_KarhuNames[random.randint(1,len(clan_KarhuNames))-1]

            print("Name: ",FkarGiven, FkarClan)
            
        else:

            print('Lizardfolk', gender)

            # Lizardfolk F names shall be:
            # Given name + ' + clan name

            FlizName = f_LizardfolkNames[random.randint(1,len(f_LizardfolkNames))-1]
            FlizClan = clan_LizardfolkNames[random.randint(1,len(clan_LizardfolkNames))-1]

            print("Name: ",FlizName,"'",FlizClan.lower(),sep='')

    









