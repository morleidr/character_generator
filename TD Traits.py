"""
TD Traits Generator
"""

import random

charTraits = []

while len(charTraits) < 3:
    input("Press Enter to choose a trait\n")
    traits = ['Acrobat','Alchemist','Armor Master','Barfighter','Beastspeaker',
              'Berserker','Blacksmith','Brawler','Charismatic','Cleave',
              'Dark-fighter','Defender','Diehard','Drunken Master','Dungeoneer',
              'Educated','Eidetic Memory','Familiar','Fleet of Foot','Healer',
              'Insightful','Lucky','Marksman','Martial Artist','Nimble Fingers',
              'Opportunist','Perceptive','Quartermaster','Quick Shot','Resolute',
              'Shield Bearer','Sneaky','Spell Reader','Spell-Touched','Strong',
              'Survivalist','Tough','Tracker','Trapmaster','Vigilant']

    charTrait = traits[random.randint(0,len(traits))-1]
    charTraits.append(charTrait)
    traits.remove(charTrait)
    print(charTraits)


another = input("Need another (for human)?\n"
                "Answer 'y' or 'n'\n")

while another not in ('y','n'):
    another = input("Need another (for human)?\n"
                    "Answer 'y' or 'n'\n")
    

if another == 'n':
    print("Very well. Good luck, traveller!")
    #break

    
if another == 'y':
    charTrait = traits[random.randint(0,len(traits))-1]
    charTraits.append(charTrait)
    traits.remove(charTrait)
    print(charTraits)
