"""
For Testing
"""

import random
from character_data import *

sname = m_SlavicNames[random.randint(1,len(m_SlavicNames))-1]
sSuffix = sname[len(sname)-1:]

print(sname)
print(sSuffix)

if sSuffix != 'a' or 'e' or 'i' or 'o' or 'u':
    print(m_SlavicNames[random.randint(1,len(m_SlavicNames))-1],
          ' ',
          sname,'ovic',sep='')
else:
    print(m_SlavicNames[random.randint(1,len(m_SlavicNames))-1],
          ' ',
          sname[0:-1],'yevic',sep='')
