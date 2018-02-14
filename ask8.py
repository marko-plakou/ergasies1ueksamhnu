#askhsh 8 se python 3
import random
lista=[]
#dhmiourgeia listas me 30 tuxaius arithmus.
for n in range (30):
    lista.append(random.randint(-30,30))
print (lista)
#arxikopoihsh metavlhtwn.
k=0
i=0
j=1
l=2
#to m einai 29  γιατί oi prwtes duo theseis ths listas exun kaliuthei apo to i kai to i+1.
m=29
#to prwto stoixeio ths triadas pou elegxete kathorizete apo to i kai h diadikasia eanalbanete 28 fores.
for i in range(0,29):
#kathe fora to deytero stoixeio ksekina  mia thesh meta to prwto  kai eksetazei gia to trito m fores. 
    for j in range((i+1), m):
#to trito stoixeo pou sigkrinete  ksekinaei mia thesh metato deytero kai sunexizei m wste na ftasei sthn teleytai thesh ths listas.
        for l in range((j+1),30):
#ean to athroisma tws triwn stoixeiwn einai mhden tote o metrhths ayksanei kata 1.
            if (lista[i]+lista[j]+lista[l]==0):
                print (lista[i],lista[j],lista[l])
                k=1
#to m meiwnetai kathe fora pou ekteleite to i etsi wste oi anazhthseis tou tritoi stoixeiou na meiwnontai kata ena.
m-=1
#ean o metrhths arameinei mhdes ote den uparxei triada arithmwn.
if k==0:
    print("DEN VRETHIKAN ZEYGOI")
    

