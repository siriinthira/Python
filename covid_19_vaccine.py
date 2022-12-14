# -*- coding: utf-8 -*-
"""Covid-19 vaccine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15DUIYx9D4ECmU_slRyfJ9_aLmvpQBAqQ
"""

# เขียนโปรแกรมหรือออกแบบ Algorithm สำหรับจัดการข้อมูลสถานะของประชากรในประเทศไทยที่ได้รับการฉีดวัคซีน Covid-19 โดยคุณลักษณะของโปรแกรมมีดังนี้
# เก็บสถานะการได้รับวัคซีน (0: ยังไม่ได้รับวัคซีน, 1: ได้รับวัคซีนแล้ว 1 เข็ม, 2: ได้รับวัคซีนแล้ว 2 เข็ม)
# สามารถเรียกดูสถานะการได้รับฉีดวัคซีนของประชากรแต่ละคน
# สามารถนับจำนวนประชากรที่ได้รับวัคซีน โดยแยกตามสถานะได้

from random import randint
import random
case=[]
count=1
case0=''
case1=''
case2=''
for x in range(1,11):
    if x%2!=0:
        case.append('person : '+str(count))
        count=count+1
    else:
        number = randint(0,2)
        case.append('case : '+str(number))
for x in range(1,10,2):
    if case[x]=='case : 0':
        case0=case0+case[x-1]
    elif case[x]=='case : 1':
        case1=case1+case[x-1]
    elif case[x]=='case : 2':
        case2=case2+case[x-1]
print(case)
print("case 0 : "+case0)
print("case 1 : "+case1)
print("case 2 : "+case2)

import array as th_population
id_1234567891111 = [1, "Tina Fey"]
id_1234567891112 = [1, "Lady Gaga"]
id_1254567891113 = [2, "Ray Macdonald"]
id_1234567891114 = [0, "Thomas Edison"]
th_population = [id_1234567891111, id_1234567891112, id_1254567891113, id_1234567891114]


print(id_1254567891113)

no_vaccine = 0
one_shot_vaccine = 0
two_shot_vaccine = 0

for x in th_population:
  if x[0] == 0:
    no_vaccine+= 1
  elif x[0] == 1:
    one_shot_vaccine+=1
  else :two_shot_vaccine+=1
print(one_shot_vaccine, "people have one vaccine" )
print(two_shot_vaccine, "people have two vaccines")
print(no_vaccine, "people have not received any vaccine")
