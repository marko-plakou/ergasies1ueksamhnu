#askhsh 2 se python 2
import datetime
import urllib2
import json

#arxikoihsh metavlhtwn kai dhlwsh listas.
cur_date=datetime.datetime.now()
mynums=[]
epitixies=[]
thesh=[]
#Εeisagwgh arithmwn apo ton xrhsth
for i in range(10):
    mynums[i]=int(input("dwse arithmo"))
#gia ton prohgumeno mhna kanw request gia diabasma twn dedomenwn stis sigkekrimens hmeromhnies.
for i in range(31):
    date1= date1 - datetime.timedelta(days=1)
    datetm= date1.strftime("%d-%m-%y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%datetm
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
#analush stoixeiwn javascript kai anazhthsh dedomenwn me values draws kai draw.
    data=json.loads(data)
    kl= data['draws']['draw']
    klhr=[]
#anazhthsh gia ta apotelesmata.
    for element in kl:
        pro=i["results"]
        sum=0
#sugkrish apotelesmatwn me tous arithmous toy xrhsth kai aykshsh toy metrhth.
        for i in mynums:
            if i in pro:
                sum+=1
        klhr.append(sum)
#anazhthsh tou megistu ths listas.
    max(klhr),klhr.count(max(klhr))
#h lista epitixies pairnei ws stoixeia tis epitixies pou eixe o xrhsths se mia hmera kai h lista thesh ths hmeres tou mhna.
    epitixies[i]= (max(klhr)*klhr.countmax(max(klhr)))
    thesh[i]=i
#eyresh megstu kai mhdenismos twn allwn stoixeiwn.
for K  in range (31):
    if epitixies[k+1]>epitixies[k]:
        epitixies[k]=0
#eyresh kai ektupwsh hmeras.
for j in range(31):
    if epitixies[j]!=0:
        date2=datetime.datetime.now()
        date3=date2.day
        if date3>thesh[j]:
            hm_epitixias=date2-datetime.timedelta(days=date3-thesh[j])
        else:
            hm_epitixias=date2-datetime.timedelta(days=(thesh[j]-date3)+date3)
print ("h hmera me thn megaluterh eitixia einai",hm_epitixias)            
