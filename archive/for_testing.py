"""
For Testing
"""

import random
from character_data import *


# Lizardfolk F names shall be:
# Given name + ' + clan name

FlizName = f_LizardfolkNames[random.randint(1,len(f_LizardfolkNames))-1]
FlizClan = clan_LizardfolkNames[random.randint(1,len(clan_LizardfolkNames))-1]

print(FlizName,"'",FlizClan.lower(),sep='')
