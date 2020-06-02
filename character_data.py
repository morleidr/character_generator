"""
Character Races and Names
"""

import xlrd

path = "Character Traits.xlsx"

inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

val = '' 


#   Genders
genders = ['Male','Female']



#   Races
races = []
for y in range(2, inputWorksheet.nrows):
    races.append(inputWorksheet.cell_value(y,1))
try:
    while True:
        races.remove(val)
except ValueError:
    pass



#   Human Races
human_races = []
for y in range(2, inputWorksheet.nrows):
    human_races.append(inputWorksheet.cell_value(y,2))
try:
    while True:
        human_races.remove(val)
except ValueError:
    pass



#   Female Arabic Names
f_ArabicNames = []
for y in range(2,inputWorksheet.nrows):
    f_ArabicNames.append(inputWorksheet.cell_value(y,4))
try:
    while True:
        f_ArabicNames.remove(val)
except ValueError:
    pass



#   Male Arabic Names
m_ArabicNames = []
for y in range(2,inputWorksheet.nrows):
    m_ArabicNames.append(inputWorksheet.cell_value(y,5))
try:
    while True:
        m_ArabicNames.remove(val)
except ValueError:
    pass



#   Female Celtic Names
f_CelticNames = []
for y in range(2,inputWorksheet.nrows):
    f_CelticNames.append(inputWorksheet.cell_value(y,6))
try:
    while True:
        f_CelticNames.remove(val)
except ValueError:
    pass



#   Male Celtic Names
m_CelticNames = []
for y in range(2,inputWorksheet.nrows):
    m_CelticNames.append(inputWorksheet.cell_value(y,7))
try:
    while True:
        m_CelticNames.remove(val)
except ValueError:
    pass



#   Female Chinese Names
f_ChineseNames = []
for y in range(2,inputWorksheet.nrows):
    f_ChineseNames.append(inputWorksheet.cell_value(y,8))
try:
    while True:
        f_ChineseNames.remove(val)
except ValueError:
    pass



#   Male Chinese Names
m_ChineseNames = []
for y in range(2,inputWorksheet.nrows):
    m_ChineseNames.append(inputWorksheet.cell_value(y,9))
try:
    while True:
        m_ChineseNames.remove(val)
except ValueError:
    pass


#   Family Chinese Names
fam_ChineseNames = []
for y in range(2,inputWorksheet.nrows):
    fam_ChineseNames.append(inputWorksheet.cell_value(y,10))
try:
    while True:
        fam_ChineseNames.remove(val)
except ValueError:
    pass


#   Female Egyptian Names
f_EgyptianNames = []
for y in range(2,inputWorksheet.nrows):
    f_EgyptianNames.append(inputWorksheet.cell_value(y,11))
try:
    while True:
        f_EgyptianNames.remove(val)
except ValueError:
    pass


#   Male Egyptian Names
m_EgyptianNames = []
for y in range(2,inputWorksheet.nrows):
    m_EgyptianNames.append(inputWorksheet.cell_value(y,12))
try:
    while True:
        m_EgyptianNames.remove(val)
except ValueError:
    pass


#   Female English Names
f_EnglishNames = []
for y in range(2,inputWorksheet.nrows):
    f_EnglishNames.append(inputWorksheet.cell_value(y,13))
try:
    while True:
        f_EnglishNames.remove(val)
except ValueError:
    pass


#   Male English Names
m_EnglishNames = []
for y in range(2,inputWorksheet.nrows):
    m_EnglishNames.append(inputWorksheet.cell_value(y,14))
try:
    while True:
        m_EnglishNames.remove(val)
except ValueError:
    pass


#   Female French Names
f_FrenchNames = []
for y in range(2,inputWorksheet.nrows):
    f_FrenchNames.append(inputWorksheet.cell_value(y,15))
try:
    while True:
        f_FrenchNames.remove(val)
except ValueError:
    pass


#   Male French Names
m_FrenchNames = []
for y in range(2,inputWorksheet.nrows):
    m_FrenchNames.append(inputWorksheet.cell_value(y,16))
try:
    while True:
        m_FrenchNames.remove(val)
except ValueError:
    pass


#   Female German Names
f_GermanNames = []
for y in range(2,inputWorksheet.nrows):
    f_GermanNames.append(inputWorksheet.cell_value(y,17))
try:
    while True:
        f_GermanNames.remove(val)
except ValueError:
    pass


#   Male German Names
m_GermanNames = []
for y in range(2,inputWorksheet.nrows):
    m_GermanNames.append(inputWorksheet.cell_value(y,18))
try:
    while True:
        m_GermanNames.remove(val)
except ValueError:
    pass


#   Female Greek Names
f_GreekNames = []
for y in range(2,inputWorksheet.nrows):
    f_GreekNames.append(inputWorksheet.cell_value(y,19))
try:
    while True:
        f_GreekNames.remove(val)
except ValueError:
    pass


#   Male Greek Names
m_GreekNames = []
for y in range(2,inputWorksheet.nrows):
    m_GreekNames.append(inputWorksheet.cell_value(y,20))
try:
    while True:
        m_GreekNames.remove(val)
except ValueError:
    pass


#   Female Indian Names
f_IndianNames = []
for y in range(2,inputWorksheet.nrows):
    f_IndianNames.append(inputWorksheet.cell_value(y,21))
try:
    while True:
        f_IndianNames.remove(val)
except ValueError:
    pass


#   Male Indian Names
m_IndianNames = []
for y in range(2,inputWorksheet.nrows):
    m_IndianNames.append(inputWorksheet.cell_value(y,22))
try:
    while True:
        m_IndianNames.remove(val)
except ValueError:
    pass


#   Female Japanese Names
f_JapaneseNames = []
for y in range(2,inputWorksheet.nrows):
    f_JapaneseNames.append(inputWorksheet.cell_value(y,23))
try:
    while True:
        f_JapaneseNames.remove(val)
except ValueError:
    pass


#   Male Japanese Names
m_JapaneseNames = []
for y in range(2,inputWorksheet.nrows):
    m_JapaneseNames.append(inputWorksheet.cell_value(y,24))
try:
    while True:
        m_JapaneseNames.remove(val)
except ValueError:
    pass


#   Female Mesoamerican Names
f_MesoamericanNames = []
for y in range(2,inputWorksheet.nrows):
    f_MesoamericanNames.append(inputWorksheet.cell_value(y,25))
try:
    while True:
        f_MesoamericanNames.remove(val)
except ValueError:
    pass


#   Male Mesoamerican Names
m_MesoamericanNames = []
for y in range(2,inputWorksheet.nrows):
    m_MesoamericanNames.append(inputWorksheet.cell_value(y,26))
try:
    while True:
        m_MesoamericanNames.remove(val)
except ValueError:
    pass


#   Female Congolese Names
f_CongoleseNames = []
for y in range(2,inputWorksheet.nrows):
    f_CongoleseNames.append(inputWorksheet.cell_value(y,27))
try:
    while True:
        f_CongoleseNames.remove(val)
except ValueError:
    pass


#   Male Congolese Names
m_CongoleseNames = []
for y in range(2,inputWorksheet.nrows):
    m_CongoleseNames.append(inputWorksheet.cell_value(y,28))
try:
    while True:
        m_CongoleseNames.remove(val)
except ValueError:
    pass


#   Female Norse Names
f_NorseNames = []
for y in range(2,inputWorksheet.nrows):
    f_NorseNames.append(inputWorksheet.cell_value(y,29))
try:
    while True:
        f_NorseNames.remove(val)
except ValueError:
    pass


#   Male Norse Names
m_NorseNames = []
for y in range(2,inputWorksheet.nrows):
    m_NorseNames.append(inputWorksheet.cell_value(y,30))
try:
    while True:
        m_NorseNames.remove(val)
except ValueError:
    pass


#   Female Polynesian Names
f_PolynesianNames = []
for y in range(2,inputWorksheet.nrows):
    f_PolynesianNames.append(inputWorksheet.cell_value(y,31))
try:
    while True:
        f_PolynesianNames.remove(val)
except ValueError:
    pass


#   Male Polynesian Names
m_PolynesianNames = []
for y in range(2,inputWorksheet.nrows):
    m_PolynesianNames.append(inputWorksheet.cell_value(y,32))
try:
    while True:
        m_PolynesianNames.remove(val)
except ValueError:
    pass


#   Female Roman Names
f_RomanNames = []
for y in range(2,inputWorksheet.nrows):
    f_RomanNames.append(inputWorksheet.cell_value(y,33))
try:
    while True:
        f_RomanNames.remove(val)
except ValueError:
    pass


#   Male Roman Names
m_RomanNames = []
for y in range(2,inputWorksheet.nrows):
    m_RomanNames.append(inputWorksheet.cell_value(y,34))
try:
    while True:
        m_RomanNames.remove(val)
except ValueError:
    pass


#   Female Slavic Names
f_SlavicNames = []
for y in range(2,inputWorksheet.nrows):
    f_SlavicNames.append(inputWorksheet.cell_value(y,35))
try:
    while True:
        f_SlavicNames.remove(val)
except ValueError:
    pass


#   Male Slavic Names
m_SlavicNames = []
for y in range(2,inputWorksheet.nrows):
    m_SlavicNames.append(inputWorksheet.cell_value(y,36))
try:
    while True:
        m_SlavicNames.remove(val)
except ValueError:
    pass


#   Female Spanish Names
f_SpanishNames = []
for y in range(2,inputWorksheet.nrows):
    f_SpanishNames.append(inputWorksheet.cell_value(y,37))
try:
    while True:
        f_SpanishNames.remove(val)
except ValueError:
    pass


#   Male Spanish Names
m_SpanishNames = []
for y in range(2,inputWorksheet.nrows):
    m_SpanishNames.append(inputWorksheet.cell_value(y,38))
try:
    while True:
        m_SpanishNames.remove(val)
except ValueError:
    pass


#   Female Fey Names
f_FeyNames = []
for y in range(2,inputWorksheet.nrows):
    f_FeyNames.append(inputWorksheet.cell_value(y,39))
try:
    while True:
        f_FeyNames.remove(val)
except ValueError:
    pass


#   Male Fey Names
m_FeyNames = []
for y in range(2,inputWorksheet.nrows):
    m_FeyNames.append(inputWorksheet.cell_value(y,40))
try:
    while True:
        m_FeyNames.remove(val)
except ValueError:
    pass


#   Family Fey Names
fam_FeyNames = []
for y in range(2,inputWorksheet.nrows):
    fam_FeyNames.append(inputWorksheet.cell_value(y,41))
try:
    while True:
        fam_FeyNames.remove(val)
except ValueError:
    pass


#   Female Dwarf Names
f_DwarfNames = []
for y in range(2,inputWorksheet.nrows):
    f_DwarfNames.append(inputWorksheet.cell_value(y,42))
try:
    while True:
        f_DwarfNames.remove(val)
except ValueError:
    pass


#   Male Dwarf Names
m_DwarfNames = []
for y in range(2,inputWorksheet.nrows):
    m_DwarfNames.append(inputWorksheet.cell_value(y,43))
try:
    while True:
        m_DwarfNames.remove(val)
except ValueError:
    pass


#   Clan Dwarf Names
clan_DwarfNames = []
for y in range(2,inputWorksheet.nrows):
    clan_DwarfNames.append(inputWorksheet.cell_value(y,44))
try:
    while True:
        clan_DwarfNames.remove(val)
except ValueError:
    pass


#   Female Goblin Names
f_GoblinNames = []
for y in range(2,inputWorksheet.nrows):
    f_GoblinNames.append(inputWorksheet.cell_value(y,45))
try:
    while True:
        f_GoblinNames.remove(val)
except ValueError:
    pass


#   Male Goblin Names
m_GoblinNames = []
for y in range(2,inputWorksheet.nrows):
    m_GoblinNames.append(inputWorksheet.cell_value(y,46))
try:
    while True:
        m_GoblinNames.remove(val)
except ValueError:
    pass


#   Clan Goblin Names
clan_GoblinNames = []
for y in range(2,inputWorksheet.nrows):
    clan_GoblinNames.append(inputWorksheet.cell_value(y,47))
try:
    while True:
        clan_GoblinNames.remove(val)
except ValueError:
    pass


#   Female Salimar Names
f_SalimarNames = []
for y in range(2,inputWorksheet.nrows):
    f_SalimarNames.append(inputWorksheet.cell_value(y,48))
try:
    while True:
        f_SalimarNames.remove(val)
except ValueError:
    pass


#   Male Salimar Names
m_SalimarNames = []
for y in range(2,inputWorksheet.nrows):
    m_SalimarNames.append(inputWorksheet.cell_value(y,49))
try:
    while True:
        m_SalimarNames.remove(val)
except ValueError:
    pass


#   Female Treefolk Names
f_TreefolkNames = []
for y in range(2,inputWorksheet.nrows):
    f_TreefolkNames.append(inputWorksheet.cell_value(y,50))
try:
    while True:
        f_TreefolkNames.remove(val)
except ValueError:
    pass


#   Male Salimar Names
m_TreefolkNames = []
for y in range(2,inputWorksheet.nrows):
    m_TreefolkNames.append(inputWorksheet.cell_value(y,51))
try:
    while True:
        m_TreefolkNames.remove(val)
except ValueError:
    pass


#   Female Karhu Names
f_KarhuNames = []
for y in range(2,inputWorksheet.nrows):
    f_KarhuNames.append(inputWorksheet.cell_value(y,52))
try:
    while True:
        f_KarhuNames.remove(val)
except ValueError:
    pass


#   Male Karhu Names
m_KarhuNames = []
for y in range(2,inputWorksheet.nrows):
    m_KarhuNames.append(inputWorksheet.cell_value(y,53))
try:
    while True:
        m_KarhuNames.remove(val)
except ValueError:
    pass


#   Clan Karhu Names
clan_KarhuNames = []
for y in range(2,inputWorksheet.nrows):
    clan_KarhuNames.append(inputWorksheet.cell_value(y,54))
try:
    while True:
        clan_KarhuNames.remove(val)
except ValueError:
    pass


#   Female Lizardfolk Names
f_LizardfolkNames = []
for y in range(2,inputWorksheet.nrows):
    f_LizardfolkNames.append(inputWorksheet.cell_value(y,55))
try:
    while True:
        f_LizardfolkNames.remove(val)
except ValueError:
    pass


#   Male Lizardfolk Names
m_LizardfolkNames = []
for y in range(2,inputWorksheet.nrows):
    m_LizardfolkNames.append(inputWorksheet.cell_value(y,56))
try:
    while True:
        m_LizardfolkNames.remove(val)
except ValueError:
    pass


#   Clan Lizardfolk Names
clan_LizardfolkNames = []
for y in range(2,inputWorksheet.nrows):
    clan_LizardfolkNames.append(inputWorksheet.cell_value(y,57))
try:
    while True:
        clan_LizardfolkNames.remove(val)
except ValueError:
    pass


#   List of Nouns
Nouns = []
for y in range(2,inputWorksheet.nrows):
    Nouns.append(inputWorksheet.cell_value(y,58))
try:
    while True:
        Nouns.remove(val)
except ValueError:
    pass

#   List of Places
Places = []
for y in range(2,inputWorksheet.nrows):
    Places.append(inputWorksheet.cell_value(y,61))
try:
    while True:
        Places.remove(val)
except ValueError:
    pass



##print(Nouns)
##print(m_LizardfolkNames)
##print(clan_LizardfolkNames)







