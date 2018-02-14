#askhsh 7 se python 3
import datetime
#arxikopoihsh metavlhtwn.
current_date=datetime.date.today()
day1=current_date.day
year=current_date.year
day_of_wk1=current_date.isoweekday()
day2=0
k=0
new_year=0
new_day=0
for i in range(1,11):
#elengxw ean o sygkekrimenos xronos einai disektos kai prosthetw tis analoges meres sto sugkekrimeno etos.
    if (i==0):
        if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
            new_date=(current_date+(datetime.timedelta(days=(366))))
            new_year=new_date.year
        else:
            new_date=(current_date+(datetime.timedelta(days=(365))))
            new_year=new_date.year
#elenxw ean kapoio apo ta epomena 10 xronia einai disekta kai prosthetw tis analoges meres sto ekastote etos.        
    else:
        if (( new_year%400 == 0)or ( new_year%4 == 0 )) and ( new_year%100 != 0):
            new_date=(current_date+(datetime.timedelta(days=(i*366))))
            new_year=new_date.year
        else:
            new_date=(current_date+ (datetime.timedelta(days=(i*365))))
            new_year=new_date.year
#apomononw thn nea hmera toy mhna etsi wste na eksetasw  ean einai prin h meta apo thn shmerinh.
        day2=new_date.day
#ean einai pio prin h ises prosthetw thn diafora ths shmerinhs apo thn nea wste na parw san apotelesma thn akribh shmerinh hmera (p.x 8) toy mhna ton epomeno xrono.
    if (day1>=day2):
        new_date=new_date+(datetime.timedelta(days=(day1-day2)))
#ean einai pio prin tote tis afairw thn diafora ths neas apo thn shmerinh wste na arw to apotelesma opws kai prin.
    else:
        new_date=new_date-(datetime.timedelta(days=(day2-day1)))
#apo thn nea ayth hmeromhnia  (h opoia tha einai idia me thn shmerinh me monh diafora to etos)vriskw thn hmera ths evdomadas poy antistoixei h sugkekrimenh hmeromhnia.
    day_of_wk2=new_date.isoweekday()
#eksetazw ean h h mera ths ebdomadas einai idia me thn shmerinh kai afu h hmera toy mhna einai h idia  katalhgw ean uparxei hmera toy epomenu xronu pou na einai h idia me thn shmerinh.
#kai ayksanw analoga ton metrhth k.
    if (day_of_wk1==day_of_wk2):
        k+=1
#h diadikasia eanalambanete alles 9 fores gia na eksetasw kai ta epomena xronia.
print ("oi hmeres pou einai ides ta epomena 10 xronia einai",k ,".")
