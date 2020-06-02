"""
D&D Character Generator
-----------------------
Based on the Tiny Dungeon characters

By Morleidr
"""

import random
from character_data import *

##import importlib
##
##importlib.import_module('character_data')

genders = ['Male','Female']
g_count = len(genders)
g_roll = random.randint(1,g_count)-1
gender = genders[g_roll]

print(gender)

if gender == 'Male':
    lf_roll = random.randint(1,len(m_LizardfolkNames))-1
    print("Name: ", m_LizardfolkNames[lf_roll])
else:
    lf_roll = random.randint(1,len(f_LizardfolkNames))-1
    print(f_LizardfolkNames[lf_roll])

    









